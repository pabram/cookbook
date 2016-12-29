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
    name = forms.CharField(max_length=128, help_text="Nazwa potrawy.")
    # content = forms.TextField(max_length=1024, help_text="Tutaj umieść swój przepis.")
    description = forms.CharField(max_length=300, help_text="Krótki opis potrawy")
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