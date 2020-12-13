# Build system for Gravity Ace, a Godot Engine game

I shared this with the thought that it might be useful to you. It may not work for your game and I made no effort to make it cross platform. That said, it's Python... results may vary.

Please do not send pull requests. Take it and go in peace.

# Setup

Pushing to itch.io requires configuring butler: https://itch.io/docs/butler/

Pushing to Steam requires configuring the Steam SDK: https://partner.steamgames.com/doc/sdk/uploading

For Steam you'll also need to create a file `BUILDDIR/.steam` where the first line is your Steam username and the second line is your Steam password.

- Start with `config.py` and plug in your paths
- Run `build` to build (builds and creates changelog)
- Run `push` to upload to itch and steam
- Run `list-changes` to print a changelog
- Add `post-commit` to your git hooks to post commits to Discord

Discord integration works via webhooks. Create a webhook URL for your channel and place in `BUILDDIR/.discord-git`. That webhook is used for the `post-commit` git hook. Create another webhook URL and place in `BUILDDIR/.discord-announce`. That webhook is used for posting changelogs from `push`.

The `post-commit` script will ignore commits containing `#private`.

# Buy Gravity Ace

[Gravity Ace is available on Steam and Itch.io!](https://gravityace.com/)
