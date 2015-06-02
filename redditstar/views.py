# STDL imports

# Django Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

# Third Party Apps
import requests

# Local Imports
from .forms import LoginForm
from .models import StarModel

"""To get multiple things from reddit:
    http://www.reddit.com/api/info.json?id=t3_37utk9,t3_37vf3t
"""

__REDDIT_BASE_URL__ = 'http://www.reddit.com'


def home(request, resource=None):
    if 'email' not in request.session:
        return HttpResponseRedirect('/login')
    favorites_names = StarModel.objects.filter(
        email=request.session['email']).values_list('listing', flat=True)
    reddit_api_resources = {
        'favorites': '%s/api/info.json?id=%s' % (
            __REDDIT_BASE_URL__, ','.join(favorites_names)),
        '': '%s/top.json' % __REDDIT_BASE_URL__,
        'top': '%s/top.json' % __REDDIT_BASE_URL__,
        'hot': '%s/hot.json' % __REDDIT_BASE_URL__}
    # TODO: Include some sort of authentication to be able to pull
    # data from reddit without having 429
    response = requests.get(reddit_api_resources[resource])
    while response.status_code == 429:
        response = requests.get(reddit_api_resources[resource])
    response_dict = response.json()
    return render(request, 'redditstar/home.html', {
        'data': response_dict['data']['children'],
        'reddit_base_url': __REDDIT_BASE_URL__,
        'favorites_names_set': set(favorites_names),
        'role': 'top' if resource == '' or resource is None else resource})


def favorite(request, listing_name=None):
    results, response = {}, None
    if 'email' not in request.session:
        results['successful'] = False
        results['errors'] = 'Login before bookmarking'
        response = JsonResponse(results, status=401)
    else:
        try:
            StarModel.objects.create(
                email=request.session['email'],
                listing=listing_name)
            results['successful'] = True
            response = JsonResponse(results)
        except:
            results['successful'] = False
            results['errors'] = 'Saving didnot complete'
            response = JsonResponse(results, status=500)
    return response


def unfavorite(request, listing_name=None):
    results, response = {}, None
    if 'email' not in request.session:
        results['success'] = False
        results['errors'] = 'Login before removing bookmark'
        response = JsonResponse(results, status=401)
    else:
        try:
            object_to_delete = StarModel.objects.get(
                email=request.session['email'],
                listing=listing_name)
            object_to_delete.delete()
            results['success'] = True
            response = JsonResponse(results)
        except:
            results['success'] = False
            results['errors'] = 'Removing bookmark didnot complete'
            response = JsonResponse(results, status=500)
    return response


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['email'] = form.cleaned_data['email']
    if 'email' in request.session:
        return HttpResponseRedirect('/')
    return render(request, 'redditstar/login.html', {'form': form})


def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return HttpResponseRedirect('/login')
