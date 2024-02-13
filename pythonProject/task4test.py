import pandas as pd

from task4 import DataHandler

# Sample DataFrame
data = {'Date': ['2022-01-01', '2022-02-01', '2022-03-01'],
        'CustomerId': [1, 2, 3],
        'Price': [50, 75, 100],
        'Quantity': [10, 15, 20]}
sales_data = pd.DataFrame(data)

data_handler = DataHandler(sales_data)
data_handler.convert_date_format(date_columns=['Date'])

data_handler = DataHandler(sales_data)
data_handler.categorize_prices()

data_handler = DataHandler(sales_data)
data_handler.change_index()

data_handler = DataHandler(sales_data)
data_handler.split_and_concat()

data_handler = DataHandler(sales_data)
data_handler.complex_data_transformation()

data_handler = DataHandler(sales_data)
data_handler.group_with_function(column_do='CustomerId', column_use='Quantity', func='sum')

data_handler = DataHandler(sales_data)
data_handler.locate_specific_row(index=1)

data_handler = DataHandler(sales_data)
data_handler.locate_specific_column(column_label='Price')

data_handler = DataHandler(sales_data)
data_handler.locate_specific_columns_and_rows(columns=['Price', 'Quantity'], rows_range=slice(0, 2))

data_handler = DataHandler(sales_data)
data_handler.locate_specific_rows_and_columns(rows=slice(0, 2), columns_range=[0, 2])

data_handler = DataHandler(sales_data)
mask_list = [True, False, True]
filtered_df = data_handler.filter_by_mask(mask_list, is_by_index=False)
