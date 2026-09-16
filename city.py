from sale_point import SalePoint
from seller import Seller


class City:
    def __init__(self, city_title: str):
        self.__city_title = city_title
        self.__sale_points = []
        self.__sellers = []

    def add_sale_point(self, sale_point: SalePoint):
        is_valid_sale_point = self.__is_valid_sale_point(sale_point)

        if is_valid_sale_point:
            self.__sale_points.append(sale_point)
        else:
            print('Добавить точку не удалось. Некорректные данные')

    def add_seller(self, seller: Seller):
        is_valid_seller = self.__is_valid_seller(seller)

        if is_valid_seller:
            self.__sellers.append(seller)
        else:
            print('Добавить продавца не удалось. Некорректные данные')

    def show_city_info(self):
        print(f'Город: {self.__city_title}')
        for sale_point in self.__sale_points:
            sale_point.show_sellers()

    def __is_valid_sale_point(self, sale_point: SalePoint) -> bool:
        return isinstance(sale_point, SalePoint)

    def __is_valid_seller(self, seller: Seller) -> bool:
        return isinstance(seller, Seller)
