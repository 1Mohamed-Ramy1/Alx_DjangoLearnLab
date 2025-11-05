from django.urls import path
from . import views

urlpatterns = [
    # مؤقتًا خليه فاضي أو حط صفحة تجريبية
    path('', views.index, name='index'),
]
