import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name="note", lookup_expr='icontains')

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(OrderFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['product'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['start_date'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['end_date'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['note'].field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
