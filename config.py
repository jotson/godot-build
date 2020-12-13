# Full path to the Godot executable
GODOT = '/path/to/godot'

# Full path to the Godot project directory you want to build
PROJECT = '/path/to/game/directory'

# Full path where executables should be build
BUILDDIR = '/path/to/build_directory'

# Godot options for build process
OPTIONS = ['--no-window', '--resolution', '640x360'] # --no-window doesn't work on linux
EXPORT = '--export' # Use --export-debug for a debug release

# Full path to steamcmd and the build vdf file (see https://partner.steamgames.com/doc/sdk/uploading)
STEAM_COMMAND = '/path/to/steamcmd.sh'
STEAM_APP_CONFIG = '/path/to/app.vdf'

# Your itch.io project and full path to butler (see https://itch.io/docs/butler/)
ITCH_PROJECT = 'username/game'
BUTLER = '/path/to/butler'

# Version cfg file for your game (see https://docs.godotengine.org/en/stable/classes/class_configfile.html)
VERSION_FILE = '/path/to/version.cfg'

# Changelog location
CHANGELOG = '/tmp/changelog.md'