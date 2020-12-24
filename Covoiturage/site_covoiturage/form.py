from django.forms import ModelForm
from .models import Trajet


class TrajetForm(ModelForm):
    class Meta:
        model = Trajet
        fields = ['conducteur', 'title', 'depart', 'arrive', 'lieu_depart', 'lieu_arrive', 'pri']
