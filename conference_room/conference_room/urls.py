"""conference_room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from conference import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view(), name='main_page'),
    path('room/new', views.NewRoomView.as_view(), name='new_room'),
    path('room/modify/<int:room_id>', views.ModifyRoomView.as_view(), name='modify_room'),
    path('room/delete/<int:room_id>', views.DeleteRoomView.as_view(), name='delete_room'),
    path('room/<int:room_id>', views.ShowRoomView.as_view(), name='show_room'),
    # path('reservation', views.ReservationRoomView.as_view(), name='book_a_conference'),


]
