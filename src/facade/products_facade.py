from logic.products_logic import ProductsLogic

class ProductsFacade:
    def __init__(self):
        self.logic = ProductsLogic()

    def get_all_products(self):
        return self.logic.get_all_products()
    
    def get_one_product(self, id):
        return self.logic.get_one_product(id)
    
    def close(self):
        self.logic.close()