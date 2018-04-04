from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
from .forms import InputForm
from .models import UserProfile


def index(request):
    template = loader.get_template('calc/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def plot(request):
    template = loader.get_template('calc/plot.html')
    context = {}
    return HttpResponse(template.render(context, request))

def chart(request):
    template = loader.get_template('calc/chart.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('calc/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def input(request):
    if request.method == 'POST':
        input_form = InputForm(request.POST)

        if input_form.is_valid():
            user = input_form.save()
            messages.success(request, "Thank you for entering")
            return HttpResponseRedirect(reverse('results', args=(user.id,)))
        messages.error(request, 'There were errors. Please try again.')
    else:
        input_form = InputForm()

    template = loader.get_template('calc/input.html')
    context = {'input_form': input_form, 'formtitle': "Input"}
    return HttpResponse(template.render(context, request))

def results(request, id):
    print("Arrived")

    up = UserProfile.objects.get(id=id)

    up.calculate_net()

    template = loader.get_template('calc/results.html')
    context = {'up' : up}
    return HttpResponse(template.render(context, request))


    