from seller import Seller


class SalePoint:
    SELLER_NAMES_SEPARATOR = ', '

    def __init__(self, title: str):
        self.__title = title.capitalize()
        self.__sellers = []

    def create_seller(self, name: str) -> bool:
        is_valid = self.__is_valid_seller_name(name)

        if not is_valid:
            return False

        new_seller = Seller(name)
        self.__sellers.append(new_seller)
        return True

    def show_sellers(self):
        seller_names = []

        for seller in self.__sellers:
            seller_names.append(seller.get_name())
        if not seller_names:
            print(f'Точка: "{self.get_title()}", продавцы: на торговой точке продавцов нет')
        else:
            print(f'Точка: "{self.get_title()}", продавцы: {SalePoint.SELLER_NAMES_SEPARATOR.join(seller_names)}')

    def sell_product(self, seller_name: str, product: str, quantity: int) -> tuple[bool, str]:
        for seller in self.__sellers:
            if seller.get_name().lower() == seller_name.lower():
                success_result = seller.sell_product(product, quantity)

                if success_result:
                    return (True,
                            f'Продавец "{seller.get_name()}" продал "{product}" '
                            f'в количестве {quantity} на точке "{self.__title}"')
                else:
                    return False, 'Недостаточно товара или товар отсутствует'

        return False, 'Продавец не найден на этой точке'

    def delete_seller_by_name(self, name: str) -> bool:
        for seller in self.__sellers:
            if seller.get_name().lower() == name.lower():
                self.__sellers.remove(seller)
                return True

        return False

    def find_seller_by_name(self, name: str) -> Seller | None:
        for seller in self.__sellers:
            if seller.get_name().lower() == name.lower():
                return seller

        return None

    def get_title(self):
        return self.__title

    def get_sellers(self):
        return list(self.__sellers)

    def __is_valid_seller_name(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        if not name.strip():
            return False

        return True
