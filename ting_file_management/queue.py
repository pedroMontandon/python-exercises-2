from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self.queue_length = 0

    def __len__(self):
        return self.queue_length

    def enqueue(self, value):
        self._data.append(value)
        self.queue_length += 1

    def dequeue(self):
        if len(self._data) == 0:
            return None
        self.queue_length -= 1
        return self._data.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError("Índice Inválido ou Inexistente")
        try:
            return self._data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
