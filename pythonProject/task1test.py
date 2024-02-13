import unittest
import pandas as pd
import os
from task1 import DataReader, DataWriter


class TestDataReading(unittest.TestCase):
    def setUp(self):
        self.data_reader = DataReader()

    def test_read_existing_excel_file(self):
        file_path = "C:/Users/user1/Desktop/תכנות/pyton/project/text.xlsx"
        data = self.data_reader.read_excel(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    def test_read_nonexistent_excel_file(self):
        file_path = "nonexistent_file.xlsx"
        data = self.data_reader.read_excel(file_path)
        self.assertIsNone(data)

    def test_read_invalid_excel_file(self):
        file_path = "C:/Users/user1/Desktop/תכנות/pyton/project/invalid_file.xlsx"
        data = self.data_reader.read_excel(file_path)
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()

class TestDataWriting(unittest.TestCase):
    def setUp(self):
        self.data_writer = DataWriter()
        self.sample_data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 22],
            'City': ['New York', 'San Francisco', 'Los Angeles']
        }

    def test_save_to_excel(self):
        file_name = "C:/Users/user1/Desktop/תכנות/pyton/project/test_output.xlsx"

        # Test saving data to a new Excel file
        self.data_writer.save_to_excel(self.sample_data, file_name)
        self.assertTrue(os.path.exists(file_name))

        # Check if the saved data is correct
        loaded_data = pd.read_excel(file_name)
        pd.testing.assert_frame_equal(loaded_data, pd.DataFrame(self.sample_data))

        # Test overwriting an existing Excel file
        updated_data = {
            'Name': ['David', 'Eva', 'Frank'],
            'Age': [28, 35, 26],
            'City': ['Chicago', 'Seattle', 'Austin']
        }

        self.data_writer.save_to_excel(updated_data, file_name)
        loaded_updated_data = pd.read_excel(file_name)
        pd.testing.assert_frame_equal(loaded_updated_data, pd.DataFrame(updated_data))

    def tearDown(self):
        # Clean up - delete the test output file
        file_name = "C:/Users/user1/Desktop/תכנות/pyton/project/test_output.xlsx"
        if os.path.exists(file_name):
            os.remove(file_name)

if __name__ == '__main__':
    unittest.main()
