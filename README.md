![Screenshot](media/logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with interrogate](https://img.shields.io/badge/interrogate-checked-yellowgreen)](https://interrogate.readthedocs.io/en/latest/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Build Status](https://travis-ci.org/vyahello/pep8-checker.svg?branch=master)](https://travis-ci.org/vyahello/pep8-checker)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/pep8-checker/badge.svg?branch=master)](https://coveralls.io/github/vyahello/pep8-checker?branch=master)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/pep8-checker/badge)](https://www.codefactor.io/repository/github/vyahello/pep8-checker)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/pep8-checker.svg)](https://hub.docker.com/repository/docker/vyahello/pep8-checker)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fpep8-checker.herokuapp.com)](https://pep8-checker.herokuapp.com)
[![Docs](https://img.shields.io/badge/docs-github-orange)](https://vyahello.github.io/pep8-checker)

# PEP8 checker

> This project allows to check your python code complies with pep8 conventions.
> 
> It uses **bottle** python micro web framework and **AWS lambda** function to execute code on the server.

## Tools

### Production

- python 3.6, 3.7, 3.8
- [bottle](https://bottlepy.org/docs/dev/tutorial.html)
- [AWS lambda](https://aws.amazon.com/)
- [travis](https://travis-ci.org/) CI

### Development

- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)

## Usage
![Usage](media/demo.gif)

### Quick start
Please check an app at https://pep8-checker.herokuapp.com.

Or launch it via dedicated docker image:
```bash
docker run --rm -it vyahello/pep8-checker:0.0.2
```
> Please follow the help instructions further.

### Source code
```bash
git clone git@github.com:vyahello/pep8-checker.git
python -m checker
```
> **Note**: _please make sure **AWS_ENDPOINT** environment variable is configured preliminary._
```bash
export AWS_ENDPOINT=https://...amazonaws.com/v1
```

**[⬆ back to top](#pep8-checker)**

## Development notes

### Docker 

#### Base image
Please use the following command sample to build base docker image:
```bash
docker build --no-cache \
         --tag vyahello/pep8-checker:{version} \ 
         --file Dockerfile.base .
```

#### Main image
Please use the following command sample to build main docker image:
```bash
docker build --no-cache \
         --tag vyahello/pep8-checker:{version} \ 
         --build-arg VERSION={version} \
         --build-arg REPOSITORY=vyahello/pep8-checker \
         --build-arg AWS_ENDPOINT={endpoint} .
```

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
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127/](https://www.linkedin.com/in/volodymyr-yahello-821746127/)

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

All recent activities and ideas are described at project [issues](https://github.com/vyahello/pep8-checker/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pep8-checker)**
