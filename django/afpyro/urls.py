from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.contrib.sites.models import Site

admin.autodiscover()

def pouet(request):
    print Site.objects.all()
    return render(request, 'home.haml', {'foobar': 'baz'})

urlpatterns = patterns('',
    url(r'^$', pouet, name='home'),
    # url(r'^afpyro/', include('afpyro.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
