from django.shortcuts import render
# from .models import Products
from home.models import Products
from home.models import Email, Search

# Create your views here.
def contact(request):
    if request.method == "POST":
        if request.POST.get("name") and request.POST.get("phone") and request.POST.get("email") and request.POST.get("message") and request.POST.get("medicine"):
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            message = request.POST.get("message")
            medicine = request.POST.get("medicine")
            product = Products(product_name=name,product_number=phone,
                    product_email=email,product_message=message,product_medicine=medicine)
            product.save()
        elif request.POST.get("emails"):
            email = request.POST.get("emails")
            mail = Email(e_email=email)
            mail.save()
        elif request.POST.get("search"):
            search = request.POST.get("search")
            searches = Search(searchs=search)
            searches.save()


    return render(request, "contact/contact.html")