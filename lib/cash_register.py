class CashRegister:
    def __init__(self, discount=0):
        '''Initialize the CashRegister with optional discount.'''
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = (0, 0)  # To keep track of the last transaction (price, quantity)
    
    def add_item(self, title, price, quantity=1):
        '''Add an item to the register and update the total.'''
        # Calculate the total price for this item
        item_total = price * quantity
        
        # Update total
        self.total += item_total
        
        # Add items to the items list
        self.items.extend([title] * quantity)
        
        # Update last transaction (price of last item, quantity of last item)
        self.last_transaction = (price, quantity)
    
    def apply_discount(self):
        '''Apply discount to the total, if any.'''
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        '''Void the last transaction and update the total.'''
        if self.last_transaction != (0, 0):
            last_price, last_quantity = self.last_transaction
            self.total -= (last_price * last_quantity)
            
            # Remove the last items from the items list
            for _ in range(last_quantity):
                self.items.pop()
            
            # Reset last transaction
            self.last_transaction = (0, 0)