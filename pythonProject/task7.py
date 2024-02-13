import sys
import random
from datetime import datetime
import csv
from xml.dom.minidom import Document

import pandas as pd


class TaskHandler:

    def handle_error(self, error_type, value, name):
        try:
            raise error_type(f"{value} is invalid for {name}")
        except error_type as e:
            current_time = datetime.now().strftime("%d.%m.%y, %H:%M")
            error_message = f"<Your_Name, {current_time}> {e} <Your_Name>"
            print(error_message)

    def read_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)

    def read_word(self, file_path):
        document = Document(file_path)
        for paragraph in document.paragraphs:
            print(paragraph.text)

    def random_sales_and_highest_payment(self, product_name):
        random_sales = random.randint(1, 100)
        highest_payment = random.uniform(10, 1000)
        return random_sales, highest_payment

    def print_python_version(self):
        print(f"Python Version: {sys.version}")

    def process_parameters(self, *args, **kwargs):
        result = {}
        for arg in args:
            if isinstance(arg, int):
                print(arg)
            elif isinstance(arg, str) and "VALUE NAME" in kwargs and arg == kwargs["VALUE NAME"]:
                result[arg] = arg
        return result

    def print_table(self, df):
        print(df)

        print("First 3 rows:")
        print(df.head(3))

        print("Last 2 rows:")
        print(df.tail(2))

        print("Random row:")
        print(df.sample())

    def iterate_over_table(self, df):
        for column in df.columns:
            print(f"Column: {column}")
            for value in df[column]:
                print(value)

task_handler = TaskHandler()

task_handler.handle_error(TypeError, "value", "parameter_name")

task_handler.read_csv('example.csv')
task_handler.read_word('example.docx')

product_name = "Example Product"
sales, highest_payment = task_handler.random_sales_and_highest_payment(product_name)
print(f"For {product_name}, random sales: {sales}, highest payment: {highest_payment}")

task_handler.print_python_version()

task_handler.process_parameters(5, "text", "example", VALUE_NAME="example")

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 75000]}
df = pd.DataFrame(data)


task_handler.print_table(df)

task_handler.iterate_over_table(df)
