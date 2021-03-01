.DEFAULT_GOAL := default_target

PROJECT_NAME := personal-finance
PYTHON_VERSION := 3.9.1
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

setup-dev:
	pip install pip --upgrade
	pip install -U setuptools wheel
	pip install -e .[dev]


.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev 
