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
    print("Connecting to POE...")
    client = PoeClient().client

    stdin_passed = not sys.stdin.isatty()

    if shell:
        print("Initializing shell gpt mode...")
        from handlers.shell_handler import ShellHandler
        print("Creating connection to POE...")
        handler = ShellHandler(client)
        print("Connected to POE.\n")
        handler.handle()

    elif bots:
        list = client.bot_names
        print(list)

    elif chat:
        print("Initializing chat gpt mode...")
        from handlers.chat_handler import ChatHandler
        print("Creating connection to POE...")
        handler = ChatHandler(client)
        print("Connected to POE.\n")
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
