class Car():
    objects = []
    _id = 0
    def __init__(self, marka, model, yers, valume, color, kuzov, probeg, price):
        self.id = Car._id
        self.marka = marka
        self.model = model
        self.yers = yers
        self.valume = valume
        self.color = color
        self.kuzov = kuzov
        self.probeg = probeg
        self.price = price
        Car.objects.append(self)
        Car._id += 1

    @property
    def comments(self):
        return [c for c in Comment.objects if c.product == self]
class Comment:
    objects = []

    def __init__(self, product, body):
        from datetime import datetime
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)