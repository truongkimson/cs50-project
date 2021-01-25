
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Hangout
from .forms import HangoutViewForm, HangoutModifyForm, HangoutCreateForm
from django.urls import reverse


def home(request):
    context = {}
    return render(request, 'hangout/home.html', context)

@login_required
def profile(request):
    context = {}
    return render(request, 'hangout/profile.html', context)

@login_required
def create(request):
    if request.method == 'GET':
        form = HangoutCreateForm()
        context = {'form': form}
        return render(request, 'hangout/create.html', context)
    else:
        print(request.POST)
        input = request.POST.copy()
        input['owner'] = request.user.id
        form = HangoutCreateForm(input)
        form.save()
        return HttpResponseRedirect(reverse('home'))

@login_required
def list(request):
    owned_hangouts = request.user.owned_hangouts.filter(date__gte=timezone.now())
    participating_hangouts = request.user.participating_hangouts.filter(date__gte=timezone.now())
    past_hangouts = request.user.owned_hangouts.filter(date__lt=timezone.now())
    past_hangouts.union(request.user.participating_hangouts.filter(date__lt=timezone.now()))
    context = {'owned_hangouts': owned_hangouts,
               'participating_hangouts': participating_hangouts,
               'past_hangouts': past_hangouts,
               }
    return render(request, 'hangout/list.html', context)

@login_required
def discover(request):
    hangout_list = Hangout.objects.filter(date__gte=timezone.now())
    context = {'hangout_list': hangout_list}
    return render(request, 'hangout/discover.html', context)

@login_required
def detail(request, hangout_id):
    h = Hangout.objects.get(pk=hangout_id)
    form = HangoutViewForm(instance=h)

    if 'msg' in request.GET:
        msg = request.GET['msg']
    else:
        msg = None

    if h.owner_id == request.user.id:
        owned = True
    else:
        owned = False
        
    context = {'hangout_id': hangout_id,
               'form': form,
               'msg': msg,
               'owned': owned,
               }
    return render(request, 'hangout/detail.html', context)

@login_required
def modify(request, hangout_id):
    h = Hangout.objects.get(pk=hangout_id)
    if h.owner_id == request.user.id:
        form = HangoutModifyForm(instance=h)
        context = {'hangout_id': hangout_id,
                    'form': form,
                    }
        if request.method == 'GET':
            return render(request, 'hangout/modify.html', context)
        else:
            form = HangoutModifyForm(request.POST, instance=h)
            form.save()
            return HttpResponseRedirect(reverse('hangout:detail', args=(hangout_id,))
                                        + '?msg=success')
    else:
        return redirect('hangout:access-denied')
        

@login_required
def delete(request, hangout_id):
    h = Hangout.objects.get(pk=hangout_id)
    if h.owner_id == request.user.id:
        h.delete()
        context = {}
        return render(request, 'hangout/delete.html', context)
    else:
        return redirect('hangout:access-denied')

def access_denied(request):
    return render(request, 'hangout/access_denied.html', {})
