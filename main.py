from data import sensores, actuadores
from colorama import Fore, Style
from seeder import count_sensor_actuador, generate_sensor_readings, generate_actuator_actions
from utiles import print_styled


# TOTAL DE SENSORES DE UNA HABITACION
total_sensores_recamara_1 = count_sensor_actuador(sensores, 'Sensor', 'Recámara 1')
print_styled("Total de sensores en Recámara 1: ", Fore.GREEN, Style.BRIGHT)
print_styled(str(total_sensores_recamara_1))

# TOTAL DE ACTUADORES DE UNA HABITACION
total_actuadores_cocina = count_sensor_actuador(actuadores, 'Actuador', 'Cocina')
print_styled("\nTotal de actuadores en Cocina: ", Fore.GREEN, Style.BRIGHT)
print_styled(str(total_actuadores_cocina))


# LECTURAS ALEATORIAS DEL SENSOR
print_styled("\nGenerando lectura de sensor aleatoria:", Fore.YELLOW, Style.NORMAL)
print_styled(str(generate_sensor_readings(None, None, None)))

# LECTRAS ALEATORIAS DEL ACUTADOR
print_styled("\nGenerando acción de actuador aleatoria:", Fore.YELLOW, Style.NORMAL)
print_styled(str(generate_actuator_actions("Cocina", "Servomotor")))
