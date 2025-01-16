from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout', logout_view, name="logout"),
	path('wishlist/remove/<int:pk>/', wishlist_remove, name='wishlist_remove'),
    path('wishlist/', wishlist_view, name='wishlist_view'),
	path('wishlist_action/<int:pk>/', wishlist_action, name='wishlist_action'),
	path('search/', tour_search, name='tour_search'),
]
