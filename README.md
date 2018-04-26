## Thermos CLI

A flask command line interface built on python. 

## Note

If you wish to collaborate,visit https://github.com/mwangi-njuguna/thermos-cli.


## Prerequisites

Both the CLI and generated project have dependencies that require python3.6.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Generating a New Flask Application](#Generating a new flask project)
* [Generating Templates and Blueprints](#Generating templates and blueprints)
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

### Generating a Flask Project 

```bash
thermos create PROJECT-NAME
```

### Generating Templates and Blueprints

You can use the `thermos create app APPNAME` to create a new application structure:

```bash
thermos create template TEMPLATENAME

# Navigate into the new app
cd NAMEOFAPP

# if in the directory src/app/nameofapp/ and you run
thermos create blueprint BLUEPRINTNAME

```

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

## Documentation

The documentation for the thermos CLI is located in this repo's [Doc](https://github.com/mwangi-njuguna/thermos-cli/blob/thuita/DOC.md).

## License

MIT
