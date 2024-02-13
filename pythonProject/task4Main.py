import pandas as pd
from task4 import DataHandler

def main():

    data = {
        'CustomerId': [1, 2, 3, 4, 5],
        'Price': [30, 70, 120, 40, 90],
        'Date': ['03-01-2022', '01-02-2022', '01-01-2024', '01-03-2022', '01-01-2022']
    }
    sales_data = pd.DataFrame(data)


    data_handler = DataHandler(sales_data)


    data_handler.convert_date_format()

    data_handler.categorize_prices()

    data_handler.change_index()

    data_handler.split_and_concat()

    data_handler.complex_data_transformation()

    data_handler.group_with_function(column_do='CustomerId', column_use='Price', func='sum')

    data_handler.locate_specific_row(index=2)

    data_handler.locate_specific_column(column_label='Price')

    data_handler.locate_specific_columns_and_rows(columns=['CustomerId', 'Price'], rows_range=range(2, 5))

    data_handler.locate_specific_rows_and_columns(rows=range(1, 4), columns_range=range(0, 2))

    mask_list = [True, False, True, False, True]
    filtered_data = data_handler.filter_by_mask(mask_list)

    print("Filtered Data:")
    print(filtered_data)

if __name__ == "__main__":
    main()
