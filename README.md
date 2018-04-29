goto-project
============
Easy and fast project switching in your shell!

This is a like `workon` for python, but more powerfull and not only for python.

[![Build Status](https://travis-ci.org/sivakov512/goto-project.svg?branch=master)](https://travis-ci.org/sivakov512/goto-project)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/goto-project/badge.svg?branch=master)](https://coveralls.io/github/sivakov512/goto-project?branch=master)
![Python versions](https://img.shields.io/badge/python-3.6-blue.svg)
[![PyPi](https://img.shields.io/badge/PyPi-0.1.1-yellow.svg)](https://pypi.python.org/pypi/goto-project)

Installation
------------
Install it in your user-space with

``` shell
pip3 install goto-project --user  # or pip if python3 is your default interpreter
```

You can install `zsh` completion with [antigen](https://github.com/zsh-users/antigen)

``` shell
antigen bundle sivakov512/goto-project completions/zsh
```
Now type `gt `, then press <TAB> and you will see all available projects.

If you have project names `awesome-project` you can type `gt aw`, press <TAB> and get `gt awesome-project`.

Configuration and usage
-----
Specify your project in `~/.goto-project.yaml` file.

``` yaml
goto-project:  # this is a project name
  path: ~/Devel/Projects/goto-project/  # path project
  instructions:  # any instructions to call when you switch project
    - source ~/Devel/Envs/py3_goto-project/bin/activate
  command: vim  # command to run when project opened
  clear_on_exit: false  # if specified as false then terminal output will not be cleared on project close
```

To list all available projects call

``` shell
gt
```

To open project call `gt` with project name as argument

``` shell
gt goto-project
```

To close project press `C-D`. When you close project all changes will be breaked. For example, `$PATH` will be restored if you extend it.

Usage example
-------
For example you have a project named `awesome-nuxt-blog` placed at `~/Projects/awesome-nuxt-blog`.
You need to extend your `$PATH` with `.mode_modules/.bin`, source `.env/bin/activate` and show git status when project opened.

Create `~/.goto-project.yaml` with this content:
``` yaml
awesome-nuxt-blog:
  path: ~/Projects/awesome-nuxt-blog
  instructions:
    - source .env/bin/activate
    - export PATH=".node_modules/.bin:$PATH"
    - git status
```

Now you at `~/`. Type `gt awesome-nuxt-blog`. Now you at `~/Projects/awesome-nuxt-blog`.

All your instructions are executed. Also you see `git status` output in your shell.

Type `C-D` and now you in `~/`.

Screencast
----------
...available [here](https://asciinema.org/a/149712)
