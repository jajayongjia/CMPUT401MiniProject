from django.urls import path

from . import views

urlpatterns = [
    path('data', views.get_all_data, name='fetch all'),
    path('distData', views.getDistinctValue, name="fetch Year range"),
    path('getLocation', views.getTuitionForTwoLocation, name="fetch two locations")
]
