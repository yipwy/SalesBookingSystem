from django.shortcuts import render, redirect
from .models import Company, Phase
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  # Class View

from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)




# Create your views here.
@login_required()
def list_companies(request):
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies': companies})

@login_required()
def create_company(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')
    return render(request, 'companies-form.html', {'form': form})

@login_required()
def update_company(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('list_companies')
    return render(request, 'companies-form.html', {'form': form, 'company': company})

@login_required()
def delete_company(request, id):
    company = Company.objects.get(id=id)

    if request.method == 'POST':
        company.delete()
        return redirect('list_products')
    return render(request, 'comp-delete-confirm.html', {'company': company})


class PhaseListView(LoginRequiredMixin, ListView):
    template_name = 'phase_list.html'
    queryset = Phase.objects.all()

