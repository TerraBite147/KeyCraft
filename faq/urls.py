from django.urls import path
from .views import faq_list_view, add_faq_view, edit_faq_view, delete_faq_view

urlpatterns = [
    path('', faq_list_view, name='faq_list'),
    path('add/', add_faq_view, name='add_faq'),
    path('edit/<int:faq_id>/', edit_faq_view, name='edit_faq'),
    path('delete/<int:faq_id>/', delete_faq_view, name='delete_faq'),
]
