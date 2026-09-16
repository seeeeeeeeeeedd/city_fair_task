from seller import Seller


class SalePoint:
    def __init__(self, title: str):
        self.__title = title
        self.__sellers = []

    def add_seller(self, seller: Seller):
        if self.__is_valid_seller(seller):
            self.__sellers.append(seller)
        else:
            print('Ошибка. Переданный объект не является продавцом')

    def show_sellers(self):
        if not self.__sellers:
            print('На торговой точке продавцов нет')
        else:
            for seller in self.__sellers:
                print(f'Продавец на точке "{self.__title}": {seller.get_name()}')

    def delete_seller(self, seller: Seller):
        if seller in self.__sellers:
            self.__sellers.remove(seller)
            print('Продавец удален из торговой точки')
        else:
            print('Такого продавца нет на торговой точке. Ошибка удаления')

    def __is_valid_seller(self, seller: Seller) -> bool:
        return isinstance(seller, Seller)
