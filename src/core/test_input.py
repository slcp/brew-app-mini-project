import unittest
from unittest.mock import Mock, patch

from src.core.input import select_person_from_menu
from src.models.person import Person

class Test_Select_Person_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    #
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    @patch("src.core.input.select_from_menu")
    def test_when_number_is_returned_from_select_return_the_person_at_that_position(self, mock_select_from_menu):
        # Arrange
        person = Mock(Person)
        person.name = "Stuart"
        people = [person]
        mock_select_from_menu.return_value = 0
        
        # Act
        actual = select_person_from_menu(people)

        # Assert
        self.assertEqual(actual, people[0])

    @patch("src.core.input.select_from_menu")
    def test_when_false_is_returned_from_select_menu_return_none(self, mock_select_from_menu):
        # Arrange
        person = Mock(Person)
        person.name = "Stuart"
        people = [person]
        mock_select_from_menu.return_value = False

        # Act
        actual = select_person_from_menu(people)

        # Assert
        self.assertFalse(actual)


# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()
