class Product:

    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0

    def set_discount_in_percent(self, discount_in_percent):
        self.__discount_in_percent = discount_in_percent

    def get_current_price(self):
        result = self.__price * (1 - self.__discount_in_percent / 100)
        return round(result, 2)

    def is_category(self, category):
        return  self.__category == category

    def __str__(self):
        return f"{self.__name} ({self.__category}) {self.get_current_price()}"

def show_product(products):
    for p in products:
        print(p)

def special_offer(products, category, discount_in_percent):
    for p in products:
        if p.is_category(category):
            p.set_discount_in_percent(discount_in_percent)

products = []
products.append(Product("mleko", "spożywcze", 3.99))
products.append(Product("masło", "spożywcze", 6.56))
products.append(Product("jogurt", "spożywcze", .99))
products.append(Product("płyn do naczyń", "chemia", 4.50))
show_product(products)

special_offer(products, "chemia", 30)
print()
show_product(products)