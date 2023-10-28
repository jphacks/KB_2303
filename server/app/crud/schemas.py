class AdminSessionSchema:
    admin_id: int

    def __init__(self, admin_id: int = None):
        self.admin_id = admin_id


class LINECommunicationStateSchema:
    state: str
    data: dict

    def __init__(self, state: str = None, data: dict = None):
        self.state = state
        self.data = data
