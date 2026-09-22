from seller import Seller

SELLER_NAMES_SEPARATOR = ", "


class SalePoint:
    def __init__(self, title: str):
        self.__title = title.capitalize()
        self.__sellers = []

    def add_seller(self, seller: Seller):
        if self.__is_valid_seller(seller):
            self.__sellers.append(seller)
        else:
            print('Ошибка. Переданный объект не является продавцом')

    def show_sellers(self):
        seller_names = []
        for seller in self.__sellers:
            seller_names.append(seller.get_name())
        if not seller_names:
            print(f'Точка: "{self.get_title()}", продавцы: на торговой точке продавцов нет')
        else:
            print(f'Точка: "{self.get_title()}", продавцы: {SELLER_NAMES_SEPARATOR.join(seller_names)}')

    def delete_seller(self, seller: Seller):
        if seller in self.__sellers:
            self.__sellers.remove(seller)
            print('Продавец удален из торговой точки')
        else:
            print('Такого продавца нет на торговой точке. Ошибка удаления')

    def get_title(self):
        return self.__title

    def get_sellers(self):
        return self.__sellers

    def __is_valid_seller(self, seller: Seller) -> bool:
        return isinstance(seller, Seller)
