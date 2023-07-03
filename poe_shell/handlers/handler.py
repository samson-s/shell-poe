from poe import Client


class Handler:
    chat_bot = None

    def __init__(self, client: Client, chat_bot: str | None = None) -> None:
        if chat_bot:
            self.chat_bot = chat_bot

        self.client = client
        self.print_handler_description()

    def handle(self):
        raise NotImplementedError

    def print_handler_description(self):
        raise NotImplementedError
