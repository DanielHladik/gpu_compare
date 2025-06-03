from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import GraphicsCard, UpscalingTechnology
from django.http import JsonResponse

def home(request):
    return render(request, 'cards/home.html')

def card_list(request):
    manufacturer = request.GET.get('manufacturer')
    tech = request.GET.get('technology')
    search = request.GET.get('search')
    cards = GraphicsCard.objects.all()
    if manufacturer:
        cards = cards.filter(manufacturer=manufacturer)
    if tech:
        cards = cards.filter(supported_technologies__name=tech)
    if search:
        cards = cards.filter(name__icontains=search)
    return render(request, 'cards/card_list.html', {'cards': cards})

def card_detail(request, pk):
    card = get_object_or_404(GraphicsCard, pk=pk)
    return render(request, 'cards/card_detail.html', {'card': card})

def technology_detail(request, pk):
    tech = get_object_or_404(UpscalingTechnology, pk=pk)
    return render(request, 'cards/technology_detail.html', {'tech': tech})

def compare(request):
    # Porovnání dvou karet podle ID v GET parametrech
    card1_id = request.GET.get('card1')
    card2_id = request.GET.get('card2')
    card1 = GraphicsCard.objects.filter(pk=card1_id).first() if card1_id else None
    card2 = GraphicsCard.objects.filter(pk=card2_id).first() if card2_id else None
    all_cards = GraphicsCard.objects.all()
    return render(request, 'cards/compare.html', {
        'card1': card1,
        'card2': card2,
        'all_cards': all_cards,
    })

# API endpoint pro AJAX porovnání
def compare_api(request):
    card1_id = request.GET.get('card1')
    card2_id = request.GET.get('card2')
    card1 = GraphicsCard.objects.filter(pk=card1_id).first() if card1_id else None
    card2 = GraphicsCard.objects.filter(pk=card2_id).first() if card2_id else None
    def card_data(card):
        if not card:
            return None
        return {
            'name': card.name,
            'manufacturer': card.manufacturer,
            'memory_gb': card.memory_gb,
            'memory_type': card.memory_type,
            'price': float(card.price),
            'benchmark_index': card.benchmark_index,
            'technologies': [f"{t.name} {t.version}" for t in card.supported_technologies.all()],
        }
    return JsonResponse({
        'card1': card_data(card1),
        'card2': card_data(card2),
    })
