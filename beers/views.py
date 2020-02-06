from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from beers.forms import CompanyForm, BeerFormset
from beers.models import Beer, Company


class BeerDetailView(DetailView):
    model = Beer

    @login_required()
    def dispatch(self, request, *args, **kwargs):
        pass


class BeerListView(ListView):
    model = Beer


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyAndBeersCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "beers/company_with_beers.html"
    success_url = reverse_lazy('company-list-view')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.POST:
            ctx['beer_formset'] = BeerFormset(self.request.POST)
        else:
            ctx['beer_formset'] = BeerFormset()

        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        beer_formset = ctx['beer_formset']

        if beer_formset.is_valid():
            self.object = form.save()
            beer_formset.instance = self.object
            beer_formset.save()

        return super().form_valid(form)


class CompanyEditView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyDetailView(DetailView):
    model = Company


class CompanyListView(ListView):
    model = Company

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        self.request.session['counter'] = self.request.session.get('counter', 0) + 1

        ctx['counter'] = self.request.session['counter']

        return ctx


@login_required(login_url='/login')
def my_view(request):
    print("hello")

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
