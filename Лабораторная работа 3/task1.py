class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name: Название книги
        :param author: Автор книги
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self._author = author
        self._name = name
        # self.name = name
        # self.author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка объекта "Аудио книга"
        :params name: Название книги
        :params author: Автор книги
        :params pages: Количество страниц в книге
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц в книге должно быть больше нуля")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Кол-во страниц {self._pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, " \
               f"author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    """Класс аудио книги"""
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка объекта "Аудио книга"
        :params name: Название книги
        :params author: Автор книги
        :params duration: Продолжительность книги
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float!")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть числом больше нуля!")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, " \
               f"author={self._author!r}, duration={self._duration!r})"


book1 = Book("Война и мир", "Толстой")
book2 = PaperBook("Война и мир", "Толстой", 200)
book3 = AudioBook("Война и мир", "Толстой", 12.0)
print(book1)
print(repr(book1))
print(book2)
print(repr(book2))
print(book3)
print(repr(book3))
