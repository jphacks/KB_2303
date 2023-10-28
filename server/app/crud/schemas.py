class AdminSessionSchema:
    admin_id: int

    def __init__(self, admin_id: int = None):
        self.admin_id = admin_id


class LINECommunicationStateSchema:
    state: str

    def __init__(self, state: str = None):
        self.state = state
