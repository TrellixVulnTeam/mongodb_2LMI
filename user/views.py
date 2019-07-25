from django.shortcuts import render , HttpResponse , redirect
from bson.objectid import ObjectId
from .models import *
from datetime import datetime
import csv
# Create your views here.
def index(request):
	if request.method == 'POST' :

		start = request.POST['start']
		end = request.POST['end']
		start = start.replace('T',' ')
		start = datetime.strptime(start,'%Y-%m-%d %H:%M')
		end = end.replace('T',' ')
		end = datetime.strptime(end,'%Y-%m-%d %H:%M')
		users = people_output.objects.all()
		search.objects.all().delete()
		for userr in users:
			msi = userr.signup
			signup = msi.replace('T',' ')
			signup = signup.replace('.000Z','')
			signup = datetime.strptime(signup,'%Y-%m-%d %H:%M:%S')
			_id = userr._id
			points = userr.points
			name = userr.name
			if start <= signup <= end:
				searchs = search.objects.create(_id=_id,signup=msi,points=points,name =name)

		return render(request,'index.html',context={
			'post':True
		})


	context = {}
	return render(request,'index.html',context)


def csv_download(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename="search.csv"'
	searchss = search.objects.all()
	writer = csv.writer(response, delimiter=',')
	writer.writerow(['_id', 'signup', 'points', 'name'])
	for obj in searchss:
		writer.writerow([obj._id, obj.signup, obj.points, obj.name])

	return response