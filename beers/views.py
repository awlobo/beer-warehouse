from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from beers.models import Beer, Company, SpecialIngredient


def beer_detail_view(request, pk):
    print("user", request.user)
    print("GET", request.GET)
    context = {
        'beer': Beer.objects.get(pk=pk)
    }
    return render(request, "beer_detail.html", context)


def beer_list_view(request):
    beer_list = Beer.objects.all()

    print(beer_list.count())
    print(beer_list.filter(id=1))
    print(beer_list.filter(id=1).exists())
    print(beer_list.order_by("name"))

    company = Company.objects.get(pk=2)
    print(beer_list.filter(company=company))
    print(beer_list.filter(company__name__startswith="H", abv__gte=5))
    print(beer_list.filter(Q(company__name__startswith="H") | Q(abv__gte=5)))

    # comp = Company.objects.create(name="Piecitos", tax_number=3342)
    # Beer.objects.create(name="Piesbien", company_id="1")

    # Beer.objects.filter(pk=4).first().delete()

    print(company.fk_beers.all())

    for beer in company.fk_beers.all():
        print(beer)
        # beer.abv = 4.8
        # beer.save()

    print(Beer.objects.filter(pk__in=[1, 2, 3, 4, 5]))

    # special = SpecialIngredient(name="romero")
    # special.save()
    # print(special)

    beer = Beer.objects.filter(pk__in=[1, 2, 3, 4, 5]).first()
    ingredient = SpecialIngredient.objects.get(pk=1)
    # beer.special_ingredients.add(ingredient)

    print(beer.special_ingredients.all())


    context = {
        'beer_list': beer_list
    }
    return render(request, "beer_list.html", context)
