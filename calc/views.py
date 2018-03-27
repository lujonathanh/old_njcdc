from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
from .forms import InputForm
from .models import UserProfile


def index(request):
    return HttpResponse("Hello, world. You're at the calc index.")

def input(request):
    #http://127.0.0.1:8000/print("INputting")
    if request.method == 'POST':
        input_form = InputForm(request.POST)

        if input_form.is_valid():
            user = input_form.save()
            messages.success(request, "Thank you for entering")
            #return HttpResponseRedirect(reverse('input'))
            #return HttpResponseRedirect(reverse('index'))
            return HttpResponseRedirect(reverse('results', args=(user.id,)))
            # return HttpResponseRedirect(reverse('results', kwargs={'id' : input_form.instance.id}))

            # return HttpResponseRedirect(reverse('results', args=[input_form.instance.id]))
            # return HttpResponseRedirect(reverse('results', kwargs={'id': user.id}))
            # return HttpResponseRedirect(reverse('results', kwargs={'up': user}))
        messages.error(request, 'There were errors. Please try again.')
    else:
        input_form = InputForm()

    template = loader.get_template('calc/input.html')
    context = {'input_form': input_form, 'formtitle': "Input"}
    return HttpResponse(template.render(context, request))

def results(request, id):
    # response = "You're looking at the results of entering with profile %s."
    print("Arrived")

    up = UserProfile.objects.get(id=id)
    up.calculate_net()

    template = loader.get_template('calc/results.html')
    context = {'up' : up}
    return HttpResponse(template.render(context, request))