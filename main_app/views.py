from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from.models import Finch, Food
from .forms import SightingForm

# finches =[
#     {'name': 'European Goldfinch', 'wingspan': '21-25 cm', 'weight': '14-19 g', 'description': 'Male European goldfinches can often be distinguished by a larger, darker red mask that extends just behind the eye. The shoulder feathers are black, whereas they are brown on the female. In females, the red face does not extend past the eye. The ivory-coloured bill is long and pointed, and the tail is forked.'},
#     {'name': 'Hawfinch', 'wingspan': '29-33 cm', 'weight': '46-70 g', 'description': 'It is a robust bird with a thick neck, large round head and a wide, strong conical beak with a metallic appearance. It has short pinkish legs with a light hue and it has a short tail. It has brown eyes. The plumage of the female is slightly paler than that of the male. The overall colour is light brown, its head having an orange hue to it.'},
# ]

# Create your views here.

# define the home view
def home(request):
    # include an.html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    id_list = finch.foods.all().values_list('id')
    foods_finch_doesnt_have = Food.objects.exclude(id__in=id_list)

    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'sighting_form': sighting_form, 'foods': foods_finch_doesnt_have })

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'wingspan', 'weight', 'description']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['wingspan', 'weight', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)

    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.add(food_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.remove(food_id)
    return redirect('detail', finch_id=finch_id)

class FoodList(ListView):
    model = Food
    template_name = 'foods/index.html'

class FoodDetail(DetailView):
    model = Food
    template_name = 'foods/detail.html'

class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'color']

class FoodDelete(DeleteView):
    model = Food
    success_url = '/foods/'