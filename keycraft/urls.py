from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    path('newsletter/', include('newsletter.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'keycraft.views.handler404'
