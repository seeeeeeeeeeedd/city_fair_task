class Seller:
    def __init__(self, name: str):
        is_valid = self.__is_valid_name(name)
        if is_valid:
            self.__name = name.title()
        else:
            self.__name = 'Имя неизвестно'

    def __is_valid_name(self, name: str) -> bool:
        if isinstance(name, str):
            if name.strip():
                return True
        return False

    def get_name(self) -> str:
        return self.__name
