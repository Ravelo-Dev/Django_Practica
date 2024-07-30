from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=50)
    description = forms.CharField(label="Descripcion", max_length=500, required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)