from django.forms import ModelForm

from . models import Contact

class ContactForm(ModelForm):
    """
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs['disabled'] = 'disabled'
    """
    class Meta:
        model = Contact
        
        fields = ['first_name','last_name','active','profile_picture','email','phone', 'customer']
        labels = {
                'first_name':'Nombre',
                'last_name':'Apellido',
                'active':'Activo',
                'profile_picture':'Foto',
                'email':'Email',
                'phone':'Teléfono'
            }
        #readonly_fields = ('customer',)
