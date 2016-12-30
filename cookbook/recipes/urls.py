from django.conf.urls import url, include
from recipes import views
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_recipe/', views.add_recipe, name='add_recipe'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)',
        views.show_recipe, name='show_recipe'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/password/change/$', RegistrationView.as_view(), name='password_change'),
]