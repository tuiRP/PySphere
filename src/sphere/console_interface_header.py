from enum import Enum
import threading
from collections import deque

class ConsoleTextColor(Enum):
    CTCOL_DEFAULT = 0
    CTCOL_RED = 1
    CTCOL_GREEN = 2
    CTCOL_YELLOW = 3
    CTCOL_BLUE = 4
    CTCOL_MAGENTA = 5
    CTCOL_CYAN = 6
    CTCOL_WHITE = 7
    CTCOL_QTY = 8

class ConsoleOutput:
    def __init__(self, log_color=ConsoleTextColor.CTCOL_DEFAULT, log_string=""):
        self._iTextColor = log_color
        self._sTextString = log_string

    def GetTextColor(self):
        return self._iTextColor

    def GetTextString(self):
        return self._sTextString

class ConsoleInterface:
    def __init__(self):
        self._ciQueueMutex = threading.Lock()
        self._ciQueueCV = threading.Condition(self._ciQueueMutex)
        self._qOutput = deque()

    @staticmethod
    def CTColToRGB(color):
        def MakeRGB(r, g, b):
            return (r | (g << 8) | (b << 16))
        
        if color == ConsoleTextColor.CTCOL_RED:
            return MakeRGB(255, 0, 0)
        elif color == ConsoleTextColor.CTCOL_GREEN:
            return MakeRGB(0, 255, 0)
        elif color == ConsoleTextColor.CTCOL_YELLOW:
            return MakeRGB(127, 127, 0)
        elif color == ConsoleTextColor.CTCOL_BLUE:
            return MakeRGB(0, 0, 255)
        elif color == ConsoleTextColor.CTCOL_MAGENTA:
            return MakeRGB(255, 0, 255)
        elif color == ConsoleTextColor.CTCOL_CYAN:
            return MakeRGB(0, 127, 255)
        elif color == ConsoleTextColor.CTCOL_WHITE:
            return MakeRGB(255, 255, 255)
        else:
            return MakeRGB(175, 175, 175)

    def AddConsoleOutput(self, output):
        with self._ciQueueMutex:
            self._qOutput.append(output)
            self._ciQueueCV.notify()

# Exemplo de uso
if __name__ == "__main__":
    console = ConsoleInterface()
    output = ConsoleOutput(ConsoleTextColor.CTCOL_RED, "Error message")
    console.AddConsoleOutput(output)

    for item in console._qOutput:
        print(item.GetTextString())
