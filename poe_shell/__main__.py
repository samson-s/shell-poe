import typer
import sys
import os
from rich.table import Table
from rich.console import Console

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
    ),
    bot: str = typer.Option(
        None,
        "--bot",
        "-b",
        help="Specify the bot to chat with.",
        rich_help_panel="Assistance Options",
    ),
):
    console = Console()

    if not os.path.exists(STORAGE_PATH):
        os.makedirs(STORAGE_PATH)

    if remove_api_key:
        PoeClient().remove_api_key()
        return

    client = PoeClient().connect()

    if bots:
        bot_names = client.bot_names
        table = Table("Tag", "Bot Name")
        for tag in bot_names:
            table.add_row(tag, bot_names[tag])
        console.print(table)
        return

    if shell:
        from .handlers.shell_handler import ShellHandler as Handler
    elif chat:
        from .handlers.chat_handler import ChatHandler as Handler
    elif message:
        from .handlers.one_off_handler import OneOffHandler as Handler
    else:
        typer.echo("Use --help for more information.")
        return

    hander = Handler(client, bot)

    stdin_passed = not sys.stdin.isatty()
    if stdin_passed:
        message = f"{sys.stdin.read()}\n\n{message or ''}"

    hander.handle(message)


def cli():
    app()


if __name__ == "__main__":
    app()
