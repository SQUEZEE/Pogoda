from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

gorod = input('Введите ваш город : ')




owm = OWM('c2d17363d701a52c453a2296a475fcb5')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(gorod)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
temperature = w.temperature('celsius')['temp']

if temperature > 20.0:
	print('Нормас можешь идти гулять')
elif temperature < 0:
	print('На улице холодрыга сиди дома')
else:
	print('На улице холодно оденься по теплее')	

print('Облачность : ' + w.detailed_status)	

print('Температура : ' + str(temperature) + ' градусов')	

