from django.shortcuts import render

def index(request):
	print 'hello'
	return render(request, 'ninjas/index.html')

def allNinjas(request):
	print 'turtles'
	
	context = {
		'ninja_name' : 'all'
	}
	return render(request, 'ninjas/ninjas.html', context)

def ninjas(request, color):
	
	context = { 
		'ninja_name' : color
	}
	return render(request, 'ninjas/ninjas.html', context)

