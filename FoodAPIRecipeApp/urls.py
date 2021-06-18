from django.urls import path
from .views import fetch_recipe_from_keyword
urlpatterns = [
	path('foods/',fetch_recipe_from_keyword,name='fetch_recipe_from_keyword'),
]