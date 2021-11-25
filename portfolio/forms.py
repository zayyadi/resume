from django import forms
from .models import Blog, ContactProfile

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["name","author", "body","image", "description"]
        widgets = {
            
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'zayyad', 'type':'hidden'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }

class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'class': 'form-control',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)