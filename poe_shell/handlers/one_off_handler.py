from .handler import Handler


class OneOffHandler(Handler):
    chat_bot = "descshellbot"

    def handle(self, message: str):
        for chunk in self.client.send_message(
            self.chat_bot, message, with_chat_break=True
        ):
            print(chunk["text_new"], end="", flush=True)
        print("\n")

    def print_handler_description(self):
        pass
