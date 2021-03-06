
all: dependencies run

dependencies:
	python3 -m pip install mysql-connector-python-rf
	python3 -m pip install openpyxl
	python3 -m pip install pyqt5
	python3 -m pip install pandas
	python3 -m pip install pypika
	python3 -m pip install pdfkit
	python3 -m pip install wkhtmltopdf
	python3 -m pip install matplotlib
	python3 -m pip install numpy

run:
	python3 src/app.py
