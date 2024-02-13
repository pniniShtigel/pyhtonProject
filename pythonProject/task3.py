import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class SalesData:

    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def eliminate_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def calculate_total_sales(self):
        self.data["total_sales"] = self.data.groupby("product")["sales"].transform("sum")

    def _calculate_total_sales_per_month(self):
        self.data["month"] = pd.to_datetime(self.data["date"]).dt.month_name()
        self.data["total_sales_per_month"] = (
            self.data.groupby(["month", "product"])["sales"].transform("sum")
        )

    def _identify_best_selling_product(self):
        self.best_selling_product = self.data.groupby("product")["sales"].sum().idxmax()

    def _identify_month_with_highest_sales(self):
        self.month_with_highest_sales = (
            self.data.groupby("month")["sales"].sum().idxmax()
        )

    def analyze_sales_data(self):

        self.eliminate_duplicates()
        self.calculate_total_sales()
        self._calculate_total_sales_per_month()
        self._identify_best_selling_product()
        self._identify_month_with_highest_sales()
        self.data["average_sales_per_month"] = (
            self.data.groupby("month")["sales"].mean()
        )
        self.minest_selling_product = self.data.groupby("product")["sales"].sum().idxmin()
        return {
            "best_selling_product": self.best_selling_product,
            "month_with_highest_sales": self.month_with_highest_sales,
            "minest_selling_product": self.minest_selling_product,
            "average_sales_per_month": self.data[["month", "average_sales_per_month"]].to_dict(
                orient="records"
            ),
        }


    def calculate_cumulative_sales(self):

        grouped_sales = self.data.groupby(["product", "month"])["sales"].sum().unstack()
        grouped_sales["cumulative_sales"] = grouped_sales.cumsum(axis=1)
        return grouped_sales.reset_index()

    def add_90_percent_values_column(self, column_name: str = "Quantity"):

        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' not found in SalesData DataFrame.")

        percentile_value = self.data[column_name].quantile(0.9)
        discount = 0.1  # 10% הנחה
        discounted_value = percentile_value * (1 - discount)
        self.data["{}_90_percent_discounted".format(column_name)] = np.where(
            self.data[column_name] <= discounted_value, discounted_value, self.data[column_name]
        )

    def bar_chart_category_sum(self, x_column: str = "product", y_column: str = "Quantity"):

        if x_column not in self.data.columns or y_column not in self.data.columns:
            raise ValueError(f"Invalid column(s) specified: {x_column}, {y_column}")

        data = self.data.groupby(x_column)[y_column].sum().reset_index()
        plt.bar(data[x_column], data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Sum of {} per {}".format(y_column, x_column))
        plt.show()

    def calculate_mean_quantity(self):

        if "Total" not in self.data.columns:
            raise ValueError("Column 'Total' not found in SalesData DataFrame.")

        total_array = self.data["Total"].to_numpy()
        return np.mean(total_array), np.median(total_array), np.partition(total_array, -2)[-2]

    def filter_by_sellings_or_and(self, num_sellings_condition: int = 5, price_condition: float = 300):

        filtered_data = self.data[(self.data["Number of Sellings"] > num_sellings_condition) |
                                  (self.data["Number of Sellings"] == 0)]
        filtered_data = filtered_data[filtered_data["Price"] > price_condition]
        filtered_data = filtered_data[filtered_data["Number of Sellings"] < 2]
        return filtered_data

    def divide_by_2(self):

        black_friday_data = self.data[self.data["Date"] == "BLACK FRIDAY"]
        black_friday_data["BlackFridayPrice"] = black_friday_data["Price"] / 2
        self.data.update(black_friday_data)

    def calculate_stats(self, columns: str = None):

        if columns is None:
            columns = self.data.columns
        results = {}
        for column in columns:
            results[column] = {
                "max": self.data[column].max(),
                "sum": self.data[column].sum(),
                "abs": self.data[column].abs().sum(),
                "cummax": self.data[column].cummax(),
            }
        return results

