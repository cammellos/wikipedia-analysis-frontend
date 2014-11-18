from django.shortcuts import render
from django.http import HttpResponse
from edit_history.forms import UrlForm
from edit_history.models import Url


def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


# Create your views here.

def index(request):
  urls = Url.objects.all()
  return render(request, 'edit_history/index.html',{'urls': urls})

def create(request):
  if request.method == 'POST':
    url = UrlForm(request.POST)
    url.save()

def new(request):
  form = UrlForm()
  return render(request, 'edit_history/new.html',{'form': form})

