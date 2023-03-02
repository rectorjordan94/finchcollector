from django.shortcuts import render
from.models import Finch

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
    return render(request, 'finches/detail.html', { 'finch': finch })