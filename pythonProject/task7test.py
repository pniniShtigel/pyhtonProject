import unittest
from task7 import TaskHandler


class TestTaskHandler(unittest.TestCase):

    def setUp(self):
        self.task_handler = TaskHandler()

    def test_handle_error(self):
        with self.assertRaises(TypeError):
            self.task_handler.handle_error(TypeError, "value", "parameter_name")

    def test_read_csv(self):
        with self.assertLogs() as cm:
            self.task_handler.read_csv('example.csv')
        self.assertTrue("['row_data_1']" in cm.output[0])

    def test_read_word(self):

        with self.assertLogs() as cm:
            self.task_handler.read_word('example.docx')
        self.assertTrue("paragraph_text_1" in cm.output[0])

    def test_random_sales_and_highest_payment(self):
        product_name = "Example Product"
        sales, highest_payment = self.task_handler.random_sales_and_highest_payment(product_name)
        self.assertTrue(isinstance(sales, int))
        self.assertTrue(isinstance(highest_payment, float))

    def test_print_python_version(self):
        with self.assertLogs() as cm:
            self.task_handler.print_python_version()
        self.assertTrue("Python Version:" in cm.output[0])

    def test_process_parameters(self):
        result = self.task_handler.process_parameters(5, "text", "example", VALUE_NAME="example")
        self.assertEqual(result, {"example": "example"})

    def test_print_table(self):
        with self.assertLogs() as cm:
            self.task_handler.print_table(df)


    def test_iterate_over_table(self):
        with self.assertLogs() as cm:
            self.task_handler.iterate_over_table(df)


if __name__ == '__main__':
    unittest.main()
