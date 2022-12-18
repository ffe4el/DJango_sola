from . import views
from django.urls import path, include

app_name = 'cal'
urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/new/delete', views.event_none),
	path('event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
    path('event/edit/(?P<event_id>\d+)/delete', views.event_delete, name='event_delete'),

]