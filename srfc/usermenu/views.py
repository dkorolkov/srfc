from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from usermenu.models import Menu, Info


def index(request):
    return redirect(reverse('menu'))


class MenuView(ListView):
    model = Menu
    template_name = "usermenu/menu.html"

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(users__in=(user,))
    

class TableView(ListView):
    template_name = "usermenu/table.html"

    @classmethod
    def create_view(cls, table_name):
        model = Info.get_table(table_name)
        return type(table_name.capitalize(), (cls,), {'model': model})

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.select_related('region').filter(region__users__in=(user,))
