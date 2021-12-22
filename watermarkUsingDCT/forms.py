from django import forms 
from .models import *

class QrcodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = ['Qrcodeimg']
    
    def __init__(self, *args, **kwargs):
        super(QrcodeForm, self).__init__(*args, **kwargs)
        self.fields['Qrcodeimg'].label = "Upload Qr Code Image"


class WaterMarkForm(forms.ModelForm): 
  
    class Meta: 
        model = WaterMark 
        fields = ['coverImg','watermarkImg']    
        
        
    def __init__(self, *args, **kwargs):
        super(WaterMarkForm, self).__init__(*args, **kwargs)
        self.fields['coverImg'].label = "Upload Cover Image"
        self.fields['watermarkImg'].label = "Upload Watermark Image"
        # self.fields['coverImg'].widget.attrs.update({'label' : 'Upload Cover Image'})
        # self.fields['watermarkImg'].widget.attrs.update({'label' : 'form-control-file'})


