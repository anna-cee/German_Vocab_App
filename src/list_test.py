import pytest



def test_menu():
    menu_option = input
    if menu_option == int:
        assert ('Please enter an option from the menu')
    if menu_option != '1' or '2' or '3' or '4' or '5':
         assert ('Please enter an option from the menu')