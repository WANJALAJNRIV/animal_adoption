from .models import Pet
from .forms import PetForm, PetSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from users.decorators import pet_manager_or_admin_required



def search_pets(request):
    """
    View for searching and filtering available pets.

    This view allows users to search for available pets based on various criteria such as species, breed, age, gender,
    adoption fee, suburb, and state.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with search results.
    :rtype: HttpResponse
    """
    pets = Pet.objects.filter(adoption_status='Available')
    form = PetSearchForm(request.GET)

    if request.method == 'GET':
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
    """
    View for displaying available pets to the public.

    This view allows any user, including anonymous users, to view a list of available pets and apply filters.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with the list of available pets.
    :rtype: HttpResponse
    """
    pets = Pet.objects.filter(adoption_status='Available')
    form = PetSearchForm(request.GET)

    if request.method == 'GET':
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
    return render(request, 'pets/public_pet_list.html', {'pets': pets, 'grouped_pets': grouped_pets, 'form': form})


def public_pet_detail(request, pet_id):
    """
    View for displaying pet details publicly.

    This view allows any user, including anonymous users, to view the details of a specific pet.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pet_id: The ID of the pet to be displayed.
    :type pet_id: int
    :return: A rendered HTML template with the pet's details.
    :rtype: HttpResponse
    """
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/public_pet_detail.html', {'pet': pet})


@login_required
@pet_manager_or_admin_required
def pet_create(request):
    """
    View for creating a new pet.

    This view allows users with the 'pet_manager' or 'admin' role to create a new pet by submitting a form.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with the pet creation form or a redirect response.
    :rtype: HttpResponse
    """

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
@pet_manager_or_admin_required
def pet_list(request):
    """
    View for listing all pets.

    This view allows users with the 'pet_manager' or 'admin' role to view a list of all pets.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML template with the list of pets.
    :rtype: HttpResponse
    """

    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
@pet_manager_or_admin_required
def pet_detail(request, pet_id):
    """
    View for displaying pet details.

    This view allows users with the 'pet_manager' or 'admin' role to view the details of a specific pet.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pet_id: The ID of the pet to be displayed.
    :type pet_id: int
    :return: A rendered HTML template with the pet's details.
    :rtype: HttpResponse
    """

    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


@login_required
@pet_manager_or_admin_required
def pet_update(request, pet_id):
    """
    View for updating pet details.

    This view allows users with the 'pet_manager' or 'admin' role to update a pet's details.
    If the request method is POST and the form is valid, the pet's details are updated, and a success message is displayed.
    If the request method is GET, the pet's details are displayed in a form for editing.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pet_id: The ID of the pet to be updated.
    :type pet_id: int
    :return: A rendered HTML template with the form or a redirect response.
    :rtype: HttpResponse
    """

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
@pet_manager_or_admin_required
def pet_delete(request, pet_id):
    """
    View for deleting a pet.

    This view allows users with the 'pet_manager' or 'admin' role to delete a pet's details. 
    Users must confirm the deletion via a form. If the request method is POST and the form is valid,
    the pet's details are deleted, and a success message is displayed. If the request method is GET,
    the confirmation form is shown.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pet_id: The ID of the pet to be deleted.
    :type pet_id: int
    :return: A rendered HTML template or a redirect response.
    :rtype: HttpResponse
    """

    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        pet.delete()
        messages.success(request, 'Pet details have been deleted successfully.')
        return redirect('pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})
