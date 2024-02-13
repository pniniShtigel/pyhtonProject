import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TestDataVisualization(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Date': pd.date_range('2022-01-01', periods=5),
            'Sales': [100, 150, 200, 120, 180],
            'Quantity': [10, 15, 20, 12, 18],
            'Revenue': [500, 750, 1000, 600, 900],
            'Category': ['A', 'B', 'A', 'C', 'B'],
            'Profit': [50, 75, 100, 60, 90],
            'Price': [30, 40, 25, 35, 50]
        })

    def test_matplotlib_line_plot(self):
        plt.plot(self.df['Date'], self.df['Sales'], label='Sales')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.title('Sales Over Time')
        plt.legend()
        plt.savefig('test_matplotlib_line_plot.png')

        plt.close()

    def test_seaborn_scatter_plot(self):
        sns.scatterplot(x='Quantity', y='Revenue', data=self.df)
        plt.title('Seaborn Scatter Plot of Quantity vs Revenue')
        plt.savefig('test_seaborn_scatter_plot.png')
        plt.close()



if __name__ == '__main__':
    unittest.main()
