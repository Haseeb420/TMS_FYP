from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# Create your views here.


class IndexView(View):
    template_name = "AdminSide/templates/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)


class PackageView(View):
    template_name = "AdminSide/templates/Packages/Packages.html"

    def get(self, request):
        return render(request, self.template_name)


class ProductView(View):
    template_name = "AdminSide/templates/product_list.html"

    def get(self, request):
        return render(request, self.template_name)


class AddProductView(View):
    template_name = "AdminSide/templates/add_product.html"

    def get(self, request):
        return render(request, self.template_name)


class EditProductView(View):
    template_name = "AdminSide/templates/edit_product.html"

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(View):
    template_name = "AdminSide/templates/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)
