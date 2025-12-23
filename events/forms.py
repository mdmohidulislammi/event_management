from django import forms
from events.models import Event, Category, Participant

INPUT_CLASS = (
    "w-full px-4 py-3 rounded-lg border border-gray-300 "
    "focus:outline-none focus:ring-2 focus:ring-green-400 "
    "focus:border-green-400"
     "bg-white text-black placeholder-gray-200 ")


class Participant_form(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Enter participant name'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Enter email address'}),
        }


class Event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'due_date', 'time', 'location']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Event name'}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Event description',
                'rows': 4}),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': INPUT_CLASS}),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': INPUT_CLASS}),
            'location': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Event location'}),
        }


class Category_Details(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Category_name', 'description']
        widgets = {
            'Category_name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Category name'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Category description',
                'rows': 3
            }),
        }
