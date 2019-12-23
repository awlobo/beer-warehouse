from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from beers.forms import CompanyForm
from beers.models import Beer, Company


class BeerDetailView(DetailView):
    model = Beer


class BeerListView(ListView):
    model = Beer


def company_edit_old(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request)
        if form.is_valid():
            company.name = form.cleaned_data("name")
            company.tax_number = form.cleaned_data('tax_number')
            company.save
    else:
        form = CompanyForm(initial={
            'name': company.name,
            'tax_number': company.tax_number
        })

    context = {
        'form': form
    }
    return render(request, 'beers/../templates/company/../templates/beers/company_form.html', context)


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm(instance=company)

    context = {
        'form': form
    }
    return render(request, 'beers/../templates/company/../templates/beers/company_form.html', context)


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyDetailView(DetailView):
    model = Company


class CompanyListView(ListView):
    model = Company

# print(beer_list.count())
# print(beer_list.filter(id=1))
# print(beer_list.filter(id=1).exists())
# print(beer_list.order_by("name"))
#
# company = Company.objects.get(pk=2)
# print(beer_list.filter(company=company))
# print(beer_list.filter(company__name__startswith="H", abv__gte=5))
# print(beer_list.filter(Q(company__name__startswith="H") | Q(abv__gte=5)))

# comp = Company.objects.create(name="Piecitos", tax_number=3342)
# Beer.objects.create(name="Piesbien", company_id="1")

# Beer.objects.filter(pk=4).first().delete()

# print(company.fk_beers.all())

# for beer in company.fk_beers.all():
#     print(beer)
#     beer.abv = 4.8
#     beer.save()

# print(Beer.objects.filter(pk__in=[1, 2, 3, 4, 5]))

# special = SpecialIngredient(name="romero")
# special.save()
# print(special)

# beer = Beer.objects.filter(pk__in=[1, 2, 3, 4, 5]).first()
# ingredient = SpecialIngredient.objects.get(pk=1)
# beer.special_ingredients.add(ingredient)

# print(beer.special_ingredients.all())
