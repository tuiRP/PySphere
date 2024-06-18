"""
threads.py
"""

from threading import Lock
from threads_header import AbstractSphereThread

class SphereThread(AbstractSphereThread):
    def __init__(self, name, priority):
        super().__init__(name, priority)
        self._lock = Lock()

    def onStart(self):
        print(f"Thread {self.name} started with priority {self.priority}")

    def tick(self):
        print(f"Thread {self.name} ticking...")
        # Implement the main logic of the thread here

    def onTerminate(self):
        print(f"Thread {self.name} terminated")
