from django.shortcuts import render, redirect
from django.contrib import messages
from leads.models import Lead
from leads.forms import LeadForm, AssignAgentForm
from .forms import AgentCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
User = get_user_model()

# ===============================
# Dashboard
# ===============================
def dashboard(request):
    leads = Lead.objects.all()
    unassigned_leads = Lead.objects.filter(agent__isnull=True)
    agent_leads = Lead.objects.filter(agent=request.user)
    context = {
        'leads': leads,
        'unassigned_leads': unassigned_leads,
        'agent_leads': agent_leads
    }
    return render(request, 'accounts/dashboard.html', context)


# ===============================
# Agents List
# ===============================
@staff_member_required
@login_required(login_url='/account/signin')
def agents_list(request):
    agents = User.objects.filter(type="Agent")
    context = {
        'agents': agents
    }
    return render(request, 'accounts/agents/agents.html', context)


# ===============================
# Create Agent
# ===============================
@staff_member_required
@login_required(login_url='/account/signin')
def create_agent(request):
    form = AgentCreationForm()
    if request.method == "POST":
        form = AgentCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_staff=False
            f.type="Agent"
            f.save()
            
            # Send Email with Password
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            send_mail(
                'New Acocunt Creation',
                f'Your account has been created on WEBSITE. Your email is {email} and password is {password}.',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, f"Agent has been created. He/She will get an email shortly with login details.")
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'accounts/agents/create-agent.html', context)


# ===============================
# Assign Agent
# ===============================
@staff_member_required
@login_required(login_url='/account/signin')
def assign_agent(request, id):
    lead = Lead.objects.get(id=id)
    form = AssignAgentForm(instance=lead)
    if request.method == "POST":
        form = AssignAgentForm(request.POST, instance=lead)
        if form.is_valid():
            f = form.save(commit=False)
            f.status = 'Assigned'
            f.save()
            messages.success(request, f"Agent has been assigned to lead {lead.first_name} {lead.last_name}.")
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'accounts/leads/assign-agent.html', context)


# ===============================
# Create Lead
# ===============================
@staff_member_required
@login_required(login_url='/account/signin')
def create_lead(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            if not form.data['agent']:
                f.status="Unassigned"
            else:
                f.status="Assigned"
            f.save()
            messages.success(request, f"A new lead has been created.")
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'accounts/leads/create-lead.html', context)


# ===============================
# Edit Lead
# ===============================
@staff_member_required
@login_required(login_url='/account/signin')
def edit_lead(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadForm(instance=lead)
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, f"The lead has been updated.")
            return redirect('dashboard')
    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'accounts/leads/edit-lead.html', context)
