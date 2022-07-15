from hackaton.vievs import *
from hackaton.models import *

urlpatterns = [
    ('listing/', listing),
    ('create/', create),
    ('retrieve/', retrieve),
    ('update/', update),
    ('delete/', delete),
    ('comment/', comment),
]
