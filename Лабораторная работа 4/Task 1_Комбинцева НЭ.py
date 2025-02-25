from typing import List, Optional

class Predator:
    """
    Базовый класс для хищных животных.
    Атрибуты:
        species (str): Вид хищника.
        habitat (str): Место обитания.
        diet (List[str]): Список предпочитаемой пищи.
    """
    def __init__(self, species: str, habitat: str, diet: List[str]) -> None:
        self.species = species
        self.habitat = habitat
        self.diet = diet

    def __str__(self) -> str:
        return f"{self.species}, обитает в {self.habitat}, питается {', '.join(self.diet)}."

    def __repr__(self) -> str:
        return f"Predator(species={self.species}, habitat={self.habitat}, diet={self.diet})"

    def hunt(self, prey: str) -> str:
        """
        Метод, описывающий охоту на добычу.
        Аргументы:
            prey (str): Название добычи.
        Возвращает:
            str: Сообщение о результате охоты.
        """
        return f"{self.species} охотится на {prey}."


class Lion(Predator):
    """
    Дочерний класс для львов.
    Атрибуты:
        pride_size (int): Размер прайда.
    """
    def __init__(self, habitat: str, diet: List[str], pride_size: int) -> None:
        super().__init__("Лев", habitat, diet)
        self._pride_size = pride_size  # Непубличный атрибут

    def __str__(self) -> str:
        return f"{self.species}, обитает в {self.habitat}, питается {', '.join(self.diet)}, размер прайда: {self._pride_size}."

    def __repr__(self) -> str:
        return f"Lion(species={self.species}, habitat={self.habitat}, diet={self.diet}, pride_size={self._pride_size})"

    def roar(self) -> str:
        """
        Метод, описывающий рычание льва.
        Возвращает:
            str: Сообщение о рычании.
        """
        return f"{self.species} громко рычит!"

    def hunt(self, prey: str) -> str:
        """
        Перегруженный метод охоты для львов.
        Львы охотятся в группах, поэтому добавляем информацию о прайде.
        Аргументы:
            prey (str): Название добычи.
        Возвращает:
            str: Сообщение о результате охоты.
        """
        return f"{self.species} и его прайд из {self._pride_size} особей охотятся на {prey}."


class Book:
    """
    Базовый класс для книг.
    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц.
    """
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга '{self.title}' автора {self.author}, {self.pages} страниц."

    def __repr__(self) -> str:
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"

    def read(self) -> str:
        """
        Метод, описывающий чтение книги.
        Возвращает:
            str: Сообщение о чтении.
        """
        return f"Вы читаете книгу '{self.title}'."


class FictionBook(Book):
    """
    Дочерний класс для художественных книг.
    Атрибуты:
        genre (str): Жанр книги.
    """
    def __init__(self, title: str, author: str, pages: int, genre: str) -> None:
        super().__init__(title, author, pages)
        self.genre = genre

    def __str__(self) -> str:
        return f"Художественная книга '{self.title}' автора {self.author}, жанр: {self.genre}, {self.pages} страниц."

    def __repr__(self) -> str:
        return f"FictionBook(title={self.title}, author={self.author}, pages={self.pages}, genre={self.genre})"

    def read(self) -> str:
        """
        Перегруженный метод чтения для художественных книг.
        Художественные книги читаются для удовольствия.
        Возвращает:
            str: Сообщение о чтении.
        """
        return f"Вы наслаждаетесь чтением художественной книги '{self.title}'."


class ReferenceBook(Book):
    """
    Дочерний класс для справочных книг.
    Атрибуты:
        topic (str): Тема справочника.
    """
    def __init__(self, title: str, author: str, pages: int, topic: str) -> None:
        super().__init__(title, author, pages)
        self.topic = topic

    def __str__(self) -> str:
        return f"Справочная книга '{self.title}' автора {self.author}, тема: {self.topic}, {self.pages} страниц."

    def __repr__(self) -> str:
        return f"ReferenceBook(title={self.title}, author={self.author}, pages={self.pages}, topic={self.topic})"

    def read(self) -> str:
        """
        Перегруженный метод чтения для справочных книг.
        Справочные книги читаются для поиска информации.
        Возвращает:
            str: Сообщение о чтении.
        """
        return f"Вы ищете информацию в справочной книге '{self.title}'."


class Furniture:
    """
    Базовый класс для мебели.
    Атрибуты:
        material (str): Материал мебели.
        color (str): Цвет мебели.
    """
    def __init__(self, material: str, color: str) -> None:
        self.material = material
        self.color = color

    def __str__(self) -> str:
        return f"Мебель из {self.material}, цвет: {self.color}."

    def __repr__(self) -> str:
        return f"Furniture(material={self.material}, color={self.color})"

    def assemble(self) -> str:
        """
        Метод, описывающий сборку мебели.
        Возвращает:
            str: Сообщение о сборке.
        """
        return f"Мебель из {self.material} собирается."


class Table(Furniture):
    """
    Дочерний класс для столов.
    Атрибуты:
        shape (str): Форма стола.
    """
    def __init__(self, material: str, color: str, shape: str) -> None:
        super().__init__(material, color)
        self.shape = shape

    def __str__(self) -> str:
        return f"Стол из {self.material}, цвет: {self.color}, форма: {self.shape}."

    def __repr__(self) -> str:
        return f"Table(material={self.material}, color={self.color}, shape={self.shape})"

    def assemble(self) -> str:
        """
        Перегруженный метод сборки для столов.
        Столы могут иметь сложную сборку из-за формы.
        Возвращает:
            str: Сообщение о сборке.
        """
        return f"Стол формы {self.shape} из {self.material} собирается с дополнительными инструкциями."


class Chair(Furniture):
    """
    Дочерний класс для стульев.
    Атрибуты:
        has_backrest (bool): Наличие спинки.
    """
    def __init__(self, material: str, color: str, has_backrest: bool) -> None:
        super().__init__(material, color)
        self.has_backrest = has_backrest

    def __str__(self) -> str:
        backrest_info = "со спинкой" if self.has_backrest else "без спинки"
        return f"Стул из {self.material}, цвет: {self.color}, {backrest_info}."

    def __repr__(self) -> str:
        return f"Chair(material={self.material}, color={self.color}, has_backrest={self.has_backrest})"

    def assemble(self) -> str:
        """
        Перегруженный метод сборки для стульев.
        Стулья могут иметь разную сложность сборки в зависимости от наличия спинки.
        Возвращает:
            str: Сообщение о сборке.
        """
        if self.has_backrest:
            return f"Стул из {self.material} со спинкой собирается с дополнительными инструкциями."
        else:
            return f"Стул из {self.material} без спинки легко собирается."


if __name__ == "__main__":
    # Пример использования классов
    lion = Lion("саванна", ["антилопы", "зебры"], 5)
    print(lion)
    print(lion.hunt("зебру"))
    print(lion.roar())

    fiction_book = FictionBook("1984", "Джордж Оруэлл", 328, "антиутопия")
    print(fiction_book)
    print(fiction_book.read())

    reference_book = ReferenceBook("Энциклопедия", "Неизвестный автор", 1000, "Наука")
    print(reference_book)
    print(reference_book.read())

    table = Table("дерево", "коричневый", "круглый")
    print(table)
    print(table.assemble())

    chair = Chair("металл", "чёрный", True)
    print(chair)
    print(chair.assemble())