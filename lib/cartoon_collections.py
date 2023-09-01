def roll_call_dwarves(dwarves):
    for idx, dwarf in enumerate(dwarves):
        print(f'{idx + 1}. {dwarf}')

def summon_captain_planet(calls):
    return [f'{call.capitalize()}!' for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(items):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for item in items:
        if item in cheeses:
            return item
    return None
