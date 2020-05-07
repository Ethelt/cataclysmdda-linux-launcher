# Simple Linux launcher for Cataclysm: Dark Days Ahead

This scirpt checks if there is a new release of C:DDA on Github, backs up your saves in backups/ directory and then installs new version.
It doesn't preserve any modifications to game files while doing so.

### Installation:
Just download the files, give necessary permissions to launcher file and run it. All the files will be stored in the directory of the launcher. All the dependencies should come preinstalled with most distributions, or are dependencies of the game itself.

### Configuration
For now there is only one option in config file - number of backups to keep. When the number of backups exceeds this number, the oldest backup will be deleted.

### F.A.Q.
##### How to stay on the same version despite new updates?
There is no pretty solution for the time being, you can just increase the number in current_version file to some big number and then return it back to normal when you'll want to get the newest version again. It's important that you just change the number and not add anything to the file, because it will cause the launcher to crash.
