VENV_PATH = .venv

.PHONY: clean
clean:
	@find . -name '*.py?' -delete
	@find . -name '.cache' -type d | xargs rm -rf
	@find . -name '.pytest_cache' -type d | xargs rm -rf
	@find . -name '__pycache__' -type d | xargs rm -rf
	@find . -name 'test-results' -type d | xargs rm -rf
	@rm -rf $(VENV_PATH)

.PHONY: venv
venv:
	@test -d $(VENV_PATH) || python3 -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate; pip install --upgrade pip pip-tools
	. $(VENV_PATH)/bin/activate; make compile-requirements
	. $(VENV_PATH)/bin/activate; pip-sync requirements.txt

.PHONY: compile-requirements
compile-requirements:
	pip-compile --no-emit-index-url --upgrade requirements.in

.PHONY: test
test:
	. $(VENV_PATH)/bin/activate; python -m pytest

.PHONY: download-input
download-input:
	./download-input.sh $(day)

.PHONY: lint
lint:
	. $(VENV_PATH)/bin/activate; python -m ruff src