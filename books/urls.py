from django.conf.urls import url
from . import views

urlpatterns = [
    url('books', views.books_list, name='books_list'),
    url('', views.post_list, name='post_list'),
]
