from django.conf.urls import url, patterns
from django.views.generic.base import TemplateView
from views import *

urlpatterns = patterns('',
    (r'^catalog', data_catalog),
    (r'^noaa_catalog', TemplateView.as_view(), {'template': 'noaa_catalog.html'}),
    (r'^needs', data_needs),
    (r'^resources', external_resources),
    (r'^map_tile_example/([\w-]*)', map_tile_example),
    (r'^map_tile_esri_example/([\w-]*)', map_tile_esri_example),
    (r'^map_tile_leaflet_example/([\w-]*)', map_tile_leaflet_example),
    (r'^arcrest_example/([\w-]*)', arcrest_example),
    (r'^([\w-]*)', tiles_page)
)
