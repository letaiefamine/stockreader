from django.shortcuts import render

from .forms import stockReaderForm,ExpiryDateForm
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
    bcp = article.objects.all()
    # date = articleExpiryDates.objects.all()
    # print(date[1].expiryDate)
    date = articleExpiryDates.objects.select_related('referenceId')
    print(date)
    # for elmt in bcp:
    # #     date = articleExpiryDates.objects.filter(referenceId=elmt.referenceId)
    # #     print(date)
    # #     date = articleExpiryDates.objects.filter
    #     date = articleExpiryDates.objects.select_related('referenceId').filter(elmt.referenceId)
    #     print(date[1].expiryDate)
    # #     for elem in date:
    # #         print(elem.referenceId)
    context = {"sotcks": bcp,"dates" : date}
    return render(request, 'stock.html', context)


def index(request):
    return render(request, "index.html")
