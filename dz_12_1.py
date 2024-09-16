from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс Товар с закрытыми атрибутами наимаенование товара,
    магазин продавец, цена товара
    """

    __name: str
    __store_name: str
    __price: float

    @property
    def name(self):
        return self.__name

    @property
    def store_name(self):
        return self.__store_name

    @property
    def price(self):
        return self.__price


class Warehouse:
    """
    Класс Склад хранящий закрытый массив с товарами,
    имеет метод для вывода инфо по товару по индексу,
    выводи инфо товара по наименованию, сортировки товаров по наименованию,
    магазину продавцу и цене"""
    def __init__(self, *args):
        self.__products = args

    def output_by_index(self, find_index):
        try:
            product = self.__products[find_index]
            print(
                "Информация:\n"
                f"Наименование товара: {product.name}\n"
                f"Магазин продающий товар: {product.store_name}\n"
                f"Стоимость товара: {product.price} руб"
            )
        except IndexError:
            print("Такой индекс отсутствует!!")

    def output_by_name(self, find_name):
        for product in self.__products:
            if product.name.lower() == find_name.lower():
                print(
                    "Информация:\n"
                    f"Наименование товара: {product.name}\n"
                    f"Магазин продающий товар: {product.store_name}\n"
                    f"Стоимость товара: {product.price} руб"
                )
                break
        else:
            print("Такое наименование отсутсвует на складе!!")

    def sort_by_name(self):
        self.__products = sorted(
            self.__products, key=lambda product: product.name.lower()
        )

    def sort_by_store_name(self):
        self.__products = sorted(
            self.__products, key=lambda product: product.store_name.lower()
        )

    def sort_by_price(self):
        self.__products = sorted(self.__products, key=lambda product: product.price)


orange = Product("Апельсин", "Пятёрочка", 5)
apple = Product("Яблоко", "Евроопт", 4)
milk = Product("Молоко", "Виталюр", 3)
banan = Product("Банан", "Санта", 8)

warehouse = Warehouse(orange, apple, milk, banan)
warehouse.output_by_name("яблоко")
warehouse.output_by_index(2)
warehouse.sort_by_name()
warehouse.sort_by_store_name()
warehouse.sort_by_price()
