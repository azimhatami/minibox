PROJECT=minibox
VENV=$(HOME)/.virtualenvs/$(PROJECT)


venv:
	python3 -m venv $(VENV)


install:
	pip install -e .
	pip install -r requirements.txt
