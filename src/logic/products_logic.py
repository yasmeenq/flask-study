from utils.dal import DAL

class ProductsLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_products(self):
        sql = "SELECT * FROM productsflask"
        return self.dal.get_table(sql)
    
    def get_one_product(self, id):
        sql = "SELECT * FROM productsflask WHERE id = %s"
        return self.dal.get_scalar(sql, (id,))
    
    def close(self):
        self.dal.close

    