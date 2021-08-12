from django import forms

from recipe_app.models import Author

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)

class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
