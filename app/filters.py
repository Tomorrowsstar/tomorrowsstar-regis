from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='姓名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('school', 'school'),
        ),
        field_labels={
            'name': '姓名',
            'school': '學校',
        },
        label='順序'
    )

    class Meta:
        model = Item
        fields = ('name', 'school', 'memo',)
