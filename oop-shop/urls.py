from shop.views import *
from account.views import *

urlpatterns = [
    ('products/', product_list),
    ('product-create/', product_create),
    ('product-detail/', product_detail),
    ('product-update/', product_update),
    ('product-delete/', product_delete),
    
    ('category-create/', category_create),
    ('comment-create/', create_comment)
]
