from django import forms
from recipes.models import Category, Recipe

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Wpisz nazwę kategorii.")
    views = forms.CharField(widget=forms.HiddenInput(), initial=0)
    likes = forms.CharField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class RecipeForm(forms.ModelForm):
    photo = forms.FileField(required=False, help_text="Dodaj zdjęcie swojej potrawy")
    name = forms.CharField(max_length=128, help_text="Nazwa potrawy.")
    description = forms.CharField(max_length=300, help_text="Krótki opis potrawy")
    content = forms.CharField(widget=forms.Textarea, help_text="Tutaj umieść swój przepis")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)



    class Meta:
        model = Recipe
        exclude = ('category', 'slug',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data