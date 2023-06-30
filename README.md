Welcome to Shell POE

This app provides a shell and CLI assistance using PoeClient API.

Usage:

API key can be found from poe website's cookies.

`poe_shell --help`
for help on options

Options:
`--shell, -s`
Generates and executes shell commands.

`--chat, -c`
Chats with the bot.

`--bots`
Returns a list of available bots.

If no options are provided, it will respond to one-off messages.

It handles the following types of requests:

- Shell requests (using ShellHandler)
- Chat requests (using ChatHandler)
- One-off messages (using OneOffHandler)
- Listing available bots

The PoeClient API client is initialized and passed to the relevant handler based on the requests.


This project use poetry to manage dependencies. https://python-poetry.org/docs/
