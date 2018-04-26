## Note

A flask command line interface built on python 

If you wish to collaborate,visit https://github.com/mwangi-njuguna/thermos-cli.


## Prerequisites

Both the CLI and generated project have dependencies that require python3.6.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Generating a New Project](#generating-and-serving-an-angular-project-via-a-development-server)
* [Generating Components, Directives, Pipes and Services](#generating-components-directives-pipes-and-services)
* [Updating Angular CLI](#updating-angular-cli)
* [Development Hints for working on Angular CLI](#development-hints-for-working-on-angular-cli)
* [Documentation](#documentation)
* [License](#license)

## Installation

**BEFORE YOU INSTALL:** please make sure you have python3.6 installed.


```bash
pip install -e .
```

## Usage

```bash
thermos --help
```

### Generating a flask project 

```bash
thermos create PROJECT-NAME
```
Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

You can configure the default HTTP host and port used by the development server with two command-line options :


### Generating templates and blueprints

You can use the `thermos create app APPNAME` to create a new application structure:

```bash
thermos create template TEMPLATENAME

# Navigate into the new app
cd NAMEOFAPP

# if in the directory src/app/nameofapp/ and you run
thermos create blueprint BLUEPRINTNAME

# your blueprint will be created in src/app/nameofapp/newblueprint
# but if you were to run
ng g component ./newer-cmp
# your component will be generated in src/app/newer-cmp
# if in the directory src/app you can also run
ng g component feature/new-cmp
# and your component will be generated in src/app/feature/new-cmp
```

If you are updating to 1.0 from a beta or RC version, check out our [1.0 Update Guide](https://github.com/angular/angular-cli/wiki/stories-1.0-update).

You can find more details about changes between versions in [the Releases tab on GitHub](https://github.com/angular/angular-cli/releases).


## Development Hints for working on Angular CLI

### Working with master

```bash
git clone https://github.com/mwangi-njuguna/thermos-cli.
cd thermos-cli
pip install -e .
```

`pip install -e .` will install this cli.

Now you can use `thermos-cli` via the command line:

```bash

  thermos create

  thermos -h | --help

  thermos -v | --version

```

Please read the official [npm-link documentation](https://docs.npmjs.com/cli/link)
and the [npm-link cheatsheet](http://browsenpm.org/help#linkinganynpmpackagelocally) for more information.

To run the Angular CLI test suite use the `node tests/run_e2e.js` command.
It can also receive a filename to only run that test (e.g. `node tests/run_e2e.js tests/e2e/tests/build/dev-build.ts`).




## Documentation

The documentation for the Angular CLI is located in this repo's [wiki](https://github.com/gnhkjm/).

## License

MIT
