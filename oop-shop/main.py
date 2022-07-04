from models import User, Produkt, Comment
user1 = User("choybekov@gmail.com", "Beka", "M")
user1.resister("123", "123")
user1.login("123")
print(user1.is_authenticated)

product1 = Produkt("Iphone", "15", "343", "10")
comment1 = Comment(user1, product1, "Клаассс")
print(comment1)
