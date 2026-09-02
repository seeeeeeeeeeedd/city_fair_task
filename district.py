from sale_point import SalePoint


class District:
    def __init__(self, district_title: str):
        self.__district_title = district_title
        self.__sale_points = []

    def add_sale_point(self, sale_point: SalePoint):
        self.__sale_points.append(sale_point)

    def show_district_info(self):
        print(f'Район: {self.__district_title}')
        for point in self.__sale_points:
            point.show_sellers()
