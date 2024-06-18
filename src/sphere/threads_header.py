"""
threads_header.py
"""

from threading import Thread, Lock, Event

class AbstractSphereThread(Thread):
    def __init__(self, name, priority):
        super().__init__()
        self.name = name
        self.priority = priority
        self.exit_flag = Event()
    
    def run(self):
        self.onStart()
        while not self.exit_flag.is_set():
            self.tick()
        self.onTerminate()

    def onStart(self):
        pass
    
    def tick(self):
        pass
    
    def onTerminate(self):
        pass
    
    def terminate(self):
        self.exit_flag.set()
