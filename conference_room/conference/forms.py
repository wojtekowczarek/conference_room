from django import forms
from .models import TAKEN, Room, Reservation


class NewRoomForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)
    number = forms.IntegerField(label='Room Number')
    taken = forms.ChoiceField(choices=TAKEN, label='Taken', widget=forms.Select)
    description = forms.CharField(label='Description', widget=forms.Textarea)


class ReservationForm(forms.Form):
    date = forms.CharField(label='Date', widget=forms.SelectDateWidget)
