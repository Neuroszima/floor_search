from django.shortcuts import render

# Create your views here.
from django.views import View
from scrappy.models import ScrapyItem  # ,Product


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class SpiderFormView(View):
    def get(self, request):
        return render(request, 'crawler_view.html')


class RawDataView(View):
    def get(self, request):
        raw_data = ScrapyItem.objects.all()
        return render(request, 'raw_data_view.html', {"raw_data": raw_data})


# views currently not used:

# class ProductsView(View):
#     def get(self, request):
#         products = Product.objects.all()
#         return render(request, 'crawler_view.html', {"products": products})
#
#
# class ContactView(View):
#     def get(self, request):
#         return render(request, "empty_contact.html")
#
#
# class AboutView(View):
#     def get(self, request):
#         return render(request, "empty_about.html")
