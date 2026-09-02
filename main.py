from seller import Seller
from point_of_sale import SalePoint

seller1 = Seller('Катя')
seller2 = Seller('')

point_of_sale1 = SalePoint('Азбука вкуса')
point_of_sale2 = SalePoint('Восток')

point_of_sale1.add_seller(seller1)
point_of_sale1.add_seller(seller2)
point_of_sale2.add_seller(seller1)

point_of_sale1.show_sellers()
point_of_sale2.show_sellers()
