from poe import Client


class Handler:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.print_handler_description()

    def handle(self):
        raise NotImplementedError

    def print_handler_description(self):
        raise NotImplementedError
