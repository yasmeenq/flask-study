from utils.dal import DAL
from utils.image_handler import ImageHandler

class ProductsLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_products(self):
        sql = "SELECT * FROM productsflask"
        return self.dal.get_table(sql)
    
    def get_one_product(self, id):
        sql = "SELECT * FROM productsflask WHERE id = %s"
        return self.dal.get_scalar(sql, (id,))

    def add_product(self,product):
        image_name = ImageHandler.save_image(product.image)  #pass the image to function we created on imageHandler
        sql = "INSERT INTO productsflask(name,price,stock, image_name) VALUES(%s,%s,%s, %s)"
        return self.dal.insert(sql, (product.name, product.price, product.stock, image_name))

    def close(self):
        self.dal.close

    