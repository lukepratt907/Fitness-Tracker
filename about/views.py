from django.shortcuts import render
from .models import GymInfo
from metrics.models import EQUIPMENT, MACHINES

# Create your views here.

def about_page(request):
    # Create a GymInfo instance with the hardcoded description and year
    gym_info = GymInfo.objects.create(
        description="Mac's Strength and Power",
        year_established=2022
    )

    # Pass the equipment lists and gym_info to the template context
    return render(request, 'about/about_page.html', {'gym_info': gym_info, 'equipment_list': EQUIPMENT, 'machines_list': MACHINES})
