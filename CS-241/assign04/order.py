class Order:
    
    def __init__(self):
        self.id = ''
        self.products = []
        self.subtotal = 0
        self.tax = 0
        self.total = 0

    def get_subtotal(self):
        self.subtotal = 0
        for product in self.products:
            self.subtotal += product.price * product.quantity
        self.get_tax()

    def get_tax(self):
        self.tax = self.subtotal * 0.065
        self.get_total()

    def get_total(self):
        self.total = self.subtotal + self.tax

    def add_product(self, product):
        self.products.append(product)
        self.get_subtotal()

    def display_receipt(self):
        print(f'Order: {self.id}')
        for product in self.products:
            print(f'{product.name} ({product.quantity}) - ${product.quantity * product.price:.2f}')
        print(f'Subtotal: ${self.subtotal:.2f}')
        print(f'Tax: ${self.tax:.2f}')
        print(f'Total: ${self.total:.2f}')