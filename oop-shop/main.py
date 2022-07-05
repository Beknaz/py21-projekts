from shop.models import Product
from abstract.serializers import BaseSerializer

obj1 = Product("iphone", 234, "...", 3)
obj2 = Product("lenovo", 234, "...", 3)
obj3 = Product("Nokia", 234, "...", 3)
res = BaseSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint
pprint(res)
