class Seller:
    def __init__(self, name: str):
        is_valid = self.__is_valid_name(name)

        self.__products = {}

        if is_valid:
            self.__name = name.title()
        else:
            self.__name = 'Имя неизвестно'

    def get_name(self) -> str:
        return self.__name

    def __is_valid_name(self, name: str) -> bool:
        if isinstance(name, str):
            if name.strip():
                return True
        return False

    def add_product(self, product: str, quantity: int):
        product_valid = self.__is_product_valid(product)
        quantity_valid = self.__is_quantity_valid(quantity)

        if product_valid and quantity_valid:
            product = product.capitalize()

            if product not in self.__products:
                self.__products[product] = quantity
            else:
                self.__products[product] += quantity
        else:
            print('Некорректные данные. Попробуйте снова')

    def sell_product(self, product: str, quantity: int) -> bool:
        product = product.capitalize()

        if product not in self.__products:
            return False

        if self.__products[product] < quantity:
            return False

        self.__products[product] -= quantity
        return True

    def get_products(self) -> dict:
        return self.__products

    def __is_product_valid(self, product: str) -> bool:
        if not isinstance(product, str):
            return False

        if not product.strip():
            return False

        return True

    def __is_quantity_valid(self, quantity: int) -> bool:
        if not isinstance(quantity, int):
            return False

        if quantity < 1:
            return False

        return True
