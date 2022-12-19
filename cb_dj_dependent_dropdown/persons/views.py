
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Branch


def person_create_view(request,):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            kv = Person.objects.latest('id')
            kt=kv.id

            return redirect('detail', kt)
    return render(request, 'persons/home.html', {'form': form})


def detail(request,movie_id):
    mov=Person.objects.get(id=movie_id)

    return render(request,"persons/hi.html",{'mov':mov})

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'branches': branches })
    # return JsonResponse(list(branches.values('id', 'name')), safe=False)