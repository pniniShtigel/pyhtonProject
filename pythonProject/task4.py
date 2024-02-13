import pandas as pd
from typing import List

class DataHandler:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def convert_date_format(self, date_columns: List = None):
        if date_columns is None:
            date_columns = ['Date']
        self.sales_data[date_columns] = pd.to_datetime(self.sales_data[date_columns], format='%Y-%m-%d')

    def categorize_prices(self):
        # Adjust the conditions and labels based on your specific criteria
        conditions = [self.sales_data['Price'] < 50,
                      (self.sales_data['Price'] >= 50) & (self.sales_data['Price'] < 100),
                      self.sales_data['Price'] >= 100]
        labels = ['Low Price', 'Medium Price', 'High Price']
        self.sales_data['PriceCategory'] = pd.cut(self.sales_data['Price'], bins=[0, 50, 100, float('inf')], labels=labels)

    def change_index(self):
        self.sales_data.set_index(['CustomerId', 'Price'], inplace=True)

    def split_and_concat(self):
        # Assuming you want to split at half, adjust the split point as needed
        split_point = len(self.sales_data) // 2
        df1, df2 = self.sales_data.iloc[:split_point], self.sales_data.iloc[split_point:]
        result_df = pd.concat([df1, df2], axis=0)

    def complex_data_transformation(self):
        transposed_df = self.sales_data.T

    def group_with_function(self, column_do, column_use, func):
        grouped_result = self.sales_data.groupby(column_do)[column_use].apply(func)

    def locate_specific_row(self, index):
        # Two ways to locate a specific row by index
        specific_row_1 = self.sales_data.loc[index]
        specific_row_2 = self.sales_data.iloc[index]

    def locate_specific_column(self, column_label):

        specific_column_label = self.sales_data[column_label]
        specific_column_index = self.sales_data.loc[:, column_label]

    def locate_specific_columns_and_rows(self, columns, rows_range):

        specific_data = self.sales_data.loc[rows_range, columns]

    def locate_specific_rows_and_columns(self, rows, columns_range):
        # Locate specific rows and range of columns
        specific_data = self.sales_data.iloc[rows, columns_range]

    def filter_by_mask(self, mask_list, is_by_index=False):
        if is_by_index:
            filtered_df = self.sales_data[self.sales_data.index.isin(mask_list)]
        else:
            filtered_df = self.sales_data[mask_list]

        return filtered_df
