import typer
import sys

from poe_client import PoeClient

def main(
        message: str = typer.Argument(
            None,
        ),
        shell: bool = typer.Option(
            False,
            "--shell",
            "-s",
            help="Generate and execute shell commands.",
            rich_help_panel="Assistance Options",
        ),
        bots: bool = typer.Option(
            False,
            "--bots",
            help="Return the list of bots.",
            rich_help_panel="Assistance Options",
        ),
    ):
    print("Connecting to POE...")
    client = PoeClient().client
    print("\r")

    stdin_passed = not sys.stdin.isatty()

    if message:
        from handlers.one_off_handler import OneOffHandler

        if stdin_passed:
            message = f"{sys.stdin.read()}\n\n{message or ''}"

        OneOffHandler(client).handle(message)
        return 0

    if shell:
        print("Initializing shell gpt mode...")
        from handlers.shell_handler import ShellHandler
        print("Creating connection to POE...")
        handler = ShellHandler(client)
        print("Connected to POE.")
        handler.handle()

    if bots:
        list = client.bot_names
        print(list)


if __name__ == "__main__":
    typer.run(main)
