from sale_point import SalePoint
from city import City

city = City('Краснодар')

commands = {
    '1': 'Добавить торговую точку',
    '2': 'Добавить продавца на точку',
    '3': 'Удалить продавца с точки',
    '4': 'Показать все точки и продавцов',
    '5': 'Добавить товар продавцу',
    '6': 'Купить товар',
    '0': 'Выйти из программы'
}

(ADD_SALE_POINT_COMMAND, ADD_SELLER_COMMAND, DELETE_SELLER_FROM_POINT_COMMAND,
 SHOW_ALL_POINTS_COMMAND, ADD_PRODUCT_TO_SELLER_COMMAND, BUY_PRODUCT_COMMAND,
 EXIT_COMMAND) = commands.keys()

is_program_running = True

while is_program_running:

    print()
    for number, command in commands.items():
        print(f'{number}: {command}')

    user_number = input('Выберете действие и укажите его номер: ')

    if user_number in commands:
        if user_number == ADD_SALE_POINT_COMMAND:
            user_sale_point = input('Введите название торговой точки: ').strip().lower()
            new_sale_point = SalePoint(user_sale_point)
            city.add_sale_point(new_sale_point)
        elif user_number == ADD_SELLER_COMMAND:
            user_sale_point_title = input('Укажите название торговой точки: ').strip().lower()

            current_sale_point = city.find_sale_point_by_title(user_sale_point_title)

            if not current_sale_point:
                print('Ошибка. Точка с таким названием не найдена')
            else:
                user_seller_name = input('Укажите имя продавца: ').strip().lower()
                success = current_sale_point.create_seller(user_seller_name)

                if success:
                    print('Продавец добавлен')
                else:
                    print('Ошибка. Некорректное имя продавца')
        elif user_number == REGISTER_SELLER_ON_POINT_COMMAND:
            user_seller_name = input('Укажите имя продавца: ').strip().lower()
            seller = city.find_seller_in_city(user_seller_name)
            if seller:
                user_sale_point_title = input('Укажите название торговой точки: ').strip().lower()
                sale_point = city.find_sale_point_by_title(user_sale_point_title)

                if sale_point:
                    city.register_seller_on_point(seller, sale_point)
                else:
                    print('Точка не найдена')
            else:
                print('Продавец не найден')

        elif user_number == DELETE_SELLER_FROM_POINT_COMMAND:
            user_sale_point_title = input('Укажите название точки для поиска продавца: ').lower().strip()
            sale_point = city.find_sale_point_by_title(user_sale_point_title)
            if sale_point:
                user_seller_name = input('Укажите имя продавца для удаления: ').strip().lower()
                seller = city.find_seller_on_points(user_seller_name)
                if seller:
                    sale_point.delete_seller(seller)
                else:
                    print()
                    print('Ошибка. Такого продавца на точке нет')
            else:
                print()
                print('Ошибка. Такой точки не существует')
        elif user_number == SHOW_ALL_POINTS_COMMAND:
            city.show_city_info()
        elif user_number == SHOW_ALL_SELLERS_COMMAND:
            city.show_all_sellers()
        elif user_number == ADD_PRODUCT_TO_SELLER_COMMAND:
            user_seller_name = input('Укажите имя продавца: ').strip()
            seller = city.find_seller_in_city(user_seller_name)

            if not seller:
                print('Продавец не найден')
            else:
                user_product = input('Укажите наименование товара: ').strip()
                user_quantity = input('Укажите количество для добавления: ').strip()

                if not user_quantity.isdigit():
                    print('Ошибка. Количество должно быть числом')
                else:
                    seller.add_product(user_product, int(user_quantity))
                    print('Товар успешно добавлен')
        elif user_number == BUY_PRODUCT_COMMAND:
            user_seller_name = input('Укажите имя продавца: ').strip()
            user_point_title = input('Укажите название торговой точки: ').strip()
            user_product = input('Укажите название товара: ').strip()
            user_quantity = input('Укажите количество: ').strip()

            if not user_quantity.isdigit():
                print('Количество должно быть числом')
            else:
                success, message = city.sell_product_on_point(user_seller_name, user_point_title,
                                                              user_product, int(user_quantity))
                print(message)
        elif user_number == EXIT_COMMAND:
            is_program_running = False
            print()
            print('Выход из программы')
    else:
        print()
        print('Неизвестная команда. Попробуйте снова')
