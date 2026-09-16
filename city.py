from sale_point import SalePoint


class City:
    def __init__(self, city_title: str):
        self.__city_title = city_title
        self.__sale_points = []

    def add_sale_point(self, sale_point: SalePoint):
        is_valid_sale_point = self.__is_valid_sale_point(sale_point)

        if is_valid_sale_point:
            self.__sale_points.append(sale_point)
        else:
            print('Добавить точку не удалось. Некорректные данные')

    def show_city_info(self):
        print(f'Город: {self.__city_title}')
        for sale_point in self.__sale_points:
            sale_point.show_sellers()

    def __is_valid_sale_point(self, sale_point: SalePoint) -> bool:
        if isinstance(sale_point, SalePoint):
            return True
        return False
