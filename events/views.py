from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from django.db.models import Q,Count
from django.contrib import messages
from events.models import Event, Category, Participant
from events.forms import Event_form, Category_Details, Participant_form
from django.utils import timezone


def organizer_dashboard(request):
    type=request.GET.get('type', 'all')
    tod=date.today()
    current_year=timezone.now().year
    counts=Event.objects.aggregate(total=Count('id'),
                                   completed=Count('id', filter=Q(due_date__lt=tod)),
                                   in_progress=Count('id', filter=Q(due_date__gt=tod)),
                                   events_today=Count('id', filter=Q(due_date=tod)))
    
       
    events=Event.objects.select_related('category').prefetch_related('participant')
   
    if type=='today':
        events=events.filter(due_date=tod)
    elif type=='completed':
        events=events.filter(due_date__lt=tod)
    elif type=='in_progress':
        events=events.filter(due_date__gt=tod)
    elif type=='all':
        events=events.all()
    
    context={'counts':counts,'events':events,'current_year':current_year}
    return render(request, 'body.html', context)



def create_event(request):
    current_year=timezone.now().year
    if request.method=='POST':
        category_form=Category_Details(request.POST)
        event_form=Event_form(request.POST)
        participant_form=Participant_form(request.POST)
        if category_form.is_valid() and event_form.is_valid() and participant_form.is_valid():

            category=category_form.save()

            event=event_form.save(commit=False)

            event.category=category

            event.save()
            participant=participant_form.save()
            participant.event.add(event)

            messages.success(request, 'EVENT CREATED SUCCESSFULLY')
            return redirect('create-event')
    else:
        category_form=Category_Details()
        event_form=Event_form()
        participant_form=Participant_form()

    context={'event_form':event_form, 'category_form':category_form,
              'participant_form':participant_form, 'current_year':current_year}
    return render(request, 'forms.html', context)
def update_event(request, id):
    event=Event.objects.get(id=id)
    current_year=timezone.now().year
    
    
    event_form=Event_form(instance=event)
    if event.category:
        category_form=Category_Details(instance=event.category)
    # if event.participant:
    #     participant_form=Participant_form(instance=event.participant)
    participant_form=Participant_form(instance=event)

    if request.method=='POST':
        category_form=Category_Details(request.POST, instance=event.category)
        event_form=Event_form(request.POST, instance=event)
        participant_form=Participant_form(request.POST)
        if category_form.is_valid() and event_form.is_valid() and participant_form.is_valid():

            category=category_form.save()

            event=event_form.save(commit=False)

            event.category=category

            event.save()
            participant=participant_form.save()
            participant.event.add(event)

            messages.success(request, 'EVENT UPDATED SUCCESSFULLY')
            return redirect('update_event', id)

    context={'event_form':event_form, 'category_form':category_form,
              'participant_form':participant_form, 'current_year':current_year}
    return render(request, 'forms.html', context)


    
def delete_event(request, id):
    
        event=Event.objects.get(id=id)
        event.delete()
        messages.success(request, 'Event Deleted Successfully')
        return redirect('organizer_dashboard', )




def home(request):
    current_year=timezone.now().year
    if request.method=='GET':
        return render(request, 'login.html', {'current_year':current_year})
    
def logedIn(request):
    if request.method=='POST':
        return redirect('organizer_dashboard')
    


