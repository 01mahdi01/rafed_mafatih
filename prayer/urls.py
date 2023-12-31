from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name="home_page"),
    path('create/prayer', views.create_prayer_page, name="create_prayer_page"),
    path('create/categoty', views.create_category_page, name="create_category_page"),
    path('prayer/list', views.create_prayer, name="create_prayer"),
    path('category/list', views.create_category, name="create_category"),
    path('edit/prayer/<int:id>', views.edit_prayer_page, name="edit_prayer_page"),
    path('edit/prayer/update/<int:id>', views.update_prayer, name="update_prayer"),
    path('edit/category/<int:id>', views.edit_category_page, name="edit_category_page")
]
