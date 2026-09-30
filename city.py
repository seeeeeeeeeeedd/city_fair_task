from sale_point import SalePoint


class City:
    def __init__(self, city_title: str):
        self.__city_title = city_title
        self.__sale_points = []

    def add_sale_point(self, sale_point: SalePoint):
        is_valid_sale_point = self.__is_valid_sale_point(sale_point)

        if is_valid_sale_point:
            new_sale_point_title = sale_point.get_title()
            existing_sale_point = self.find_sale_point_by_title(new_sale_point_title)

            if existing_sale_point:
                print('Торговая точка с таким названием уже существует. Добавление невозможно')
            else:
                self.__sale_points.append(sale_point)
        else:
            print('Добавить точку не удалось. Некорректные данные')

    def show_city_info(self):
        print(f'Город: {self.__city_title}')

        for sale_point in self.__sale_points:
            sale_point.show_sellers()

    def show_all_sellers(self):
        for sale_point in self.__sale_points:
            sellers = sale_point.get_sellers()

            for seller in sellers:
                current_seller_name = seller.get_name()
                print(f'Продавец: {current_seller_name}')

    def find_sale_point_by_title(self, title: str):
        for sale_point in self.__sale_points:
            current_sale_point_title = sale_point.get_title()

            if current_sale_point_title.lower() == title.lower():
                return sale_point

        return None

    def find_seller_on_points(self, name: str):
        for sale_point in self.__sale_points:
            sellers = sale_point.get_sellers()

            for seller in sellers:
                current_seller_name = seller.get_name().lower()

                if current_seller_name == name.lower():
                    return seller

        return None

    def sell_product_on_point(self, seller_name: str, point_title: str, product: str, quantity: int) -> tuple[
        bool, str]:
        sale_point = self.find_sale_point_by_title(point_title)

        if not sale_point:
            return (False, 'Точка не найдена')

        result = sale_point.sell_product(seller_name, product, quantity)

        return result

    def __is_valid_sale_point(self, sale_point: SalePoint) -> bool:
        return isinstance(sale_point, SalePoint)
