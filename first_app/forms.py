from django import forms
from  first_app.models import  Topic
class URLForm(forms.ModelForm):
      class Meta:
          model = Topic
          fields=['url_name']
