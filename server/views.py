from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse

from server.models import FormCompletion
from server.forms import TypeForm, UploadForm
from server.schema import form_map
from server.schemulator import schema_to_form

def step_1(request):
    form = TypeForm(request.POST or None)
    if form.is_valid():
        return HttpResponseRedirect(reverse('step_2', args=[form.cleaned_data['form_type']]))
    return TemplateResponse(request, 'form.html', {'form': form, 'title': 'Select Form Type'})

def step_2(request, slug):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.form_type = slug
        form_completion = form.save()
        return HttpResponseRedirect(reverse('step_3', args=[form_completion.id]))
    return TemplateResponse(request, 'form.html', {'form': form, 'title': 'Upload Form Image'})

def step_3(request, id):
    form_completion = get_object_or_404(FormCompletion, id=id)
    next = reverse('step_4', args=[form_completion.id])
    # status is new, processing, or error
    return TemplateResponse(request, 'step_3.html', {'next': next, 'id': id, 'title': 'Processing...'})

def check_3(request, id):
    form_completion = get_object_or_404(FormCompletion, id=id)
    form_completion.process() # idempotent, does nothing if already processing/processed
    return JsonResponse({ 'status': form_completion.status })

def step_4(request, id):
    form_completion = get_object_or_404(FormCompletion, id=id)
    form_type = form_completion.form_type
    form = schema_to_form(
        form_map[form_type]['schema'],
        request.POST or None,
        initial=form_completion.data
    )
    if form.is_valid():
        form_completion.data = form.cleaned_data
        form_completion.status = 'verified'
        form_completion.save()
        return HttpResponseRedirect(reverse('step_5'))
    return TemplateResponse(request, 'form.html', {'form': form, 'title': 'Verify Data'})

def step_5(request):
    return TemplateResponse(request, 'step_5.html', {'title': 'Complete'})
