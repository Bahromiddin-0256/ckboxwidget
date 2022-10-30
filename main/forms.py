from django.forms import ModelForm
from main.models import Article
from widgets import CKBoxWidget


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

        widgets = {
            "description": CKBoxWidget()
        }
