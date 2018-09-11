from django.shortcuts import render, HttpResponse, redirect
from decimal import Decimal
# from django.http.response import HttpResponseNotAllowed 
# Create your views here.

def index(request):
	# request.session['prices'] = 0;
	# request.session['totalAmount'] = 0;
	
	return render (request, 'index.html')

def process(request):
	if request.method == "POST":
		if request.POST['id'] == 'id1':
			request.session['item'] = 19.99* int(request.POST['quantity'])
			print('this is 1')
		elif request.POST['id'] == 'id2':
			request.session['item'] = 29.99* int(request.POST['quantity'])
			print('this is 2')	
		elif request.POST['id'] == 'id3':
			request.session['item'] = 4.99* int(request.POST['quantity'])
			print('this is 3')
		elif request.POST['id'] == 'id4':
			request.session['item'] = 49.99* int(request.POST['quantity'])
			print('this is 4')
		else:
			print('Error')
		if 'prices' not in request.session:
			request.session['prices'] = 0
		else:
			request.session['prices'] += int(request.POST['quantity'])
		# request.session['prices'] += int(request.POST['quantity'])
		request.session['totalAmount'] += request.session['item']
		return redirect('/sold')
	else:
		return redirect(request, '/back_to_home')


def sold(request):
	return render(request, "sold.html")

def back_to_home(request):
	return render(request,"/process")

# def clear(request):
# 	equest.session['prices'] = 0;
# 	request.session['totalAmount'] = 0;
# 	return redirect('/')