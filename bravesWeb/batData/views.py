from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import SimulationForm
import sys
from io import StringIO
from django.template import loader
from pylab import *
import PIL, PIL.Image, io
from analyze import analyzelib



def index(request):
	form = SimulationForm()
	context = {'form': form}
	return render(request, "batData/index.html", context)

def results(request):
	output = ""
	if request.method == 'POST':
		form = SimulationForm(request.POST)
		if form.is_valid():
			variable1 = form.data['variable1']
			variable2 = form.data['variable2']
			graph = form.data['graph']
			if graph == ('Scatter Plot'):
				analyzelib.scatter(variable1, variable2)
			if graph == ('Bar Chart'):
				analyzelib.bar_chart(variable1, variable2)
			if graph == ('Histogram'):
				analyzelib.histogram(variable1)
			return render(request, "batData/results.html")
		else:
			form = SimulationForm()
		return render(request, "batData/index.html", {'form': form})