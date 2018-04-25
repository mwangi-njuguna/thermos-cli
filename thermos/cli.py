"""
thermos

Usage:
  thermos create app <appname>
  thermos create
  thermos -h | --help
  thermos -v | --version

Options:
  -h --help                         Show this screen for available options.
  -v --version                         Show the version.
Examples:
  thermos create <app-name>
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/mwangi-njuguna/thermos-cli
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

import subprocess


def main():
    """The main CLI entry-point."""

    import thermos.commands
    import os

    options = docopt(__doc__, version=VERSION)

    # for (k, v) in options.items():
    #     if hasattr(thermos.commands, k) and v:
    #         module = getattr(thermos.commands, k)
    #         thermos.commands = getmembers(module, isclass)
    #         command = [command[1] for command in thermos.commands if command[0] != 'Base'][0]
    #         command = command(options)
    #         command.run()

    if options['create']:
        if options['app']:
            app_name = options['<appname>']
            if app_name:
                if not os.path.exists(app_name):
                    path = os.makedirs(app_name)
                else:
                    BASE_DIR = os.path.join( os.path.dirname(os.path.dirname( __file__ )))
                    print(BASE_DIR)
                    # if os.chdir(BASE_DIR+"/"+app_name):
                    # subprocess.Popen("git init")

                    os.chdir(BASE_DIR+"/"+app_name)
                    os.system('git init')
                    os.system("touch .gitignore")
                    os.system("touch README.md")



                    with open('.gitignore','w+') as gitignore:
                        gitignore.write('virtual/ \n *.pyc \nstart.sh')
                        gitignore.close()

                    print(os.getcwd())
                    # else:
                    #     print("enter")
                # if not os.path.exists(app_name):
                #     path = os.makedirs(app_name)
                #     if os.chdir(os.path.dirname(os.getcwd())):
                #         print(os.chdir(app_name))
