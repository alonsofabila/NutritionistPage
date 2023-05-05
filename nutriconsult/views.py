from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AssistantRegistrationForm, NutritionistRegistrationForm, ClientRegistrationForm
from .models import Client


# Create your views here.
def dashboard(request):
    all_clients = Client.objects.all
    return render(request, 'nutriconsult/dashboard.html', {'all_clients': all_clients})


@login_required
def assistant_register(request):
    if request.method == 'POST':
        assistant_form = AssistantRegistrationForm(request.POST)
        if assistant_form.is_valid():
            new_user = assistant_form.save(commit=False)
            new_user.set_password(assistant_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'nutriconsult/register_done.html', {'new_user': new_user})
    else:
        assistant_form = AssistantRegistrationForm()
        return render(request, 'nutriconsult/register_assistant.html', {'assistant_form': assistant_form})


@login_required
def nutritionist_register(request):
    if request.method == 'POST':
        nutritionist_form = NutritionistRegistrationForm(request.POST)
        if nutritionist_form.is_valid():
            new_user = nutritionist_form.save(commit=False)
            new_user.set_password(nutritionist_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'nutriconsult/register_done.html', {'new_user': new_user})
    else:
        nutritionist_form = NutritionistRegistrationForm()
        return render(request, 'nutriconsult/register_nutritionist.html', {'nutritionist_form': nutritionist_form})


@login_required
def client_register(request):
    if request.method == 'POST':
        client_form = ClientRegistrationForm(request.POST)
        if client_form.is_valid():
            new_client = client_form.save(commit=False)
            new_client.save()
            return render(request, 'nutriconsult/register_client_done.html', {'new_client': new_client})
    else:
        client_form = ClientRegistrationForm()
        return render(request, 'nutriconsult/register_client.html', {'client_form': client_form})
