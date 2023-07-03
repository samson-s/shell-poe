from ..utils import run_command
from .handler import Handler


class ShellHandler(Handler):
    chat_bot = "poeshellbot"

    def handle(self, message: str | None = None):
        print("Enter command description.")
        print("Enter 'd' to exit.")
        print("Enter 'e' to execute the command.")
        print("Enter 'c' to enter custom command mode.")

        if message:
            command = self.send_message(message.strip())
        else:
            command = ""

        while True:
            message = input(">>> ").strip()

            if message in ["d", "exit"]:
                break
            elif message in ["e"]:
                run_command(command)
            elif message in ["c"]:
                self.custom_command_mode()
            elif message:
                command = self.send_message(message)
                print("Enter command description or 'e' to enter.")
            else:
                continue

        # Use command to check if interacted with gpt
        # Remove context if interacted
        if command:
            self.client.send_chat_break(self.chat_bot)

    def send_message(self, message: str) -> str:
        response = ""

        for chunk in self.client.send_message(self.chat_bot, message):
            text_new = chunk["text_new"]
            print(text_new, end="", flush=True)
            response += text_new
        print("\n")

        return response

    def custom_command_mode(self):
        while True:
            command = input("Custom command: ").strip()
            if command in ["d", "exit"]:
                print("Exiting custom command mode.")
                break
            elif command:
                run_command(command)
            else:
                continue

    def print_handler_description(self):
        print("---Shell Mode---")
