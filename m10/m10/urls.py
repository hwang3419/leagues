from django.conf.urls import patterns, include, url
from rest_resource.api import TestResource, SP1Resource, E0Resource, D1Resource, I1Resource
from tastypie.api import Api
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#test_resource = TestResource()
#sp1_resource = SP1Resource()
v1_api = Api(api_name = 'v1')
v1_api.register(SP1Resource())
v1_api.register(E0Resource())
v1_api.register(D1Resource())
v1_api.register(I1Resource())
v1_api.register(TestResource())
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'm10.views.home', name='home'),
    url(r'^$', 'rest_resource.views.home'),
    (r'^match/', 'm10.views.match'),
    (r'^api/', include(v1_api.urls)),
    (r'^summary/', 'm10.views.summary'),
    (r'^comment/', 'm10.views.comment'),
    (r'^trend/', 'm10.views.trend'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
