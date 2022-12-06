from django.shortcuts import render
from home.models import Email, Search

# Create your views here.
def medicine(request):
    if request.method == "POST":
        if request.POST.get("emails"):
            email = request.POST.get("emails")
            mail = Email(e_email=email)
            mail.save()
        elif request.POST.get("search"):
            search = request.POST.get("search")
            searches = Search(searchs=search)
            searches.save()

    return render(request, "medicine/medicine.html")