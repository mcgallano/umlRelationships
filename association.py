class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []


class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        # Establish structural bi-directional link
        customer.orders.append(self)


if __name__ == "__main__":
    alice = Customer("Alice")
    order_1 = Order(101, alice)
    order_2 = Order(102, alice)

    print(f"Customer Profile: {alice.name}")
    for order in alice.orders:
        print(f"  Order ID: {order.order_id}")
    print(f"Order #101 lookup -> Owned by customer: {order_1.customer.name}")