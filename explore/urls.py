from django.conf.urls import url, patterns
from django.conf import settings
from django.views.generic.base import TemplateView
from views import *

urlpatterns = patterns('',
    (r'^noaa_catalog', TemplateView.as_view(), {'template': 'noaa_catalog.html'}),
    (r'^map_tile_example/([\w-]*)', map_tile_example),
    (r'^map_tile_esri_example/([\w-]*)', map_tile_esri_example),
    (r'^map_tile_leaflet_example/([\w-]*)', map_tile_leaflet_example),
    (r'^arcrest_example/([\w-]*)', arcrest_example),
    (r'^([\w-]*)', tiles_page),
)
