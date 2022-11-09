from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views




urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('about_us/', views.about_us ),
    path('date_now/', views.date_now ),
    path('', include('main.urls'))


] + static(settings.STATIC_URL, document_url=settings.STATIC_URL)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)
