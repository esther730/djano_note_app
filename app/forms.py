"""
Definition of forms.
"""


from django import forms
from .models import Note



class NoteForm(forms.ModelForm):

     class Meta:
         model = Note
         fields = ("subject", "priority", "detail")
         widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control note-editor__subject-input'
                }),
            'priority': forms.Select(attrs={
                'class': 'form-control note-editor__priority-input'
                }),
            'detail': forms.Textarea(attrs={
                'class': 'form-control note-editor__detail-input', 
                'rows':'12',
                'cols':'20',
                }),
         }
