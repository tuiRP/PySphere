# ProfileData.py

from ProfileTask import ProfileTask

class PROFILE_TYPE:
    OVERHEAD = 0
    IDLE = 1
    SLEEP = 2
    TIME_QTY = 3

class ProfileData:
    def __init__(self):
        self.reset()

    def count(self, profile_type, count):
        self.m_counts[profile_type] += count
        self.m_tasks[profile_type].count(count)

    def get_total_count(self, profile_type):
        return self.m_counts[profile_type]

    def reset(self):
        self.m_counts = [0] * PROFILE_TYPE.TIME_QTY
        self.m_tasks = [ProfileTask() for _ in range(PROFILE_TYPE.TIME_QTY)]

    def task_count(self, count):
        self.m_counts[PROFILE_TYPE.OVERHEAD] += count
        self.m_tasks[PROFILE_TYPE.OVERHEAD].count(count)
