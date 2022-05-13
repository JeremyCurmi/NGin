install:
	python3.10 -m pip install --upgrade pip && python3.10 -m pip install -r requirements.txt
format:
	python3.10 -m black .