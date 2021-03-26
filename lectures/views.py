from django.shortcuts import render

# Create your views here.

def main(request):
	text='Курс разработан воспитателем МБДОУ "Детский сад №181" г.о. Самары: Костиной О.С.'
	context={
	'text':text
	}
	return render(request, 'lectures/main.html', context)

def lecture(request, num=0):
	if num == 1:
		source = '/static/lectures/videos/lecture1.mp4'
	elif num == 2:
		source = "/static/lectures/videos/lecture2.mp4"
	elif num == 3:
		source = "/static/lectures/videos/lecture3.mp4"
	elif num == 4:
		source = "/static/lectures/videos/lecture4.mp4"
	elif num == 5:
		source = "/static/lectures/videos/lecture5.mp4"
	context={
		'source':source,
		'next': num+1
	}
	return render(request, 'lectures/lecture.html', context)
