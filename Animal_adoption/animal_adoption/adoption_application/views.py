from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdoptionApplicationForm, AdoptionApplicationFormUser
from .models import AdoptionApplication
from pets.models import Pet
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.decorators import application_manager_or_admin_required


@login_required
def apply_for_adoption(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)

    if request.method == 'POST':
        form = AdoptionApplicationFormUser(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user  # Set the applicant to the current user
            application.pet = pet
            application.save()
            messages.success(request, 'Thank you for applying for adoption! Your application has been received.')
            return redirect('public_pet_detail', pet_id=pet_id)

    else:
        form = AdoptionApplicationFormUser()

    return render(request, 'adoption_application/apply.html', {'form': form, 'pet': pet})



@login_required
@application_manager_or_admin_required
def approve_application(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.application_status = 'Approved'
            form.save()

            adopted_pet = get_object_or_404(Pet, pk=application.pet.id)
            adopted_pet.adoption_status = 'Adopted'
            adopted_pet.adopter = application.applicant
            adopted_pet.save()

            # Get all other related applications for the same pet with 'Pending' status
            related_applications = AdoptionApplication.objects.filter(
                pet=application.pet,
                application_status='Pending'
            )

            # Update related applications to 'Rejected' with manager comments
            for related_application in related_applications:
                related_application.application_status = 'Rejected'
                related_application.manager_comments = 'The pet has already been adopted'
                related_application.save()
            messages.success(request, 'Adoption application approved successfully.')
            return redirect('adoption_application_list')
    else:
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'adoption_application/approve_application.html', {'form': form, 'action': 'Approve'})

@login_required
@application_manager_or_admin_required
def reject_application(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.application_status = 'Rejected'
            form.save()
            messages.success(request, 'Adoption application has been rejected.')
            return redirect('adoption_application_list')
    else:
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'adoption_application/reject_application.html', {'form': form, 'action': 'Reject'})



@login_required
@application_manager_or_admin_required
def adoption_application_list(request):

    applications = AdoptionApplication.objects.filter(application_status='Pending')

    grouped_applications = {}
    for application in applications:
        pet = application.pet
        if pet not in grouped_applications:
            grouped_applications[pet] = []
        grouped_applications[pet].append(application)


    return render(request, 'adoption_application/application_list.html', {'grouped_applications':grouped_applications})


@login_required
@application_manager_or_admin_required
def adoption_application_detail(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    return render(request, 'adoption_application/application_detail.html', {'application': application})



def public_application_detail(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    return render(request, 'adoption_application/user_application_detail.html' ,{'application': application})


@login_required
def pet_adoption_applications(request, pet_id):

    pet_object = get_object_or_404(Pet, pk=pet_id)

    pet_applications = AdoptionApplication.objects.filter(pet=pet_object, application_status='Pending')

    return render(request, 'adoption_application/adoption_applications_pet.html', {'pet_applications': pet_applications})

