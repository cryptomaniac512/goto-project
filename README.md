goto-project
============
Easy and fast project switching in your shell!

[![Build Status](https://travis-ci.org/cryptomaniac512/goto-project.svg?branch=master)](https://travis-ci.org/cryptomaniac512/goto-project)
[![Coverage Status](https://coveralls.io/repos/github/cryptomaniac512/goto-project/badge.svg?branch=master)](https://coveralls.io/github/cryptomaniac512/goto-project?branch=master)
![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)
[![PyPi](https://img.shields.io/badge/PyPi-0.0.2-yellow.svg)](https://pypi.python.org/pypi/goto-project)

Installation
------------
You can install it in your user-space with

``` shell
pip3 install goto-project --user  # or pip if python3 is your default interpreter
```

Usage
-----
Specify your project in `~/.goto-project.yaml` file.

``` yaml
goto-project:  # this is a project name
  path: ~/Devel/Projects/goto-project/  # path project
  instructions:  # any instructions to call when you switch project
    - source ~/Devel/Envs/py3_goto-project/bin/activate
  command: vim  # command to run when project opened
  clear_on_exit: true  # if specified then terminal output will be cleared on project close
```

To list all available projects call

``` shell
gt
```

To open project call `gt` with project name as ergument

``` shell
gt goto-project
```

To close project press `C-D`. When you close project all changes will be breaked. For example, `$PATH` will be restored if you extend it.

Simple screencast available [here](https://asciinema.org/a/149712)
