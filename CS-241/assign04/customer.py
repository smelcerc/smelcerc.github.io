class Customer:

    def __init__(self):
        self.id = ''
        self.name = ''
        self.orders = []

    def get_order_count(self):
        return len(self.orders)

    def get_total(self):
        self.total = 0
        for order in self.orders:
            self.total += order.total
        return self.total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print(f"Summary for customer '{self.id}':")
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: ${self.get_total():.2f}')

    def display_receipts(self):
        print(f"Detailed receipts for customer '{self.id}':")
        print(f'Name: {self.name}')
        for order in self.orders:
            print(f'\nOrder: {order.id}')
            for product in order.products:
                print(f'{product.name} ({product.quantity}) - ${product.quantity * product.price:.2f}')
            print(f'Subtotal: ${order.subtotal:.2f}')
            print(f'Tax: ${order.tax:.2f}')
            print(f'Total: ${order.total:.2f}')

