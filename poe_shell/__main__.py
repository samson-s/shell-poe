import typer
import sys

from poe_client import PoeClient

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
):
    client = PoeClient().client

    stdin_passed = not sys.stdin.isatty()

    if shell:
        from handlers.shell_handler import ShellHandler

        handler = ShellHandler(client)
        handler.handle()

    elif bots:
        list = client.bot_names
        print(list)

    elif chat:
        from handlers.chat_handler import ChatHandler

        handler = ChatHandler(client)
        handler.handle(message)

    elif message:
        from handlers.one_off_handler import OneOffHandler

        if stdin_passed:
            message = f"{sys.stdin.read()}\n\n{message or ''}"

        OneOffHandler(client).handle(message)

    else:
        typer.echo("Use --help for more information.")


if __name__ == "__main__":
    app()
