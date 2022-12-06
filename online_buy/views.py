from django.shortcuts import render
from home.models import Email, Search


# Create your views here.
def online_buy(request):
    if request.method == "POST":
        if request.POST.get("emails"):
            email = request.POST.get("emails")
            mail = Email(e_email=email)
            mail.save()
        elif request.POST.get("search"):
            search = request.POST.get("search")
            searches = Search(searchs=search)
            searches.save()

    return render(request, 'online_buy/buy.html')