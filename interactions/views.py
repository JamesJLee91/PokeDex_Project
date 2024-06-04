from django.shortcuts import render
from django.http import HttpResponse
from .type_instances import type_dict, all_types


def index(request):
    resistance = {}
    weakness = {}
    super_effective = {}
    not_effective = {}
    type_input = ""

    if request.method == 'POST':
        type_input = request.POST.get('type_input').strip().lower()
        type_names = [t.strip() for t in type_input.split(",")]

        type1_name = type_names[0]
        type2_name = type_names[1] if len(type_names) > 1 else None

        type1 = type_dict.get(type1_name)
        type2 = type_dict.get(type2_name) if type2_name else None

        if not type1:
            return HttpResponse(f"Type {type1_name} not found", status=400)
        if type2_name and not type2:
            return HttpResponse(f"Type {type2_name} not found", status=400)

        resistance, weakness = print_defensive_interactions(type1, type2)
        super_effective, not_effective = print_offensive_interactions(type1, type2)

        # Debug statements
        print(f"Type 1: {type1.name}")
        print(f"Type 2: {type2.name if type2 else 'None'}")
        print(f"Resistance: {resistance}")
        print(f"Weakness: {weakness}")
        print(f"Super Effective: {super_effective}")
        print(f"Not Effective: {not_effective}")

    return render(request, 'index.html', {
        'type_input': type_input,
        'resistance': resistance,
        'weakness': weakness,
        'super_effective': super_effective,
        'not_effective': not_effective

    })


# Defensive
def print_defensive_interactions(type1, type2=None):
    resistance = {}
    weakness = {}
    for other_type in all_types:
        if type2:
            effectiveness = other_type.get_effectiveness(type1) * other_type.get_effectiveness(type2)
        else:
            effectiveness = other_type.get_effectiveness(type1)
        if effectiveness < 1.0:
            resistance[f"{other_type} ({effectiveness:.1f})"] = effectiveness
        elif effectiveness > 1.0:
            weakness[f"{other_type} ({effectiveness:.1f})"] = effectiveness
    return resistance, weakness


# Offensive
def print_offensive_interactions(type1, type2=None):
    super_effective = {}
    not_effective = {}
    for other_type in all_types:
        if type2:
            effectiveness1 = type1.get_effectiveness(other_type)
            effectiveness2 = type2.get_effectiveness(other_type)
            effectiveness = max(effectiveness1, effectiveness2)
        else:
            effectiveness = type1.get_effectiveness(other_type)
        if effectiveness < 1.0:
            not_effective[f"{other_type} ({effectiveness:.1f})"] = effectiveness
        elif effectiveness == 2.0:
            super_effective[f"{other_type} ({effectiveness:.1f})"] = effectiveness
    return super_effective, not_effective
