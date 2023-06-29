from poe import Client

class Handler:
    def __init__(self, client: Client) -> None:
        self.client = client

    def handle(self):
        raise NotImplementedError
