from django.shortcuts import render

from .forms import stockReaderForm, ExpiryDateForm
from .models import article, articleExpiryDates


def add(request):

    form = stockReaderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    form = stockReaderForm()
    return render(request, "add.html", {'form': form})


def addExpiryDate(request):

    form = ExpiryDateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    form = ExpiryDateForm()
    return render(request, "addexpirydate.html", {'form': form})


def stock_list(request):
    arts = article.objects.all()
    articles = list()
    for j in arts:
        expirydates = articleExpiryDates.objects.order_by('expiryDate').filter(referenceId=str(j.referenceId))
        articles.append({'referenceId': j.referenceId, 'nom': j.nom, 'expiryDate': expirydates[0].expiryDate})
    return render(request, 'stock.html', {"articles": articles})


def index(request):
    return render(request, "index.html")
