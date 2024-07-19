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
    

    # U P D A T E
    def update_product(self, product):
        old_image_name = self.get_old_image_name(product.id)
        image_name = ImageHandler.update_image(old_image_name, product.image)
        sql = "UPDATE productsflask SET name=%s, price=%s, stock=%s, image_name=%s WHERE id=%s"
        self.dal.update(sql, (product.name, product.price, product.stock, image_name, product.id))
    
    def get_old_image_name(self, id):
        sql = "SELECT image_name FROM productsflask WHERE id=%s"
        result = self.dal.get_scalar(sql, (id,))
        return result["image_name"]

    def delete_product(self, id):
        #delete the product and the image from database
        image_name = self.get_old_image_name(id)
        ImageHandler.delete_image(image_name)
        sql = "DELETE FROM productsflask WHERE id=%s"
        return self.dal.delete(sql, (id,))


    def close(self):
        self.dal.close

    