from .redis import RedisCrud


class LineCommunicationStateCrud:
    def __init__(self):
        self.crud = RedisCrud(db=1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.crud.__exit__(exc_type, exc_value, traceback)

    def _get(self, key):
        return self.crud.get(key)

    def _set(self, key, value):
        return self.crud.set(key, value)

    def _delete(self, key):
        return self.crud.delete(key)

    def create(self, line_id, data):
        self._set(line_id, data)

    def get(self, line_id):
        return self._get(line_id)

    def delete(self, line_id):
        self._delete(line_id)
