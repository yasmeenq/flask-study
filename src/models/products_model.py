
class ProductModel:
    def __init__(self, id, name, price, stock, image):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image

    def validate_insert(self):
        if not self.name: return "missing name"
        if not self.price: return "missing price"
        if not self.stock: return "missing stock"
        # if not self.image: return "missing image"
        if len(self.name) < 2 or len(self.name) > 100: return "name must be 2-100"
        if float(self.price) < 0 or float(self.price) > 10000: return "price must be 0-1000"
        if int(self.stock) < 0 or int(self.stock) > 10000: return "stock must be 0-1000"
        return None #if there's no error return nth

    def validate_edit(self):
        if not self.id: return "missing id"
        if not self.name: return "missing name"
        if not self.price: return "missing price"
        if not self.stock: return "missing stock"
        # if not self.image: return "missing image"
        if len(self.name) < 2 or len(self.name) > 100: return "name must be 2-100"
        if float(self.price) < 0 or float(self.price) > 10000: return "price must be 0-1000"
        if int(self.stock) < 0 or int(self.stock) > 10000: return "stock must be 0-1000"
        return None