import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataHandler:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def convert_date_format(self, date_columns: list = None):
        try:
            if date_columns is None:
                date_columns = ['Date']
            self.sales_data[date_columns] = pd.to_datetime(self.sales_data[date_columns])
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")

    def categorize_prices(self):
        try:
            conditions = [self.sales_data['Price'] < 50,
                          (self.sales_data['Price'] >= 50) & (self.sales_data['Price'] < 100),
                          self.sales_data['Price'] >= 100]
            labels = ['Low Price', 'Medium Price', 'High Price']
            self.sales_data['PriceCategory'] = pd.cut(self.sales_data['Price'], bins=[0, 50, 100, float('inf')], labels=labels)
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")

    def change_index(self):
        try:
            self.sales_data.set_index(['CustomerId', 'Price'], inplace=True)
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")

    def split_and_concat(self):
        try:
            split_point = len(self.sales_data) // 2
            df1, df2 = self.sales_data.iloc[:split_point], self.sales_data.iloc[split_point:]
            result_df = pd.concat([df1, df2], axis=0)
        except Exception as e:
            raise Exception(f"Error occurred during DataFrame split and concat: {e}")

    def complex_data_transformation(self):
        try:
            transposed_df = self.sales_data.T
        except Exception as e:
            raise Exception(f"Error occurred during complex data transformation: {e}")

    def group_with_function(self, column_do, column_use, func):
        try:
            grouped_result = self.sales_data.groupby(column_do)[column_use].apply(func)
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")
        except Exception as e:
            raise Exception(f"Error occurred during data grouping: {e}")

    def locate_specific_row(self, index):
        try:
            specific_row_1 = self.sales_data.loc[index]
            specific_row_2 = self.sales_data.iloc[index]
        except KeyError as e:
            raise KeyError(f"Index or column {e} not found in the DataFrame. Please check the input.")
        except Exception as e:
            raise Exception(f"Error occurred during locating specific row: {e}")

    def locate_specific_column(self, column_label):
        try:
            specific_column_label = self.sales_data[column_label]
            specific_column_index = self.sales_data.loc[:, column_label]
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")
        except Exception as e:
            raise Exception(f"Error occurred during locating specific column: {e}")

    def locate_specific_columns_and_rows(self, columns, rows_range):
        try:
            specific_data = self.sales_data.loc[rows_range, columns]
        except KeyError as e:
            raise KeyError(f"Column {e} not found in the DataFrame. Please check the column name.")
        except Exception as e:
            raise Exception(f"Error occurred during locating specific columns and rows: {e}")

    def locate_specific_rows_and_columns(self, rows, columns_range):
        try:
            specific_data = self.sales_data.iloc[rows, columns_range]
        except KeyError as e:
            raise KeyError(f"Index or column {e} not found in the DataFrame. Please check the input.")
        except Exception as e:
            raise Exception(f"Error occurred during locating specific rows and columns: {e}")

    def filter_by_mask(self, mask_list, is_by_index=False):
        try:
            if is_by_index:
                filtered_df = self.sales_data[self.sales_data.index.isin(mask_list)]
            else:
                filtered_df = self.sales_data[mask_list]
            return filtered_df
        except Exception as e:
            raise Exception(f"Error occurred during filtering by mask: {e}")

    def save_modified_sales_data(self):
        try:
            # Assuming FileOperation is a class for handling file operations
            file_operation = "c:\\"
            file_operation.save_to_excel(self.sales_data, "analyze_sales_data.xlsx")
        except Exception as e:
            raise Exception(f"Error occurred during saving modified sales data: {e}")

    @staticmethod
    def save_figures(path, figure):
        try:
            figure.savefig(path)
        except Exception as e:
            raise Exception(f"Error occurred during saving figure: {e}")
