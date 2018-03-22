from django.shortcuts import render, redirect
from django.views import View
from .models import Room, Reservation
from .forms import NewRoomForm, ReservationForm


class MainPageView(View):
    def get(self, request):
        rooms = Room.objects.all()
        ctx = {
            'rooms': rooms
        }
        return render(request, 'main.html', ctx)


class ShowRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, 'show.html', {'room': room})


class NewRoomView(View):
    def get(self, request):
        form = NewRoomForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = NewRoomForm(request.POST)
        if form.is_valid():
            r = Room()
            r.name = form.cleaned_data['name']
            r.number = form.cleaned_data['number']
            r.description = form.cleaned_data['description']
            r.save()
            return redirect('/')


class ModifyRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        form = NewRoomForm()
        ctx = {
            'room': room,
            'form': form
        }
        return render(request, 'form.html', ctx)

    def post(self, request, room_id):
        form = NewRoomForm(request.POST)
        room = Room.objects.get(pk=room_id)
        if form.is_valid():
            r = Room()
            r.name = form.cleaned_data['name']
            r.number = form.cleaned_data['number']
            r.description = form.cleaned_data['description']
            r.pk = room.id
            r.save()
            return redirect('/')


class DeleteRoomView(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        room.delete()
        return redirect('/')


class ReservationRoomView(View):
    def get(self, request, room_id):
        form = ReservationForm()
        room = Room.objects.get(pk=room_id)
        ctx = {
            'form': form,
            'room': room
        }
        return render(request, 'form.html', ctx)

    def post(self, request, room_id):
        form = ReservationForm(request.POST)
        room = Room.objects.get(pk=room_id)
        if form.is_valid():
            r = Reservation()
            r.date = form.cleaned_data['date']

