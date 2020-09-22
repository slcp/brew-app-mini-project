def add_two_numbers_together(num1, num2):
    return num1 + num2


def test_add_two_numbers_together_success():
    # Arrange
    num1 = 10
    num2 = 5
    expected = 15

    # Act
    actual = add_two_numbers_together(num1, num2)

    # Assert
    assert expected == actual


# def test_add_two_numbers_together_not_success():
#     # Arrange
#     num1 = "hello"
#     num2 = 5
#     # expected = 10

#     # Act
#     try:
#         add_two_numbers_together(num1, num2)
#         # This will always fail the assertion
#         assert False == True
#     except:
#         print('exc')
#         # This will always pass the assertion
#         assert True == True

#     # # Assert
#     # assert expected == actual

test_add_two_numbers_together_success()
# test_add_two_numbers_together_not_success()
