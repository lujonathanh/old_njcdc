from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
from .forms import InputForm


def index(request):
    template = loader.get_template('calc/index.html')
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
            return HttpResponseRedirect(reverse(results))
        messages.error(request, 'There were errors. Please try again.')
    else:
        input_form = InputForm()

    template = loader.get_template('calc/input.html')
    context = {'input_form': input_form, 'formtitle': "Input"}
    return HttpResponse(template.render(context, request))

def results(request):
    # response = "You're looking at the results of entering with profile %s."
    up = request.UserProfile
    up.calculate_net()

    template = loader.get_template('calc/results.html')
    context = {'up' : request.UserProfile}
    return HttpResponse(template.render(context, request))