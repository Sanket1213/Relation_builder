from django.shortcuts import render, HttpResponseRedirect
from .forms import RelationBuilder, AddRelation
from .models import User, Relation
# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        fm=RelationBuilder(request.POST)
        if fm.is_valid():
            fm.save()
        fm=RelationBuilder()
    else:
        fm = RelationBuilder()
    display_relation = User.objects.all()

    return render(request, 'relation/add_n_show.html', {'form':fm, 'dis_rel':display_relation })

def delete_relation(request, id):
    if request.method == 'POST':
        val=User.objects.get(pk=id)
        val.delete()
        return HttpResponseRedirect('/')

def update_relation(request, id):
    if request.method=='POST':
        val=User.objects.get(pk=id)
        fm=RelationBuilder(request.POST, instance=val)
        if fm.is_valid():
            fm.save()
    else:
        val=User.objects.get(pk=id)
        fm=RelationBuilder(instance=val)
    return render(request, 'relation/update_relation.html', {'form':fm})

def add_relation(request):
    if request.method == 'POST':
        fm=AddRelation(request.POST)
        if fm.is_valid():
            fm.save()
        fm=AddRelation()
    else:
        fm = AddRelation()
    return render(request, 'relation/add_relation.html', {'form':fm})
