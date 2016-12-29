from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_recipe/', views.add_recipe, name='add_recipe'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)',
        views.show_recipe, name='show_recipe'),
]