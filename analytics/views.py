from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Map
import pandas as pd
import geopandas as gpd
from django.conf import settings
import os
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import urllib, base64
import io


# Create your views here.
def home(request):
    return render(request,'home.html')
