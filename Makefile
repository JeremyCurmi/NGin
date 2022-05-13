install:
	python3.10 -m pip install --upgrade pip && python3.10 -m pip install -r requirements.txt

format:
	python3.10 -m black .

lint:
	pylint --disable=R,C ./src

test:
	python -m pytest -vv --cov=tests/ tests/.