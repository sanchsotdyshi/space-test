from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from task.models import Question
from django.urls import reverse
from fpdf import FPDF

# Create your views here.

def make_pdf(f_name, s_name, score):
	pdf = FPDF('L', 'mm', 'A4')
	pdf.add_page()
	pdf.add_font('FreeMono', '', 'task/static/task/sertificate/20294.ttf', uni=True)

	pdf.image('task/static/task/sertificate/sert.jpg', x=0, y=0)

	pdf.ln(60)
	pdf.set_font("FreeMono", size=70)
	pdf.cell(270, 10, txt='Сертификат', align='C')

	pdf.ln(18)
	pdf.set_font("FreeMono", size=25)
	pdf.cell(270, 10, txt='Подтверждает, что {} {}'.format(s_name, f_name), align='C')


	pdf.ln(13)
	pdf.set_font("FreeMono", size=25)
	pdf.cell(270, 10, txt='Завершил(а) курс \"Знакомство с космосом\"', align='C')

	pdf.ln(13)
	pdf.set_font("FreeMono", size=25)
	pdf.cell(270, 10, txt='Количество баллов: {}'.format(score), align='C')

	pdf.output("task/static/task/sertificate/sertificate.pdf")



def test(request):
	q = Question.objects.all()
	context={'questions': q}
	return render(request, 'task/index.html', context)

def check(request):
	score = 0
	for question in Question.objects.all():
		answer = int(request.POST.get(str(question.id), 0))
		if answer == question.correct_answer:
			score += 1

	return HttpResponseRedirect(reverse('task:form', args=(score,)))

def form(request, score=0, war=0, ):
	if war == 0:
		context={'score': score}
		return render(request, 'task/form.html', context)
	else:
		context={'score': score, 'warning': war}
		return render(request, 'task/form.html', context)

def registration(request, score=0):
	if request.method == 'POST':
		f_name = request.POST['first_name']
		s_name = request.POST['second_name']
		if f_name == '' or s_name == '':
			return HttpResponseRedirect(reverse('task:war_form', args=(score, 1,)))
		else:
			make_pdf(f_name, s_name, score)
			context={
				'path': '/static/task/sertificate/sertificate.pdf',
			}
			return render(request, 'task/sertificate.html', context)
	else:
		return HttpResponseRedirect(reverse('task:form', args=(score,)))



