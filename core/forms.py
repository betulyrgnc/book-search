from django import forms

from core.models import Bookmark

PARAMETER_CHOICES = (
    ('Tümü', 'Tümü'),
    ('İsim', 'İsim')   
)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search query', max_length=255)
    parameter = forms.ChoiceField(label='Search parameter', choices=PARAMETER_CHOICES)

class AddBookmarkForm(forms.ModelForm):
    title = forms.CharField(max_length=255)

    class Meta:
        model = Bookmark
        fields = ('title',)

    def exist_in_database(self, title):
         return True if title in [ i.title for i in Bookmark.objects.all()] else False

    def save(self, commit=True):
        bookmark_instance = super(AddBookmarkForm, self).save(commit=False)

        if commit:
            title = self.cleaned_data['title']
            #Burada veritabanında olup olmadığı kontrolü yapılıyor ve kaydediliyor
            if not self.exist_in_database(title):
                bookmark_instance.title = title
                bookmark_instance.save()
            else:
                bookmark_instance = Bookmark.objects.get(title=title)
                bookmark_instance.save()

        return bookmark_instance