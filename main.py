from seller import Seller
from sale_point import SalePoint
from city import City
from district import District

city1 = City('Краснодар')

district1 = District('Центральный')
district2 = District('Северный')

seller1 = Seller('Катя')
seller2 = Seller('')
seller3 = Seller('Иван')
seller4 = Seller('Настя')

point_of_sale1 = SalePoint('Азбука вкуса')
point_of_sale2 = SalePoint('Восток')
point_of_sale3 = SalePoint('Континент')

district1.add_sale_point(point_of_sale1)
district1.add_sale_point(point_of_sale2)
district2.add_sale_point(point_of_sale3)

city1.add_district(district1)
city1.add_district(district2)

point_of_sale1.add_seller(seller1)
point_of_sale2.add_seller(seller2)
point_of_sale3.add_seller(seller3)
point_of_sale3.add_seller(seller4)

city1.show_city_info()
