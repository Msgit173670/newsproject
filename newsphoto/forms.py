from django.forms import ModelForm
from .models import newsPhotoPost

class newsPhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = newsPhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
