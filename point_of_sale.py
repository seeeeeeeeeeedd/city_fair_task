from seller import Seller


class PointOfSale:
    def __init__(self, title: str):
        self.__title = title
        self.__sellers = []

    def add_seller(self, seller: Seller):
        self.__sellers.append(seller)

    def show_sellers(self):
        if not self.__sellers:
            print('На торговой точке продавцов нет')
        else:
            for seller in self.__sellers:
                print(f'Продавец на точке "{self.__title}": {seller.get_name()}')
