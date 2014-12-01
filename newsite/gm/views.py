from gm.models import Car, GasStation
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.db import connection
from tutorial.main import GasCrawler

class IndexView(generic.ListView):
    template_name = 'gm/index.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        return Car.objects.raw('SELECT * FROM gm_car')

class TestView(generic.ListView):
	template_name = 'gm/test.html'
	def get_queryset(self):
		return Car.objects.all()

class AddCarView(generic.ListView):
	template_name = 'gm/addcar.html'
	def get_queryset(self):
		return Car.objects.raw('SELECT * FROM gm_car')

class EditCarView(generic.DetailView):
	model = Car
	template_name = 'gm/editcar.html'

def result(request, locationzip):
	station = GasStation.objects.raw('SELECT * FROM gm_gasstation WHERE location = %s', [locationzip])
	return render(request, 'gm/result.html', {'station_list': station})
	

def recordmanager(request):
	#c = Car.objects.get(pk=request.POST['choice']).delete()
	#c.save()
	if 'add' in request.POST:
		return HttpResponseRedirect(reverse('gm:addcar'))

	if 'new' in request.POST:
		if request.POST['company'] == "" or request.POST['modeltype'] == "" or request.POST['madeyear'] == "" or request.POST['mpg'] == "" or request.POST['location'] == "":
			return HttpResponseRedirect(reverse('gm:index'))
		cursor = connection.cursor()
		cursor.execute("INSERT INTO gm_car(company, modeltype, madeyear, mpg, location) VALUES (%s,%s,%s,%s,%s)",(request.POST['company'],request.POST['modeltype'],request.POST['madeyear'],request.POST['mpg'],request.POST['location']))
		return HttpResponseRedirect(reverse('gm:index'))

	if 'edit' in request.POST:
		if 'choice' in request.POST:
			return HttpResponseRedirect(reverse('gm:editcar', args=(request.POST['choice'],)))

	if 'save' in request.POST:
		if request.POST['company'] == "" or request.POST['modeltype'] == "" or request.POST['madeyear'] == "" or request.POST['mpg'] == "" or request.POST['location'] == "":
			return HttpResponseRedirect(reverse('gm:index'))
		else:
			cursor = connection.cursor()
			cursor.execute ("""UPDATE gm_car SET company=%s, modeltype=%s, madeyear=%s, mpg=%s, location=%s WHERE id=%s""", (request.POST['company'], request.POST['modeltype'], request.POST['madeyear'], request.POST['mpg'], request.POST['location'], request.POST['id']))
			#c = Car(id = request.POST['id'],company = request.POST['company'], modeltype = request.POST['modeltype'], madeyear = request.POST['madeyear'], mpg = request.POST['mpg'], location = request.POST['location'])
			#c.save(force_update=True)
			return HttpResponseRedirect(reverse('gm:index'))

	if 'delete' in request.POST:
		if 'choice' in request.POST:
			#Car.objects.get(pk=request.POST['choice']).delete()
			cursor = connection.cursor()
			cursor.execute ("""DELETE FROM gm_car WHERE id=%s""", (request.POST['choice']))

	if 'search' in request.POST:
		if 'choice' in request.POST:
			#cursor = connection.cursor()
			#cursor.execute ("""DELETE FROM testdata""")
			str = Car.objects.get(pk=request.POST['choice']).location;
			print "haha"
			print str;
			#g = GasCrawler(str)
			#g.run()
			return HttpResponseRedirect(reverse('gm:result', args=(str,)))
	
	return HttpResponseRedirect(reverse('gm:index'))

	
	