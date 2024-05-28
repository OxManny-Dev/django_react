
from django.urls import path, include

from . import views

urlpatterns = [
	path("",  views.index),
	# we can use the name parameter to give a name to the route
	# we can use that name in the reverse function to get the path
	path("<int:wildcard>", views.int_route, name="int_route"),
	path("<str:wildcard>", views.string_route, name="string_route"),
]