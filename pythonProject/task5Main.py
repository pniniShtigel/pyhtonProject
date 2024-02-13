import pandas as pd
from task4 import DataHandler

def main():

    data = {
        "Date": ["2023-01-01", "2023-01-03", "2023-02-01", "2023-02-02", "2023-02-03", "2023-03-01"],
        "CustomerId": [1, 2, 3, 4, 5, 6],
        "Price": [50, 80, 120, 30, 90, 110],

    }


    data_handler = DataHandler(pd.DataFrame(data))


    data_handler.convert_date_format()
    data_handler.categorize_prices()
    data_handler.change_index()
    data_handler.split_and_concat()
    data_handler.complex_data_transformation()
    data_handler.group_with_function(column_do='column1', column_use='column2', func=lambda x: x.sum())
    data_handler.locate_specific_row(index=0)
    data_handler.locate_specific_column(column_label='Price')
    data_handler.locate_specific_columns_and_rows(columns=['Price', 'Date'], rows_range=slice(1, 4))
    data_handler.locate_specific_rows_and_columns(rows=slice(2, 5), columns_range=[0, 2])
    data_handler.filter_by_mask(mask_list=[True, False, True], is_by_index=False)


if __name__ == "__main__":
    main()
