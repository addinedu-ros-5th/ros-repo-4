import random

# 품목 클래스
class Item:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"Item({self.item_id}, {self.name}, {self.quantity})"

# OrderListNode 클래스
class OrderList:
    def __init__(self):
        self.items = self.initialize_items()

    def initialize_items(self):
        # 18개의 품목 초기화
        items = [
            Item('P01', "Toothpaste", random.randint(1, 100)),
            Item('P02', "Shampoo", random.randint(1, 100)),
            Item('P03', "Soap", random.randint(1, 100)),
            Item('P04', "Hand Sanitizer", random.randint(1, 100)),
            Item('P05', "Laundry Detergent", random.randint(1, 100)),
            Item('P06', "Dish Soap", random.randint(1, 100)),
            Item('P07', "Paper Towels", random.randint(1, 100)),
            Item('P08', "Toilet Paper", random.randint(1, 100)),
            Item('P09', "Facial Tissues", random.randint(1, 100)),
            Item('P10', "Trash Bags", random.randint(1, 100)),
            Item('P11', "Sponges", random.randint(1, 100)),
            Item('P12', "Cleaning Spray", random.randint(1, 100)),
            Item('P13', "Batteries", random.randint(1, 100)),
            Item('P14', "Light Bulbs", random.randint(1, 100)),
            Item('P15', "Umbrella", random.randint(1, 100)),
            Item('P16', "Notebook", random.randint(1, 100)),
            Item('P17', "Pen", random.randint(1, 100)),
            Item('P18', "Basketball", random.randint(1, 100))
        ]
        return items

    def get_random_order_list(self):
        # 10~18개의 랜덤 품목 선택
        num_items = random.randint(6, 10)
        random_items = random.sample(self.items, num_items)
        # 선택된 품목의 수량도 랜덤으로 설정
        for item in random_items:
            item.quantity = random.randint(1, 50)
        return random_items

    def print_order_list(self, order_list):
        for item in order_list:
            print(f"Item ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}")
        print(f"Total items: {len(order_list)}")  # 출력된 항목의 개수를 출력


