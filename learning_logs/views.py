from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


def index(request):
    """The homepage for learning logs"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """All the topics in our database"""
    topics = Topic.objects.order_by('date_added')
    template = 'learning_logs/topics.html'
    context = {'topics': topics}
    return render(request, template, context)


@login_required
def topic(request, pk):
    """Specific topic that the user request"""
    topic = Topic.objects.get(id=pk)
    entries = topic.entry_set.order_by('-date_added')
    template = 'learning_logs/topic.html'
    context = {'topic': topic, 'entries': entries}
    return render(request, template, context)


@login_required
def new_topic(request):
    #Add a new topic
    if request.method != 'POST':
       #create a blank form
       form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    template = 'learning_logs/new_topic.html'
    return render(request, template, context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
       form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    template = 'learning_logs/new_entry.html'
    return render(request, template, context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
       form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    template = 'learning_logs/edit_entry.html'
    return render(request, template, context)
