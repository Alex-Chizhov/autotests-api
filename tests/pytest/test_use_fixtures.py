import pytest


@pytest.fixture
def clear_books_database():
    """Фикстура для очистки данных из базы данных"""
    print("[FIXTURE] Удаляем все данные из базы данных")


@pytest.fixture
def fill_books_database():
    """Фипкстура для заполнения данных в базе данных"""
    print("[FIXTURE] Создаем новые данные в базе данных")


@pytest.mark.usefixtures("fill_books_database", "clear_books_database")
class TestLibrary:

    def test_read_book(self):
        ...

    def test_delete_book(self):
        ...