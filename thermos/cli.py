"""

thermos



Usage:
  
  thermos create template <templatename>


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

    import os,pip



    options = docopt(__doc__, version=VERSION)



    # for (k, v) in options.items():

    #     if hasattr(thermos.commands, k) and v:

    #         module = getattr(thermos.commands, k)

    #         thermos.commands = getmembers(module, isclass)

    #         command = [command[1] for command in thermos.commands if command[0] != 'Base'][0]

    #         command = command(options)

    #         command.run()



    if options['create']:

        if options['template']:

            template_name = options['<templatename>']

            if template_name:

                if not os.path.exists(template_name):

                    path = os.makedirs(template_name)

                else:

                   