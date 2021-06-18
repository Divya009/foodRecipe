from django.shortcuts import render
from urllib.parse import unquote
import requests
import requests, json
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def fetch_recipe_from_keyword(request):
	keyword = request.GET.get('keyword', '')
	recipe_id = request.GET.get('recipe_id', '')
	list_of_recipe_data = []
	if keyword:
		json_response = fetch_list_of_recipe_from_open_api_using_keyword(keyword)
		try:
			list_of_recipe_data = json_response['results']
		except:
			list_of_recipe_data = []

	if recipe_id and request.is_ajax():
		try:
			json_response = fetch_recipt_of_given_recipe_id(recipe_id)
			success = True
		except:
			success = False
			
		return JsonResponse({'success':success,'json_response':json_response})

	return render(request, 'FoodAPIRecipeApp/show_recipe_data.html', {'list_of_recipe_data':list_of_recipe_data,'keyword':keyword})


def fetch_list_of_recipe_from_open_api_using_keyword(keyword):
	api_url = '%srecipes/complexSearch' %(settings.API_BASE_URL)
	params = {'apiKey':settings.API_KEY, 'query':keyword}
	response = requests.get(api_url, params=params)
	json_response = response.json()

	return json_response

def fetch_recipt_of_given_recipe_id(recipe_id):
	api_url = '%srecipes/%s/information' %(settings.API_BASE_URL, recipe_id)
	params = {'apiKey':settings.API_KEY}
	response = requests.get(api_url, params=params)
	json_response = response.json()

	return json_response