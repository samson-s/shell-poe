from utils import run_command
from .handler import Handler
from roles import SHELL_ROLE


class ShellHandler(Handler):
    chat_bot = "shellbotsss"

    def handle(self):
        command = ""

        print("Enter command description \nor 'd' to exit \nor 'c' to custom command mode.")
        while True:
            prompt = input(">>> ").strip()

            if prompt in ['d', 'exit']:
                break
            elif prompt in ['e']:
                run_command(command)
            elif prompt in ['c']:
                self.custom_command_mode()
            elif prompt:
                command = self.send_message(prompt)
                print("Enter command description or 'e' to enter.")
            else:
                continue

        # Use command to check if interacted with gpt
        # Remove context if interacted
        if command:
            self.client.send_chat_break(self.chat_bot)
    
    def send_message(self, message: str)->str:
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
            if command in ['d', 'exit']:
                print("Exiting custom command mode.")
                break
            elif command:
                run_command(command)
            else:
                continue
