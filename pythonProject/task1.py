import pandas as pd

class DataReader:
    def __init__(self):
        pass

    def read_excel(self, file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_excel(file_path)
        except FileNotFoundError:
            print(f"Error: Excel file not found at '{file_path}'.")
            return None
        except pd.errors.ParserError:
            print(f"Error: Could not parse Excel file at '{file_path}'.")
            return None

        return df

# Example usage
data_reader = DataReader()
data = data_reader.read_excel("C:/Users/user1/Desktop/תכנות/pyton/project/text.xlsx")

if data is not None:
    print(data.head())

class DataWriter:
    def __init__(self):
        pass

    def save_to_excel(self, data, file_name: str):

        try:
            # Convert the data to a Pandas DataFrame if it is not already
            if not isinstance(data, pd.DataFrame):
                data = pd.DataFrame(data)

            # Save the data to the Excel file using Pandas
            data.to_excel(file_name, index=False)
            print(f"Data saved to '{file_name}' successfully.")
        except Exception as e:
            print(f"Error: {e}")

# Example usage
data_writer = DataWriter()
data_writer.save_to_excel(data, "C:/Users/user1/Desktop/תכנות/pyton/project/task2.xlsx")

