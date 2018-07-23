from controlcenter import Dashboard, widgets
from products.models import Products


class ModelItemList(widgets.ItemList):
    model = Products
    list_display = ('name', 'price')


class MyDashboard(Dashboard):
    # title = 'Products',
    widgets = (
        widgets.Group([ModelItemList, ModelItemList], width=widgets.LARGER, height=300),
        # ModelItemList,
    )