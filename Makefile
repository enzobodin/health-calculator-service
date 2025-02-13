.PHONY: init run test build

init:
	pip install -r requirements.txt

run:
	uvicorn app:app --reload --host 0.0.0.0 --port 5001

test:
	uvicorn app:app --host 0.0.0.0 --port 5001 &
	sleep 5
	pytest -v test.py
	kill $$(lsof -t -i:5001)

build:
	docker build -t health-calculator .