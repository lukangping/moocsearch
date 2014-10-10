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
	url = 'http://localhost:9200/moocsearch/course/_search'

	if request.GET['keywords']:
		payload = {'q': request.GET['keywords']}
		results = requests.get(url, params=payload)
	else:
		results = requests.get(url)

	courses = []

	for course in results.json()["hits"]["hits"]:
		cid = course["_id"]
		title = course["_source"]["title"]
		link  = course["_source"]["link"]
		courses.append({'cid':cid, 'title':title, 'link':link})
	return render(request, 'results.html', {'courses':courses, 'keywords':request.GET['keywords']})