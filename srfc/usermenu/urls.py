from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import MenuView, TableView, index
from .models import Info

urlpatterns = [
    path(r'', index, name='index'),
    path(r'menu/', login_required(MenuView.as_view()), name='menu'),
    ]

for table_name in Info.get_table_names():
    urlpatterns.append(path(f'{table_name}/',
                            login_required(TableView.create_view(table_name).as_view()),
                            name=table_name))
