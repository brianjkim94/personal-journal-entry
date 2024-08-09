from django.shortcuts import render, get_object_or_404, redirect
from .models import JournalEntry, Tag, Location
from .forms import JournalEntryForm

def entry_list(request):
    entries = JournalEntry.objects.all()
    return render(request, 'journal/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    return render(request, 'journal/entry_detail.html', {'entry': entry})

def entry_create(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/entry_form.html', {'form': form})

def entry_edit(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == "POST":
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=pk)
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'journal/entry_form.html', {'form': form})

def entry_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('entry_list')
    return render(request, 'journal/entry_confirm_delete.html', {'entry': entry})

def search_by_date(request):
    if 'date' in request.GET:
        date_str = request.GET['date']
        entries = JournalEntry.objects.filter(date=date_str)
    else:
        entries = JournalEntry.objects.none()
    return render(request, 'journal/entry_list.html', {'entries': entries})

def search_by_tag(request):
    if 'tag' in request.GET:
        tag_name = request.GET['tag']
        tag = Tag.objects.filter(name=tag_name).first()
        if tag:
            entries = JournalEntry.objects.filter(tags=tag)
        else:
            entries = JournalEntry.objects.none()
    else:
        entries = JournalEntry.objects.none()
    return render(request, 'journal/entry_list.html', {'entries': entries})
