
from django.urls import path
from . import views

app_name = 'CanteenApp'

urlpatterns = [
    path('', views.Home, name='homeurl'),
    path('order/', views.order, name='orderurl'),
    path('order_summary/', views.order_summary, name='summaryurl'),
    path('update/<int:item_id>/', views.update, name='updateurl'),
    path('delete/<int:item_id>/', views.delete, name='deleteurl'),
]

