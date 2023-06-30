from .handler import Handler


class ChatHandler(Handler):
    chat_bot = "chinchilla"

    def handle(self, message: str | None):
        if message:
            self.send_message(message.strip())

        print("Enter message or 'd' to exit.")

        while True:
            message = input(">>> ").strip()

            if message in ["d", "exit"]:
                break
            elif message:
                self.send_message(message)
            else:
                continue

        if message:
            self.client.send_chat_break(self.chat_bot)

    def send_message(self, message: str):
        response = ""

        for chunk in self.client.send_message(self.chat_bot, message):
            text_new = chunk["text_new"]
            print(text_new, end="", flush=True)
            response += text_new
        print("\n")

        return response

    def print_handler_description(self):
        print("---Chat Mode---")
