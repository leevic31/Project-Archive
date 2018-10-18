
all: dependencies run

dependencies:
	python3 -m pip install openpyxl
	python3 -m pip install PyMySQL

run:
	python3 src/app.py
