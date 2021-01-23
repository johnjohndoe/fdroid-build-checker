![GitHub Actions tests](https://github.com/johnjohndoe/fdroid-build-checker/workflows/Test/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/) [![AGPL 3.0](https://img.shields.io/badge/license-AGPL%203.0-blueviolet.svg)](https://www.gnu.org/licenses/agpl-3.0.html)



# fdroid-build-checker

Python code to check if [F-Droid][fdroid] recent build has succeeded or failed.

![Logo](gfx/logo.png)

## Description

The scripts check if your custom packages occur on the [recent changes][recent-changes] page and then inspect the
associated last build pages for the build result.

## Setup

```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Install

```sh
$ pip3 install --user git+https://github.com/johnjohndoe/fdroid-build-checker.git
```


## Usage

```sh
$ python3 ~/.local/lib/python3.8/site-packages/fdroid_build_checker/
```

See [`fdroid_build_checker/__main__.py`](fdroid_build_checker/__main__.py)

## Tests

Execute the following command to run all tests:

```sh
pipenv run python -m pytest
```

## Dependencies

See [Pipfile](Pipfile)

## License

```
Copyright (C) 2021  Tobias Preuss

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## Credits

This package was created with Cookiecutter and
the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter)
project template.


[fdroid]: https://f-droid.org
[recent-changes]: https://f-droid.org/wiki/index.php?title=Special:RecentChanges&days=30&from=&hidebots=0&hideanons=1&hideliu=1&limit=500
