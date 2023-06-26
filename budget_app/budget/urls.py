from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),

]
