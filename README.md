![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/pep8-checker.svg?branch=master)](https://travis-ci.org/vyahello/pep8-checker)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/pep8-checker/badge.svg?branch=master)](https://coveralls.io/github/vyahello/pep8-checker?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with interrogate](https://img.shields.io/badge/interrogate-checked-yellowgreen)](https://interrogate.readthedocs.io/en/latest/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![Downloads](https://pepy.tech/badge/pypans)](https://pepy.tech/project/pep8-checker)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pep8-checker.svg)](https://pypi.python.org/pypi/pep8-checker/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pep8-checker.svg)](https://pypi.python.org/pypi/pep8-checker/)
[![CodeFactor](https://www.codefactor.io/repository/github/Volodymyr Yahello/pep8-checker/badge)](https://www.codefactor.io/repository/github/Volodymyr Yahello/pep8-checker)

# pep8-checker

> A brief description for **pep8-checker** tool.

## Tools

- python 3.6 | 3.7 | 3.8
- [travis](https://travis-ci.org/) CI
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)
  - [pydocstyle](https://github.com/PyCQA/pydocstyle)

## Usage

![Usage](usage.gif)

### Quick start

```bash
pip install pep8-checker
✨ 🍰 ✨
```

After please run **pep8-checker** tool from your shell:
```bash
pep8-checker
```

### Source code

```bash
git clone path/to/github/repo.git
pip install -e .
pep8-checker
```

Or using direct release:
```bash
pip install git+https://path/to/github/repo@0.0.1
pep8-checker
```

### Local debug

```bash
git clone path/to/github/repo.git
python -m pep8-checker
```
**[⬆ back to top](#pep8-checker)**

## Development notes

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle` and `interrogate`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```
### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/Volodymyr Yahello](https://github.com/Volodymyr Yahello)
* [https://www.linkedin.com/in/Volodymyr Yahello](https://www.linkedin.com/in/Volodymyr Yahello)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/Volodymyr Yahello/pep8-checker/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pep8-checker)**
