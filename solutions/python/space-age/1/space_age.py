def round_two_numbers(number):
    rounded_number = int(number*1000) % 10
    return round(number, 2) if rounded_number != 5 else round((number-0.001), 2)
planets = {
    'mercury' :	0.2408467, 
    'venus':	0.61519726,
    'earth': 1.0,
    'mars':	1.8808158,
    'jupiter':	11.862615,
    'saturn': 29.447498,
    'uranus':	84.016846,
    'neptune':	164.79132
}

def calculate_planet(number, planet):
    return round_two_numbers(number/(31556926*planets[planet]))
    
class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        return calculate_planet(self.seconds, 'earth')
    
    def on_mercury(self):
        return calculate_planet(self.seconds, 'mercury')
    
    def on_venus(self):
        return calculate_planet(self.seconds, 'venus')

    def on_mars(self):
       return calculate_planet(self.seconds, 'mars')

    def on_jupiter(self):
        return calculate_planet(self.seconds, 'jupiter')
        
    def on_saturn(self):
        return calculate_planet(self.seconds, 'saturn')

    def on_uranus(self):
        return calculate_planet(self.seconds, 'uranus')

    def on_neptune(self):
        return calculate_planet(self.seconds, 'neptune')