from .models import Pet
from .forms import PetForm, PetSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count


def search_pets(request):
    pets = Pet.objects.filter(adoption_status='Available')
    if request.method == 'GET':
        form = PetSearchForm(request.GET)
        if form.is_valid():
            species = form.cleaned_data.get('species')
            breed = form.cleaned_data.get('breed')
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            adoption_fee = form.cleaned_data.get('adoption_fee')
            suburb = form.cleaned_data.get('suburb')
            state = form.cleaned_data.get('state')

            if species:
                pets = pets.filter(species__icontains=species)
            if breed:
                pets = pets.filter(breed__icontains=breed)
            if age:
                pets = pets.filter(age=age)
            if gender:
                pets = pets.filter(gender=gender)
            if adoption_fee:
                pets = pets.filter(adoption_fee=adoption_fee)
            if suburb:
                pets = pets.filter(suburb__icontains=suburb)
            if state:
                pets = pets.filter(state__icontains=state)

    grouped_pets = pets.values('species', 'breed').annotate(total=Count('id'))

    return render(request, 'search_pets.html', {'grouped_pets': grouped_pets, 'form': form})


def public_pets_view(request):
    pets = Pet.objects.filter(adoption_status='Available')
    return render(request, 'pets/public_pet_list.html', {'pets': pets})


def public_pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/public_pet_detail.html', {'pet': pet})


@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet has been added successfully.')
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})


@login_required
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})



@login_required
def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet details have been updated successfully.')
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form})

@login_required
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        pet.delete()
        messages.success(request, 'Pet details have been deleted successfully.')
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})
