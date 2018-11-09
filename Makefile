
all: dependencies run

dependencies:
	python3 -m pip install mysql-connector-python-rf
	python3 -m pip install openpyxl
	python3 -m pip install pyqt5
	python3 -m pip install pandas

run:
	python3 src/app.py
