import pandas as pd


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

data = {
    "product": ["A", "B", "A", "C", "A", "B", "C"],
    "sales": [100, 200, 300, 400, 500, 600, 700],
    "date": ["2023-01-01", "2023-01-03", "2023-02-01", "2023-02-02", "2023-02-03", "2023-03-01"],
}

sales_data = SalesData(data)
analysis_result = sales_data.analyze_sales_data()

print(analysis_result)
