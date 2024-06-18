import os
import threading
import ctypes
from ctypes import wintypes
import logging

class CSError(Exception):
    @staticmethod
    def GetSystemErrorMessage(error_code, buffer, size):
        # Retrieve the system error message for the provided error code
        message_length = ctypes.windll.kernel32.FormatMessageW(
            ctypes.FORMAT_MESSAGE_FROM_SYSTEM,
            None,
            error_code,
            0,
            buffer,
            size,
            None
        )
        return message_length

class CNTService:
    def __init__(self):
        self._status_handle = None
        self._server_stop_event = threading.Event()
        self._is_nt_service = False
        self._status = {}

    def _on_tick(self):
        if not self._is_nt_service or self._status["current_state"] != "SERVICE_STOP_PENDING":
            return True

        self.set_service_status("SERVICE_STOP_PENDING", 0, 1000)
        g_Serv.set_exit_flag(4)
        return False

    def set_service_status(self, current_state, win32_exit_code, wait_hint):
        if current_state == "SERVICE_START_PENDING":
            self._status["controls_accepted"] = 0
        else:
            self._status["controls_accepted"] = "SERVICE_ACCEPT_STOP"

        self._status["current_state"] = current_state
        self._status["win32_exit_code"] = win32_exit_code
        self._status["wait_hint"] = wait_hint

        if current_state in ("SERVICE_RUNNING", "SERVICE_STOPPED"):
            self._status["checkpoint"] = 0
        else:
            self._status["checkpoint"] += 1

        success = ctypes.windll.advapi32.SetServiceStatus(self._status_handle, ctypes.byref(self._status))
        if not success and self._is_nt_service:
            error_msg = self.get_last_error_text(ctypes.create_unicode_buffer(256), 256)
            self.report_event("EVENTLOG_ERROR_TYPE", 0, "SetServiceStatus", error_msg)

        return success

    def service_ctrl(self, ctrl_code):
        if ctrl_code == "SERVICE_CONTROL_STOP":
            self.service_stop()
        self.set_service_status(self._status["current_state"], 0, 0)

    def service_main(self, argc, argv):
        self.service_start_main(argc, argv)

    def service_start_main(self, argc, argv):
        self._status_handle = ctypes.windll.advapi32.RegisterServiceCtrlHandlerW(argv[0], self.service_ctrl)
        if not self._status_handle:
            logging.error("RegisterServiceCtrlHandler failed")
            return

        self._status["service_type"] = "SERVICE_WIN32_OWN_PROCESS"
        self._status["service_specific_exit_code"] = 0

        if self.set_service_status("SERVICE_START_PENDING", 0, 3000):
            self.service_start(argc, argv)

        self.set_service_status("SERVICE_STOPPED", 0, 0)

    def service_start(self, argc, argv):
        self.report_event("EVENTLOG_INFORMATION_TYPE", 0, "Service start pending.")
        if not self.set_service_status("SERVICE_START_PENDING", 0, 3000):
            return -1

        self._server_stop_event.clear()
        self._server_stop_event.wait(timeout=3000)

        if not self.set_service_status("SERVICE_START_PENDING", 0, 3000):
            return -1

        h_events = [self._server_stop_event, threading.Event()]

        if not h_events[1].wait(timeout=3000):
            return -1

        p_sd = ctypes.create_string_buffer(ctypes.SECURITY_DESCRIPTOR_MIN_LENGTH)
        if not ctypes.windll.advapi32.InitializeSecurityDescriptor(p_sd, 1):
            return -1

        if not ctypes.windll.advapi32.SetSecurityDescriptorDacl(p_sd, True, None, False):
            return -1

        sa = ctypes.wintypes.SECURITY_ATTRIBUTES()
        sa.nLength = ctypes.sizeof(sa)
        sa.lpSecurityDescriptor = ctypes.byref(p_sd)
        sa.bInheritHandle = True

        if not self.set_service_status("SERVICE_START_PENDING", 0, 3000):
            return -1

        pipe_name = f"\\\\.\\pipe\\{os.path.basename(__file__)}\\{g_Serv.get_name()}"

        h_pipe = ctypes.windll.kernel32.CreateNamedPipeW(
            pipe_name,
            ctypes.wintypes.FILE_FLAG_OVERLAPPED | ctypes.wintypes.PIPE_ACCESS_DUPLEX,
            ctypes.wintypes.PIPE_TYPE_MESSAGE | ctypes.wintypes.PIPE_READMODE_MESSAGE | ctypes.wintypes.PIPE_WAIT,
            1, 0, 0, 1000, ctypes.byref(sa)
        )
        if h_pipe == ctypes.wintypes.INVALID_HANDLE_VALUE:
            self.report_event("EVENTLOG_ERROR_TYPE", 0, "Can't create named pipe. Check multi-instance?", self.get_last_error_text(ctypes.create_unicode_buffer(256), 256))
            return -1

        if self.set_service_status("SERVICE_RUNNING", 0, 0):
            rc = Sphere_MainEntryPoint(argc, argv)
            if not rc:
                self.report_event("EVENTLOG_INFORMATION_TYPE", 0, "service stopped", self.get_last_error_text(ctypes.create_unicode_buffer(256), 256))
            else:
                self.report_event("EVENTLOG_ERROR_TYPE", 0, "service stopped abnormally", str(rc))

        else:
            self.report_event("EVENTLOG_ERROR_TYPE", 0, "ServiceStart failed.")

        ctypes.windll.kernel32.CloseHandle(h_pipe)
        return 0

    def service_stop(self):
        self.report_event("EVENTLOG_INFORMATION_TYPE", 0, "Attempting to stop service")
        self._status["current_state"] = "SERVICE_STOP_PENDING"
        self.set_service_status(self._status["current_state"], 0, 3000)
        self._server_stop_event.set()

    def cmd_install_service(self):
        pass  # Implement the service installation logic

    def cmd_remove_service(self):
        pass  # Implement the service removal logic

    def cmd_main_start(self):
        self._is_nt_service = True
        service_name = f"{os.path.basename(__file__)} - {g_Serv.get_name()}"
        service_table = [
            (service_name, self.service_main),
            (None, None)
        ]

        if not ctypes.windll.advapi32.StartServiceCtrlDispatcherW(service_table):
            self.report_event("EVENTLOG_ERROR_TYPE", 0, "StartServiceCtrlDispatcher", self.get_last_error_text(ctypes.create_unicode_buffer(256), 256))

    def report_event(self, event_type, event_id, msg, args=None):
        logging.log(event_type, f"{msg} {args}")

    @staticmethod
    def get_last_error_text(buffer, size):
        error_code = ctypes.windll.kernel32.GetLastError()
        msg_len = CSError.GetSystemErrorMessage(error_code, buffer, size)
        buffer.value += f" (0x{error_code:X})"
        return buffer.value


class SphereServer:
    def __init__(self):
        self._name = "SphereServer"

    def get_name(self):
        return self._name

    def set_exit_flag(self, flag):
        pass  # Implement the exit flag logic

def Sphere_MainEntryPoint(argc, argv):
    pass  # Implement the main entry point logic

# Mock the global objects
g_Serv = SphereServer()
g_NTService = CNTService()

if __name__ == "__main__":
    g_NTService.cmd_main_start()
