#-------------------------------------product
class Product:
    def __init__(self,code="",name="",price=0.0,quantity=0,category="",description=""):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description

    def to_dict(self):
        return self.__dict__
        
