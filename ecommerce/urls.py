from django.urls import path
from . import views
from ecommerce.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="ecommerce/home.html",
)

urlpatterns = [
    path('ecom/', views.index, name='ecommerce'),
    path('ecom/<name>', views.ecom, name='ecom'),
    path('home/', home_list_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('log/', views.log_message, name='log'),
]

