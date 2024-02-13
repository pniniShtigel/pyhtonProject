from task2 import SalesData
def main():

    data = {
        "product": ["A", "B", "A", "C", "A", "B", "C"],
        "sales": [100, 200, 300, 400, 500, 600, 700],
        "date": ["2023-01-01", "2023-01-03", "2023-02-01", "2023-02-02", "2023-02-03", "2023-03-01"],
    }


    sales_data = SalesData(data)


    analysis_result = sales_data.analyze_sales_data()


    print(analysis_result)


if __name__ == "__main__":
    main()
