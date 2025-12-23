from django.urls import path
from events.views import create_event, organizer_dashboard, update_event, delete_event, home, logedIn

urlpatterns = [
    path("form/", create_event,name='create-event'),
    path("organizer-dashboard/",organizer_dashboard, name='organizer_dashboard' ),
    path("update-event/<int:id>/",update_event, name='update_event'),
    path("delete-event/<int:id>/",delete_event, name='delete_event'),
    path("logedIn/", logedIn, name='loged'),
    path("home/", home, name='home'),
]
