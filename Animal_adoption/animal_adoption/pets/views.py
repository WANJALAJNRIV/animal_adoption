# views.py
from django.shortcuts import render
from .models import Pet
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Pet


def public_pets_view(request):
    pets = Pet.objects.all()
    return render(request, 'pets/public_pet_list.html', {'pets': pets})





def public_pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/public_pet_detail.html', {'pet': pet})





def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})



def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})

# views.py
from django.shortcuts import render, redirect
from .forms import PetForm

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForm

def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form})
# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Pet

def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})
