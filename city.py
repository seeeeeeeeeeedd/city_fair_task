from district import District


class City:
    def __init__(self, city_title: str):
        self.__city_title = city_title
        self.__districts = []

    def add_district(self, district: District):
        self.__districts.append(district)

    def show_city_info(self):
        print(f'Город: {self.__city_title}')
        for district in self.__districts:
            district.show_district_info()
