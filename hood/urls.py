from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^hood/(?P<neighborhood_id>[0-9]+)$',views.hoods,name='hood-details'),
  url(r'^new/neighborhood$',views.new_hood,name='newHood'),
  url(r'^new/neighbour$',views.new_neighbour,name='newNeighbour'),
  url(r'^new/business$',views.new_business,name='newBusiness'),
  url(r'^profile/',views.user_profile,name='userProfile'),
  url(r'^search/',views.search_business,name='search'),
  url(r'^map$', views.maps, name='map'),

]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
