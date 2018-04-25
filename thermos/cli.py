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
                    # print(BASE_DIR)
                    # if os.chdir(BASE_DIR+"/"+app_name):
                    # subprocess.Popen("git init")

                    os.chdir(BASE_DIR+"/"+app_name)
                    os.system('git init')
                    os.system("touch .gitignore")
                    os.system("touch README.md")

                    with open('.gitignore','w+') as gitignore:
                        gitignore.write('virtual/ \n *.pyc \n start.sh')
                        gitignore.close()

                    if not os.path.exists('tests'):
                        os.makedirs('tests')

                    config_file = 'class Config:\n\tpass \n class ProdConfig(Config):\n\tpass\
                    \nclass DevConfig(Config): \n\tDEBUG = True\n\n\
                    config_options={"production":ProdConfig,"default":DevConfig}'

                    manage_file = "from flask_script import Manager,Server\n\
                    from app import create_app,db\n\n\
                    app = create_app('default')\n\n\
                    manager = Manager(app)\n\n\
                    manager.add_command('server', Server)\n\n\
                    if __name__ == '__main__':\n\
                    \tmanager.run()'\
                    "

                    with open('config.py','w+') as config:
                        config.write(config_file)
                        config.close()


                    with open('manage.py','w+') as manage:
                        manage.write(manage_file)
                        manage.close()


                    if not os.path.exists('app'):
                        os.makedirs('app')

                    os.chdir('app')

                    folders = ['static','templates','static/css','static/js','static/images']

                    for folder in folders:
                        if not os.path.exists(folder):
                            os.makedirs(folder)

                    init_file =  "from flask import Flask\nfrom config import config_options\nfrom flask_bootstrap import Bootstrap\nfrom flask_sqlalchemy import SQLAlchemy\n\n\nbootstrap = Bootstrap()\ndb = SQLAlchemy()\ndef create_app(config_state):\n\tapp = Flask(__name__)\n\tapp.config.from_object(config_options[config_state])\n\n\n\tbootstrap.init_app(app)\n\tdb.init_app(app)\n\tfrom .main import main as main_blueprint\n\tapp.register_blueprint(main_blueprint)\n\treturn app"

                    with open('__init__.py','w+') as init:
                        init.write(init_file)
                        init.close()

                    with open('models.py','w+') as models:
                        models.write("#models")
                        models.close()

                    if not os.path.exists('main'):
                        os.makedirs('main')

                    os.chdir('main')

                    main_init_file = "from flask import Blueprint\nmain = Blueprint('main',__name__)\n\nfrom . import views,error"
                    view_file="from . import main\n\n@main.route('/')\ndef index():\n\treturn '<h1> Hello World </h1>'"
                    error_file="from flask import render_template\nfrom . import main\n\n@main.app_errorhandler(404)\ndef for_Ow_four(error):\n\t'''\n\tFunction to render the 404 error page\n\t'''\n\treturn render_template('fourOwfour.html'),404"

                    blueprint_files = ['__init__.py' ,'views.py' ,'error.py']

                    for blueprint_file in blueprint_files:
                        if blueprint_file == '__init__.py':
                            with open(blueprint_file,'w+') as m_init:
                                m_init.write(main_init_file)
                                m_init.close()

                        elif blueprint_file == 'views.py':
                            with open(blueprint_file,'w+') as vw:
                                vw.write(view_file)
                                vw.close()

                        else:
                            with open(blueprint_file,'w+') as er:
                                er.write(error_file)
                                er.close()


                    os.chdir('..')
                    os.chdir('..')

                    with open('tests/__init__.py','a') as test_init:
                        test_init.close()

                    with open('start.sh','w+') as start:
                        start.write('python3.6 manage.py server')
                        start.close()

                    os.system('chmod a+x start.sh')



                    print(os.getcwd())














                    # else:
                    #     print("enter")
                # if not os.path.exists(app_name):
                #     path = os.makedirs(app_name)
                #     if os.chdir(os.path.dirname(os.getcwd())):
                #         print(os.chdir(app_name))
