from django.contrib import admin
from django.urls import path,include

admin.site.site_header="icoder admin"
admin.site.site_title="icoder admin panel"
admin.site.index_title="icoder admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls'))
]
