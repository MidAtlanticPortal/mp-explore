try:
    from django.urls import re_path
except (ModuleNotFoundError, ImportError):
    from django.conf.urls import url as re_path
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    #'',
    re_path(r'^noaa_catalog', TemplateView.as_view(), {'template': 'noaa_catalog.html'}),
    re_path(r'^map_tile_example/([\w-]*)', map_tile_example),
    re_path(r'^map_tile_esri_example/([\w-]*)', map_tile_esri_example),
    re_path(r'^map_tile_leaflet_example/([\w-]*)', map_tile_leaflet_example),
    re_path(r'^arcrest_example/([\w-]*)', arcrest_example),
    re_path(r'^([\w-]*)/', tiles_page),
]
