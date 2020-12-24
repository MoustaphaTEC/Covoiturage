from django.db import models


# Create your models here.
class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Personne(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

    def __str__(self):
        return self.prenom

    class Meta:
        abstract = True


class Conduc(Personne):
    nb_place = models.IntegerField()


class Trajet(TimespamtedModel):
    conducteur = models.ForeignKey(Conduc, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    depart = models.DateTimeField('date départ')
    arrive = models.DateTimeField("date d'arrivée")
    lieu_depart = models.CharField(max_length=255)
    lieu_arrive = models.CharField(max_length=255)
    pri = models.IntegerField()

    def __str__(self):
        return self.lieu_depart

    def __str__(self):
        return self.lieu_arrive

    def __str__(self):
        return self.title


class Passager(Personne):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
