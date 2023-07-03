import typer
import sys
import os

from .config import STORAGE_PATH
from .poe_client import PoeClient

app = typer.Typer()


@app.command()
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
    chat: bool = typer.Option(
        False,
        "--chat",
        "-c",
        help="Chat with the bot.",
        rich_help_panel="Assistance Options",
    ),
    bots: bool = typer.Option(
        False,
        "--bots",
        help="Return the list of bots.",
        rich_help_panel="Assistance Options",
    ),
    remove_api_key: bool = typer.Option(
        False,
        "--remove-api-key",
        help="Remove the saved API key.",
        rich_help_panel="Assistance Options",
    ),
):
    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH)

    if remove_api_key:
        PoeClient().remove_api_key()
        return

    client = PoeClient().connect()

    stdin_passed = not sys.stdin.isatty()

    if shell:
        from .handlers.shell_handler import ShellHandler

        handler = ShellHandler(client)
        handler.handle(message)

    elif bots:
        list = client.bot_names
        print(list)

    elif chat:
        from .handlers.chat_handler import ChatHandler

        handler = ChatHandler(client)
        handler.handle(message)

    elif message:
        from .handlers.one_off_handler import OneOffHandler

        if stdin_passed:
            message = f"{sys.stdin.read()}\n\n{message or ''}"

        OneOffHandler(client).handle(message)

    else:
        typer.echo("Use --help for more information.")


def cli():
    app()


if __name__ == "__main__":
    app()
