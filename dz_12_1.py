from dataclasses import dataclass

# class Product:
#     def __init__(self, name: str, store_name: str, price: float):
#         self.__name = name
#         self.__store_name = store_name
#         self.__price = price

#     @property
#     def name(self):
#         return self.__name


#     @property
#     def store_name(self):
#         return self.__store_name


#     @property
#     def price(self):
#         return self.__price

@dataclass
class Product:
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

    def __init__(self, *args):
        self.__products = args

    def output_by_name(self, find_name):
        for product in self.__products:
            if product.name.lower() == find_name.lower():
                print("Информация:\n"
                      f"Наименование товара: {product.name}\n"
                      f"Магазин продающий товар: {product.store_name}\n"
                      f"Стоимость товара: {product.price}")





orange = Product("Апельсин", "Пятёрочка", 5)
apple = Product("Яблоко", "Евроопт", 4)
milk = Product("Молоко", "Виталюр", 3)

warehouse = Warehouse(orange, apple, milk)
warehouse.output_by_name("яблоко")