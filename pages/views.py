from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thanks you For Visiting",
    }
    return render(request, "home.html", context)


class AboutPagesView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "574 Street"
        context["phone_number"] = "867-5309"
        return context

class ProductsPage(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product1"] = "Pine-sol"
        context["product2"] = "Reese's"
        context["product3"] = "Nike"
        context["product4"] = "really low quality jeans, that rip after a month of use"
        return context