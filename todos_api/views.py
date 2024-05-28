from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
months = {
	"january": "January",
	"february": "February",
	"march": "March",
	"april": "April",
	"may": "May",
	"june": "June",
	"july": "July",
	"august": "August",
	"september": "September",
	"october": "October",
	"november": "November",
	"december": "December",
}


def index(request):
	return render(request, "todos_api/index.html")




def string_route(request, wildcard):
	try:
		chosen_month = months[wildcard.lower()]
		return HttpResponse(f"Weee  {chosen_month}")
	except:
		return HttpResponseNotFound(
			f"Month not found. Please enter a valid month name.")


def int_route(request, month):
	#
	months_list = list(months.keys())

	if month > (len(months_list)):
		return HttpResponseNotFound(f"Not found")

	chosen_month = months_list[month - 1]
	# name of view, then what args we need to pass for the wildcard
	# since there's only 1 wildcard, we pass chosen_month to replace "wildcard"
	redirect_path = reverse("string_route", args=[chosen_month])
	return HttpResponseRedirect(redirect_path)
