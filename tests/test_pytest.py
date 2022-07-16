import pytest
from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    add_new_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_all_docs_info, \
    add_new_doc

FIXTURE = [
    ('11-2', True),
    ('10-4', False),
    ('10006', True)
]


def setup():
    print('setup')


def teardown():
    print('teardown')


class TestFunctionPytest:

    @pytest.mark.parametrize('doc_num, result', FIXTURE)
    def test_check_document_existance(self, doc_num, result):
        assert check_document_existance(doc_num) == result

    def test_get_doc_owner_name(self):
        assert get_doc_owner_name('11-2') == 'Геннадий Покемонов'

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}

    def test_add_new_shelf(self):
        assert add_new_shelf('4') == ('4', True)

    def test_show_all_docs_info(self):
        assert len(show_all_docs_info()) == 3

    def test_delete_doc(self):
        assert delete_doc('10006') == ('10006', True)

    def test_get_doc_shelf(self):
        assert get_doc_shelf('11-2') == '1'

    def test_move_doc_ti_shelf(self):
        assert move_doc_to_shelf('10006', '3') == 'Документ номер "10006" был перемещен на полку номер "3"'

    def test_add_new_doc(self):
        assert add_new_doc('112', 'pass', 'Aleksey', '3') == '3'
