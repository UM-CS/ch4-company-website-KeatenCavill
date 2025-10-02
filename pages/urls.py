from django.urls import path

from .views import home_page_view, AboutPagesView, ProductsPage


urlpatterns = [
    path("about/", AboutPagesView.as_view(), name="about"),
    path("", home_page_view, name="home"),
    path("products/", ProductsPage.as_view(), name="products"),
]
