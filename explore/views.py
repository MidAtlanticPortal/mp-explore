# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from data_manager.models import *


# from marco/utils.py
def get_domain(port=8010):
    try:
        #domain = Site.objects.all()[0].domain 
        domain = Site.objects.get(id=SITE_ID).domain
        if 'localhost' in domain:
            domain = 'localhost:%s' %port
        domain = 'http://' + domain
    except:
        domain = '..'   
    #print domain
    return domain

def data_catalog(request, template='explore/catalog.html'):
    themes = Theme.objects.filter(visible=True).order_by('display_name')
    themes = themes.select_related('layer_set')
    context = []
    for theme in themes: 
        layers = theme.layer_set.exclude(layer_type='placeholder')
        layers = layers.order_by('name')
        d = {'theme': theme, 'layers': layers, 'learn_link': theme.learn_link}
        context.append(d)
        
    context = {'themes': context, 'domain': get_domain(8000), 'domain8010': get_domain()}
    return render_to_response(template, RequestContext(request, context)) 


def data_needs(request, template='needs.html'):
    themes = Theme.objects.all().order_by('display_name')
    ordered_themes, theme_dict = add_ordered_needs_lists(themes)
    context = {'themes': themes, 'theme_dict': theme_dict, 
               'ordered_themes': ordered_themes, 'domain': get_domain(8000), 
               'domain8010': get_domain()}
    return render_to_response(template, RequestContext(request, context)) 


def external_resources(request, template='external_resources.html'):
    context = {'domain': get_domain(8000), 'domain8010': get_domain()}
    return render_to_response(template, RequestContext(request, context)) 
    
def add_ordered_needs_lists(themes_list):
    theme_dict = {}
    ordered_themes = []
    for theme in themes_list:
        needs = theme.dataneed_set.all().exclude(archived=True).order_by('name')
        if len(needs) > 0:
            ordered_themes.append(theme)
            theme_dict[theme] = needs
    return ordered_themes, theme_dict
    
   
def tiles_page(request, slug=None, template='tiles_page.html'):
    layer = get_object_or_404(Layer, slug_name=slug)
    orig_url = layer.url
    arctile_url = orig_url.replace('{z}', '{level}').replace('{x}', '{col}').replace('{y}', '{row}')
    arcrest_url = orig_url.replace('/export', '')
    context = {'layer': layer, 'arctile_url': arctile_url, 'arcrest_url': arcrest_url, 'domain': get_domain(8000)}
    return render_to_response(template, RequestContext(request, context)) 

def map_tile_example(request, slug=None, template='map_tile_example.html'):
    layer = get_object_or_404(Layer, slug_name=slug)
    context = {'layer': layer}
    return render_to_response(template, RequestContext(request, context)) 

def map_tile_esri_example(request, slug=None, template='map_tile_esri_example.html'):
    layer = get_object_or_404(Layer, slug_name=slug)
    orig_url = layer.url
    arctile_url = orig_url.replace('{z}', '{level}').replace('{x}', '{col}').replace('{y}', '{row}')
    context = {'layer': layer, 'arctile_url': arctile_url}
    return render_to_response(template, RequestContext(request, context)) 

def map_tile_leaflet_example(request, slug=None, template='map_tile_leaflet_example.html'):
    layer = get_object_or_404(Layer, slug_name=slug)
    orig_url = layer.url
    leaflet_url = orig_url.replace('$', '')
    context = {'layer': layer, 'leaflet_url': leaflet_url}
    return render_to_response(template, RequestContext(request, context)) 

def arcrest_example(request, slug=None, template='arcrest_example.html'):
    layer = get_object_or_404(Layer, slug_name=slug)
    context = {'layer': layer}
    return render_to_response(template, RequestContext(request, context)) 

def linkify(text):
    return text.lower().replace(' ', '-')
    
