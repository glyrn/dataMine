# 图书基本类
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"书名：{self.title}")
        print(f"作者：{self.author}")
        print(f"价格：￥{self.price:.2f}")

# 平装书，继承自书
class PaperbackBook(Book):
    def __init__(self, title, author, price, pages):
        super().__init__(title, author, price)
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"类型：平装")
        print(f"页数：{self.pages} 页")

# 精装书
class HardcoverBook(Book):
    def __init__(self, title, author, price, weight):
        super().__init__(title, author, price)
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"类型：精装")
        print(f"重量：{self.weight} 磅")


class Library:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book, quantity):
        if book.title in self.inventory:
            self.inventory[book.title] += quantity
        else:
            self.inventory[book.title] = quantity

    def checkout_book(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            print(f"借出 {quantity} 本《{title}》。")
        else:
            print(f"抱歉，《{title}》暂时无法借阅。")

    def display_inventory(self):
        print("图书馆库存:")
        for title, quantity in self.inventory.items():
            print(f"《{title}》: {quantity} 本")

# 创建一些书籍
book1 = PaperbackBook("Python编程", "Eric", 29, 544)
book2 = HardcoverBook("程序设计", "Don", 79, 3.2)
book3 = PaperbackBook("数据科学", "Lil", 24, 384)

# 创建图书馆

library = Library()

while True:
    print("\n请选择操作：")
    print("1. 添加书籍")
    print("2. 借阅书籍")
    print("3. 显示库存")
    print("4. 退出")

    choice = input("请输入选项: ")

    if choice == "1":
        title = input("请输入书名: ")
        author = input("请输入作者: ")
        price = float(input("请输入价格: "))
        book_type = input("请输入书籍类型（平装/精装）: ")
        if book_type == "平装":
            pages = int(input("请输入页数: "))
            book = PaperbackBook(title, author, price, pages)
        elif book_type == "精装":
            weight = float(input("请输入重量: "))
            book = HardcoverBook(title, author, price, weight)
        else:
            print("无效的书籍类型。")
            continue

        quantity = int(input("请输入添加的数量: "))
        library.add_book(book, quantity)
        print(f"成功添加 {quantity} 本《{title}》到库存。")

    elif choice == "2":
        title = input("请输入要借阅的书名: ")
        quantity = int(input("请输入借阅数量: "))
        library.checkout_book(title, quantity)

    elif choice == "3":
        library.display_inventory()

    elif choice == "4":
        print("感谢使用图书馆系统。")
        break

    else:
        print("无效选项，请重新输入。")
