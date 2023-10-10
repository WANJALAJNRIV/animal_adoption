from django.shortcuts import render, redirect
from .forms import AdoptionApplicationForm, AdoptionApplicationFormUser
from pets.models import Pet

def apply_for_adoption(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)

    if request.method == 'POST':
        form = AdoptionApplicationFormUser(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user  # Set the applicant to the current user
            application.pet = pet
            application.save()
            return redirect('public_pet_detail', pet_id=pet_id)

    else:
        form = AdoptionApplicationFormUser()

    return render(request, 'adoption_application/apply.html', {'form': form, 'pet': pet})



from django.shortcuts import render, redirect, get_object_or_404
from .models import AdoptionApplication
from .forms import AdoptionApplicationForm

def approve_application(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.application_status = 'Approved'
            form.save()
            return redirect('adoption_application_list')
    else:
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'adoption_application/approve.html', {'form': form, 'action': 'Approve'})

def reject_application(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.application_status = 'Rejected'
            form.save()
            return redirect('adoption_application_list')
    else:
        form = AdoptionApplicationForm(instance=application)
    return render(request, 'adoption_application/reject.html', {'form': form, 'action': 'Reject'})



from django.shortcuts import render
from .models import AdoptionApplication

def adoption_application_list(request):
    applications = AdoptionApplication.objects.all()
    return render(request, 'adoption_application/application_list.html', {'applications': applications})


from django.shortcuts import render, get_object_or_404
from .models import AdoptionApplication

def adoption_application_detail(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    return render(request, 'adoption_application/application_detail.html', {'application': application})



def public_application_detail(request, application_id):
    application = get_object_or_404(AdoptionApplication, pk=application_id)
    return render(request, 'adoption_application/user_application_detail.html' ,{'application': application})

