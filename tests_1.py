from unittest.mock import patch

import pytest

from main import directories, add_new_shelf, check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, delete_doc, get_doc_shelf, add_new_doc, show_all_docs_info


class TestFunctions:

    def test_show_all_docs_info(self):
        """Tests show_all_docs_info()"""
        expected = f"\npassport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов" \
                   f"\ninsurance 10006 Аристарх Павлов\n"
        assert show_all_docs_info() == expected

    @pytest.mark.parametrize("test_input,expected", (['11-2', '1'], ['10006', '2']))
    def test_get_doc_shelf(self, test_input, expected):
        """Tests get_doc_shelf()"""
        with patch("builtins.input") as mock:
            mock.return_value = test_input
            assert get_doc_shelf() == expected

    @pytest.mark.parametrize("test_input,expected", (['2207 876234', "Василий Гупкин"], [2207, None]))
    def test_get_doc_owner_name(self, test_input, expected):
        """Tests get_doc_owner_name()"""
        with patch("builtins.input") as mock:
            mock.return_value = test_input
            result = get_doc_owner_name()
            assert result == expected

    def test_get_all_doc_owners_names(self):
        """Tests get_all_doc_owners_names()"""
        expected = {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        assert get_all_doc_owners_names() == expected

    def test_remove_doc_from_shelf(self):
        """Tests remove_doc_from_shelf()"""
        test_input = '10006'
        expected = 0
        remove_doc_from_shelf(test_input)
        assert len(directories['2']) == expected

    @pytest.mark.parametrize("test_input,expected", (['1', ('1', False)], ['4', ('4', True)]))
    def test_add_new_shelf(self, test_input, expected):
        """Tests add_new_shelf()"""
        with patch("builtins.input") as mock:
            mock.return_value = test_input
            assert add_new_shelf() == expected
            if expected[1]:
                assert (mock.return_value, mock.return_value in directories.keys()) == expected

    @pytest.mark.parametrize("test_input,expected", (['11-2', True], ['11 - 3', False], ['', False]))
    def test_check_document_existance(self, test_input, expected):
        """Tests check_document_existance()"""
        assert check_document_existance(test_input) is expected

    @pytest.mark.parametrize("test_input,expected", (['11-2', ('11-2', True)], ['4', None]))
    def test_delete_doc(self, test_input, expected):
        """Tests delete_doc()"""
        with patch("builtins.input") as mock:
            mock.return_value = test_input
            assert delete_doc() == expected

    def test_add_new_doc(self):
        """Tests add_new_doc()"""
        with patch("builtins.input") as mock:
            mock.return_value = 'test_type'
            mock.return_value = 'test_number'
            mock.return_value = 'test_name'
            mock.return_value = '3'
            assert add_new_doc() == '3'


