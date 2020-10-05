import unittest
from unittest.mock import patch,  call

from src.core.table import get_table_width, print_divider, print_table_header

class Test_Get_Table_Width(unittest.TestCase):
    def test_when_an_item_is_longer_than_the_title_return_item_length_plus_2(self):
        # Arrange
        title = "Orange"
        data = ["Are", "Orangutan", "Kite"]
        expected = len("Orangutan") + 2

        # Act
        actual = get_table_width(title, data)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_an_title_is_longer_than_the_items_return_title_length_plus_2(self):
        # Arrange
        title = "Rhinocerous"
        data = ["Are", "Blue", "Kite"]
        expected = len("Rhinocerous") + 2

        # Act
        actual = get_table_width(title, data)

        # Assert
        self.assertEqual(actual, expected)


class Test_Table_Print_Functions(unittest.TestCase):
    @patch("builtins.print")
    def test_print_divider_prints_to_specifed_length(self, print_mock):
        # Arrange
        # Act
        print_divider(30)

        # Assert
        print_mock.assert_called_once_with('+==============================+')

    @patch("src.core.table.print_divider")
    @patch("builtins.print")
    def test_print_table_header_prints_header(self, print_mock, print_divider_mock):
        # Arrange
        title = 'title'
        print_divider_mock.side_effect = None

        # Act
        print_table_header(title, 30)
        expected = [call('| TITLE')]

        # Assert
        self.assertEqual(print_divider_mock.call_count, 2)
        self.assertEqual(print_mock.call_args_list, expected)

# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()
