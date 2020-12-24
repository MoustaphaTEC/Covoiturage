from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Trajet, Conduc, Passager
from .form import TrajetForm

trajet = Trajet.objects.all()
conduc = Conduc.objects.all()
passager = Passager.objects.all()


def index(request):
    return render(request, 'blog/index.html', {'trajets': trajet})


def show(request, id):
    tra_id = get_object_or_404(trajet, pk=id)
    # p = 0
    # for pl in conduc:
    #     if pl == tra_id.Passager.trajet.conducteur:
    #         p = p + 1
    #     place = conduc.nb_place - p
    return render(request, 'blog/afficheTrajet.html', {'trajet': tra_id, 'passagers': passager})


def trajetoire(request):
    return render(request, 'blog/trajetoire.html', {'trajets': trajet})


def afficheConducteur(request, id):
    cond_id = get_object_or_404(conduc, pk=id)
    return render(request, 'blog/afficheConducteur.html', {'cond_id': cond_id, 'trajets': trajet})


def conducteur(request):
    place = 0
    return render(request, 'blog/conducteur.html', {'conducteurs': conduc, 'trajets': trajet, 'place': place})


def passage(request):
    return render(request, 'blog/passager.html', {'passagers': passager, 'trajets': trajet})


def affichePassager(request, id):
    pass_id = get_object_or_404(passager, pk=id)
    return render(request, 'blog/affichePassager.html', {'pass_id': pass_id, 'trajets': trajet})


def creation(request, id):
    tra_id = get_object_or_404(trajet, pk=id)

    if request.method == "POST":
        form = TrajetForm(request.POST).save()
        return redirect('conducteur')
    else:
        form = TrajetForm()
    return render(request, 'blog/creation.html', {'trajet': tra_id, 'form': form})


def modifier(request, id):
    tra_id = get_object_or_404(trajet, pk=id)
    return render(request, 'blog/modifier.html', {'trajet': tra_id, 'passagers': passager})


def supprimer(request, id):
    tra_id = get_object_or_404(trajet, pk=id)
    liste = []
    for p in passager:
        liste = p.trajet.title

    nbre = liste.count(tra_id.title)
    nbre = nbre + 1
    return render(request, 'blog/supprimer.html', {'trajet': tra_id, 'passagers': passager, 'nbre': nbre})


# conducteur = request.POST.get('conducteur', '')
#         title = request.POST.get('title', '')
#         depart = request.POST.get('depart_0', '')
#         created_at = request.POST.get('depart_1', '')
#         arrive = request.POST.get('arrive_0', '')
#         updated_at = request.POST.get('arrive_1', '')
#         lieu_depart = request.POST.get('lieu_depart', '')
#         lieu_arrive = request.POST.get('lieu_arrive', '')
#         pri = request.POST.get('pri', '')
#         return redirect('/')