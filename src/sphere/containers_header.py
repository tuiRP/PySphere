from collections import deque

class CSError(Exception):
    def __init__(self, log_level, error_code, message):
        super().__init__(f"[{log_level}] Error {error_code}: {message}")

class ThreadSafeQueue:
    def __init__(self):
        self._queue = deque()
        self._head_index = 0
        self._tail_index = 0
        self._queue.append(None)  # at least one element must be in the queue

    def push(self, value):
        self._queue.append(value)
        self._tail_index += 1
        self.clean()

    def clean(self):
        while len(self._queue) > 1 and self._head_index > 0:
            self._queue.popleft()
            self._head_index -= 1
            self._tail_index -= 1

    def size(self):
        return max(0, self._tail_index - self._head_index)

    def empty(self):
        return self.size() == 0

    def pop(self):
        if self.empty():
            raise CSError("LOGL_ERROR", 0, "No elements to read from queue.")
        self._head_index += 1

    def front(self):
        if not self.empty():
            return self._queue[self._head_index + 1]
        raise CSError("LOGL_ERROR", 0, "No elements to read from queue.")

# Exemplo de uso
if __name__ == "__main__":
    queue = ThreadSafeQueue()
    queue.push("first")
    queue.push("second")
    
    print("Front element:", queue.front())
    queue.pop()
    print("Next element:", queue.front())
    queue.pop()

    # Tentar acessar um elemento quando a fila está vazia
    try:
        queue.pop()
    except CSError as e:
        print(e)
