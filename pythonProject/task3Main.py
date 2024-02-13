import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from task3 import SalesData

def main():

    data = {
        "product": ["A", "B", "A", "C", "A", "B", "C"],
        "sales": [100, 200, 300, 400, 500, 600, 700],
        "date": ["2023-01-01", "2023-01-03", "2023-02-01", "2023-02-02", "2023-02-03", "2023-03-01"],
    }


    sales_data = SalesData(data)


    sales_data.eliminate_duplicates()
    sales_data.calculate_total_sales()
    sales_data._calculate_total_sales_per_month()
    sales_data._identify_best_selling_product()
    sales_data._identify_month_with_highest_sales()
    sales_data.data["average_sales_per_month"] = (
        sales_data.data.groupby("month")["sales"].mean()
    )
    sales_data.minest_selling_product = sales_data.data.groupby("product")["sales"].sum().idxmin()
    analysis_result = sales_data.analyze_sales_data()


    print(analysis_result)


    sales_data.add_90_percent_values_column(column_name="sales")
    sales_data.bar_chart_category_sum(x_column="product", y_column="sales_90_percent_discounted")


    mean_quantity_result = sales_data.calculate_mean_quantity()
    print("Mean Quantity:", mean_quantity_result[0])
    print("Median Quantity:", mean_quantity_result[1])
    print("Second Largest Quantity:", mean_quantity_result[2])
    filtered_data = sales_data.filter_by_sellings_or_and(num_sellings_condition=5, price_condition=300)
    print("Filtered Data:")
    print(filtered_data)

    sales_data.divide_by_2()
    print("Updated Data:")
    print(sales_data.data)
    stats_result = sales_data.calculate_stats(columns=["sales", "Price"])
    print("Statistics:")
    print(stats_result)

if __name__ == "__main__":
    main()

