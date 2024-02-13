import unittest
import pandas as pd

from task2 import SalesData


class DataAnalyzer:
    pass


class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):

        data = {
            'Date': pd.to_datetime(['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02']),
            'Product': ['A', 'B', 'A', 'B'],
            'Quantity': [10, 5, 8, 12],
            'Price': [20, 30, 25, 15],
        }
        self.data_analyzer = DataAnalyzer(pd.DataFrame(data))

    def test_eliminate_duplicates(self):
        self.data_analyzer.eliminate_duplicates()
        self.assertEqual(len(self.data_analyzer.data), 4)

    def test_calculate_total_sales(self):
        self.data_analyzer.calculate_total_sales()
        self.assertTrue('Total Sales' in self.data_analyzer.data.columns)

    def test_analyze_sales_data(self):
        analysis_result = self.data_analyzer.analyze_sales_data()
        self.assertTrue('best_selling_product' in analysis_result)
        self.assertTrue('month_with_highest_sales' in analysis_result)

    def test_additional_analysis(self):
        additional_result = self.data_analyzer.additional_analysis()
        self.assertTrue('minimest_selling_product' in additional_result)
        self.assertTrue('average_sales' in additional_result)

if __name__ == '__main__':
    unittest.main()
