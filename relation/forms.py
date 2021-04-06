from django import forms
from django.core import validators
from .models import User, Relation


relations = Relation.objects.all().values_list('name', 'name')
rel_list = []
for val in relations:
    rel_list.append(val)
    
class RelationBuilder(forms.ModelForm):
    class Meta():
        model=User
        fields=['name1', 'name2', 'relation']
        widgets={
            'name1': forms.TextInput(attrs={'class':'form-control'}),
            'name2': forms.TextInput(attrs={'class':'form-control'}),
            'relation': forms.Select(choices=rel_list, attrs={'class':'form-control'}),
        }

class AddRelation(forms.ModelForm):
    class Meta():
        model=Relation
        fields=['name']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),   
        }
