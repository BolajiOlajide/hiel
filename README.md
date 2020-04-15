# Hiel

A command line utility used to bootstrap projects without having to repeat the same processes over and over again.

## Installation

To install `hiel` on your machine simply pull it from the internet (lol) using Pypi.

```sh
pip install --user hiel
```

### Note

Hiel is somewhat customized for my local machine, so to make use of it ensure you have the following on your PC.

* [Setup SSH for Github](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

* [Yarn](https://yarnpkg.com/) package manager is installed on your PC

* You have at least [Python3.6](https://www.python.org/downloads/release/python-360/) installed on your PC

* [Git](https://git-scm.com/) installed on your PC

Once this is done, get a personal access token from [Github](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to ensure bootstrapped projects can be pushed to version control (Github). The access token is stored in `$HOME/.hiel` and can be updated anytime.
You don't need to create this file as it'd be created automatically when you run `HIEL` for the first time.

<!-- markdownlint-disable MD033 -->
<div align="center">
  <img src="https://github.com/BolajiOlajide/hiel/blob/master/token.png?raw=true" alt="github token" />
</div>

#### Commands

* To view the help command

```sh
hiel --help
```

* Bootstrap a project

```sh
hiel <PROJECT_NAME> --type=[js|py] # type is used to specify the type of project, if its python/js
```

* To view the version of Hiel being used

```sh
hiel --version
```
