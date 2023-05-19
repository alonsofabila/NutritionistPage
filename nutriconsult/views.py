from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AssistantRegistrationForm, NutritionistRegistrationForm, ClientRegistrationForm, MakeConsult
from .models import Client, Consult
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def dashboard(request):
    if 'patient' in request.GET:
        patient = request.GET['patient']
        all_clients = Client.objects.filter(Q(first_name__icontains=patient) | Q(last_name__icontains=patient))
    else:
        all_clients = Client.objects.filter(is_active=1).order_by('last_name')
    all_user = User.objects.all()
    paginator = Paginator(all_clients, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'nutriconsult/dashboard.html', {'all_clients': all_clients, 'all_user': all_user,
                                                           'page_obj': page_obj})


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


@login_required
def make_consult(request):
    if request.method == 'POST':
        consult_form = MakeConsult(request.POST)
        if consult_form.is_valid():
            new_consult = consult_form.save(commit=False)
            new_consult.save()
            return render(request, 'nutriconsult/consult_done.html', {'new_consult': new_consult})
    else:
        consult_form = MakeConsult()
        return render(request, 'nutriconsult/make_consult.html', {'consult_form': consult_form})


@login_required
def patient_details(request, client_id=None):
    client = get_object_or_404(Client, pk=client_id)
    all_client = Client.objects.all()
    all_consult = Consult.objects.filter(client=client).order_by('consult_date')

    bmi = round(float(client.weight)/(float(client.height)**2), 2)

    previous_consult = all_consult.last()
    if previous_consult:
        current_bmi = round(float(previous_consult.new_weight)/(float(client.height)**2), 2)
    else:
        current_bmi = None

    return render(request, 'nutriconsult/client_detail.html', {'client': client, 'all_client': all_client,
                                                               'all_consult': all_consult, 'bmi': bmi,
                                                               'current_bmi': current_bmi})


def patient_progress(request):
    client_id = request.GET.get('client_id')
    client = get_object_or_404(Client, id=client_id)
    consult = Consult.objects.filter(client=client).order_by('consult_date')

    bmi = round(float(client.weight)/(float(client.height)**2), 2)
    previous_consult = consult.last()
    if previous_consult:
        current_bmi = round(float(previous_consult.new_weight) / (float(client.height) ** 2), 2)
    else:
        current_bmi = None

    return render(request, 'nutriconsult/patient_progress.html', {'client': client, 'consult': consult,
                                                                  'bmi': bmi, "current_bmi": current_bmi})
