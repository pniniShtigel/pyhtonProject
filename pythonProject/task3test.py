import unittest
from task3 import SalesData

class TestSalesData(unittest.TestCase):

    def setUp(self):

        self.data = {
            "Date": ["2023-01-01", "2023-01-02", "2023-02-01", "2023-02-02"],
            "Product": ["A", "B", "A", "B"],
            "Quantity": [10, 20, 30, 40],
            "Price": [100, 200, 300, 400],
            "Total": [1000, 4000, 9000, 16000],
        }
        self.sales_data = SalesData(self.data)

    def test_calculate_total_sales(self):
        # בדיקת חישוב סך המכירות
        self.sales_data.calculate_total_sales()
        expected_total_sales = [1000, 4000, 9000, 16000]
        self.assertEqual(self.sales_data.data["total_sales"].tolist(), expected_total_sales)

    def test_calculate_cumulative_sales(self):

        expected_cumulative_sales = {
            "product": ["A", "B"],
            "month": ["January", "February"],
            "cumulative_sales": [1000, 4000, 13000, 29000],
        }
        df = self.sales_data.calculate_cumulative_sales()
        self.assertEqual(df.to_dict(orient="records"), expected_cumulative_sales)

    def test_add_90_percent_values_column(self):

        self.sales_data.add_90_percent_values_column()
        expected_90_percent_values = [180, 360, 270, 360]
        self.assertEqual(
            self.sales_data.data["Quantity_90_percent_discounted"].tolist(),
            expected_90_percent_values,
        )

    def test_bar_chart_category_sum(self):

        with self.assertRaises(ValueError):
            self.sales_data.bar_chart_category_sum(x_column="NonexistentColumn")
        self.sales_data.bar_chart_category_sum()  # פונקציה זו מציירת גרף, אין צורך לבדוק ערך

    def test_calculate_mean_quantity(self):

        expected_results = (10000, 20000, 30000)
        self.assertEqual(self.sales_data.calculate_mean_quantity(), expected_results)

    def test_filter_by_sellings_or_and(self):

        expected_filtered_data = {
            "Date": ["2023-01-01", "2023-02-02"],
            "Product": ["A", "B"],
            "Quantity": [10, 40],
            "Price": [100, 400],
            "Total": [1000, 16000],
        }
        df = self.sales_data.filter_by_sellings_or_and()
        self.assertEqual(df.to_dict(orient="records"), expected_filtered_data)

    def test_divide_by_2(self):
        def test_divide_by_2(self):

            self.sales_data.data["Date"] = ["2023-01-01", "2023-02-01", "2023-11-25"]
            self.sales_data.data["Price"] = [100, 200, 300]
            self.sales_data.divide_by_2()
            expected_black_friday_price = 150
            self.assertEqual(self.sales_data.data.loc[2, "BlackFridayPrice"], expected_black_friday_price)

        def test_calculate_stats(self):

            expected_results_all_columns = {
                "Date": {"max": "2023-11-25", "sum": "2023-06-02", "abs": "2023-06-02", "cummax": "2023-11-25"},
                "Product": {"max": "B", "sum": "AB", "abs": "AB", "cummax": "B"},
                "Quantity": {"max": 40, "sum": 100, "abs": 100, "cummax": 140},
                "Price": {"max": 300, "sum": 600, "abs": 600, "cummax": 900},
                "Total": {"max": 16000, "sum": 36000, "abs": 36000, "cummax": 52000},
            }
            expected_results_single_column = {
                "Quantity": {"max": 40, "sum": 100, "abs": 100, "cummax": 140},
            }
            self.assertEqual(self.sales_data.calculate_stats(), expected_results_all_columns)
            self.assertEqual(self.sales_data.calculate_stats("Quantity"), expected_results_single_column)

    if __name__ == "__main__":
        unittest.main()
