
class Item:
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"



class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total = 0.0

    def add_item(self, item: Item):
        self.items.append(item)
        self.total += item.price
        print(f"Додано {item.name} за ${item.price:.2f} до замовлення")

    def remove_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                self.total -= item.price
                print(f"Видалено {item_name} з замовлення")
                return
        print(f"Товар '{item_name}' не знайдено")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        if not self.items:
            return "Замовлення порожнє."
        item_list = "\n".join(str(item) for item in self.items)
        return f"Замовлення для {self.customer.name}:\n{item_list}\nЗагальна сума: ${self.calculate_total():.2f}"



class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def place_order(self, order: Order):
        if order.items:
            self.orders.append(order)
            print(f"Замовлення для {self.name} оформлено на суму: ${order.calculate_total():.2f}")
        else:
            print("Замовлення порожнє, додайте товари перед оформленням")

    def view_orders(self):
        if not self.orders:
            return f"У {self.name} ще немає замовлень."
        return "\n\n".join(str(order) for order in self.orders)


def main():
    customer = Customer("astolfo")
    coffee = Item("Кава", 2.5)
    croissant = Item("Круасан", 1.75)
    sandwich = Item("Сендвіч", 4.0)

    order = Order(customer)
    order.add_item(coffee)
    order.add_item(croissant)
    order.add_item(sandwich)
    order.remove_item("Круасан")
    customer.place_order(order)

    print("\nІсторія замовлень:")
    print(customer.view_orders())

if __name__ == "__main__":
    main()
