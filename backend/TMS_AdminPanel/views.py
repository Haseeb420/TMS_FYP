from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# Create your views here.

_SiteName = "-Royal Travels"


class IndexView(View):
    _template_name = "AdminSide/templates/dashboard.html"
    _title = "Dashboard"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self._template_name, data)


""""
     All Packages views are start from here
"""

"""
Packages List view code start from here

"""


class PackageView(View):
    template_name = "AdminSide/templates/Packages/Packages.html"
    _title = "Packages"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""
Packages List view code End from here

"""

"""
Packages List view code start from here

"""


class AddPackage(View):
    template_name = "AdminSide/templates/Packages/AddPackages.html"
    _title = "AddPackages"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""
Packages List view code End from here

"""


""""
     All Packages views are ends here 
"""


"""
All users views code start here
"""


"""User List view code starts here"""


class ManageUsers(View):
    template_name = "AdminSide/templates/Users/users.html"
    _title = "Users"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""User List view code ends here"""


"""
All users views code ends here
"""


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

class ManageTransactions(View):
    template_name = "AdminSide/templates/sales-transaction/transactions.html"

    def get(self, request):
        return render(request, self.template_name)

class ManageSales(View):
    template_name = "AdminSide/templates/sales-transaction/sales.html"

    def get(self, request):
        return render(request, self.template_name)

class ManageFeedback(View):
    template_name = "AdminSide/templates/sales-transaction/feedback.html"

    def get(self, request):
        return render(request, self.template_name)
