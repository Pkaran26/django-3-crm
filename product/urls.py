from django.urls import path
from . import views

urlpatterns = [
    path('', views.SimpleView.as_view(), name='book_simple'),

    path('list/', views.BookListView.as_view(), name='book_list'),
    path('list2/', views.BookListTemplateView.as_view(), name='book_list_template'),
    path('list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('list/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('list/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
