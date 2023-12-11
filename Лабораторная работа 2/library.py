# import doctest

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """Класс, описывающий книгу"""
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: id книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("id книги должен быть типа int!")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str!")
        if not isinstance(pages, int):
            raise TypeError("Число страниц в книге должно быть типа int!")
        if pages <= 0:
            raise ValueError("Число страниц в книге должно быть больше 0!")
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    """Класс, описывающий библиотеку книг"""
    def __init__(self, books=None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: список книг, является необязательным параметром
        """
        if books is None:
            books = []
        elif not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list!")
        else:
            # Проверяем, что все элементы списка books являются экземплярами
            # класса Book
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("Книги в списке должны быть типа Book!")
        self.books = books

    def get_next_book_id(self):
        """
        Метод возвращает идентификатор для добавления новой книги
        в библиотеку. Если список книг пустой вернёт 1.
        """
        return 1 if len(self.books) == 0 else self.books[-1].id + 1

    def get_index_by_book_id(self, search_book_id: int):
        """
        Метод, возвращающий индекс книги в списке
        :param search_book_id: id искомой книги
        :raise ValueError: Если книги с данным id нет в списке книг
        """
        if not isinstance(search_book_id, int):
            raise TypeError("Идентификатор искомой книги должен быть типа int!")
        for index, book in enumerate(self.books):
            if book.id == search_book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует!")


if __name__ == '__main__':
    # doctest.testmod()
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
