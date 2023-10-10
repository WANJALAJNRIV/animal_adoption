from django.shortcuts import render, redirect, get_object_or_404
from .models import Shelter
from .forms import ShelterForm

def shelter_list(request):
    shelters = Shelter.objects.all()
    return render(request, 'shelters/shelter_list.html', {'shelters': shelters})

def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    return render(request, 'shelters/shelter_detail.html', {'shelter': shelter})

def shelter_create(request):
    if request.method == 'POST':
        form = ShelterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shelter_list')
    else:
        form = ShelterForm()
    return render(request, 'shelters/shelter_form.html', {'form': form})

def shelter_update(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)

    if request.method == 'POST':
        form = ShelterForm(request.POST, instance=shelter)
        if form.is_valid():
            form.save()
            return redirect('shelter_detail', shelter_id=shelter.id)
    else:
        form = ShelterForm(instance=shelter)

    return render(request, 'shelters/shelter_form.html', {'form': form, 'shelter': shelter})


def shelter_delete(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    if request.method == 'POST':
        shelter.delete()
        return redirect('shelter_list')
    return render(request, 'shelters/shelter_confirm_delete.html', {'shelter': shelter})
