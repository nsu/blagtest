from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blagtest.views.home', name='home'),
    # url(r'^blagtest/', include('blagtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^calc/(?P<num1>\d*)/(?P<num2>\d*)/$', 'core.views.add_nums'),
    url(r'^mult/(?P<num1>\d*)/(?P<num2>\d*)/$', 'core.views.mult_nums'),
    url(r'^blag/list/$', 'core.views.list_posts'),
)
