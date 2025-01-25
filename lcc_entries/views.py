from django.shortcuts import render
from django.http import HttpResponse
from .models import LCCComp, LCCEntry, LCCCreator

def index(request):
    all_comps = LCCComp.objects.order_by("year")
    context = {"all_comps": all_comps}
    return render(request, "lcc_entries/index.html", context)

def comp(request, comp_name):
    try:
        comp_full_name = LCCComp.objects.get(name=comp_name)
        get_entries = LCCEntry.objects.filter(competition_name=comp_full_name)
        context = {
            "current_comp_entries": get_entries,
            "comp_full_name": comp_full_name,
        }
        return render(request, "lcc_entries/comp.html", context)
    except LCCComp.DoesNotExist:
        return HttpResponse("Competition not found", status=404)

def entry(request, comp_name, slug):
    try:
        comp_full_name = LCCComp.objects.get(name=comp_name)
        entry = LCCEntry.objects.get(competition_name=comp_full_name, slug=slug)
        same_creator_entries = LCCEntry.objects.filter(creator=entry.creator).exclude(id=entry.id)
        context = {
            "entry": entry,
            "comp_full_name": comp_full_name,
            "same_creator_entries": same_creator_entries,
        }
        return render(request, "lcc_entries/entry.html", context)
    except (LCCComp.DoesNotExist, LCCEntry.DoesNotExist):
        return HttpResponse("Entry not found", status=404)

def creator(request, creator_name):
    return HttpResponse(f"This is the page for {creator_name}!")

def search(request):
    return HttpResponse("This is the search page!")

def about(request):
    return HttpResponse("This is the about page!")