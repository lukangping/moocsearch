from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def index(request):
	results = [{"cid":"id1", "title":"t1"}, {"cid":"id2", "title":"t2"}]
	context = {'courses': results}
	return render(request, 'index.html', context)

# def search(request, keywords):
def search(request):
	base_url = 'http://localhost:9200/moocsearch/course/_search'

	pagesize = 20
	pagenumber = request.GET['p']
	pagefrom = (int(pagenumber) - 1) * pagesize + 0
	url = base_url + '?size=20&from=' + str(pagefrom)

	# the view object for present
	vo = {}

	# if request.GET['keywords']:
	# 	payload = {'q': request.GET['keywords']}
	# 	results = requests.get(url, params=payload)
	# else:
	# 	results = requests.get(url)

	# for demo show all results no matter input
	results = requests.get(url)

	vo['keywords'] = request.GET['keywords']

	courses = []
	for course in results.json()["hits"]["hits"]:
		cid = course["_id"]
		title = course["_source"]["title"]
		link  = course["_source"]["link"]
		image = course["_source"]["image"]
		site = course["_source"]["site"]
		courses.append({'cid':cid, 'title':title, 'link':link, 'image':image, 'site':site})

	vo['courses'] = courses

	totalnumber = results.json()["hits"]["total"]
	currentnumber = int(pagenumber) * pagesize
	if (int(totalnumber) > currentnumber):
		vo['nexturl'] = request.path + '?keywords=' + request.GET['keywords'] + '&p=' + str(int(pagenumber)+1)
	return render(request, 'results.html', vo)


def test(request):
	return render(request, 'test.html')