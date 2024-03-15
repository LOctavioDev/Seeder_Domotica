from datetime import datetime, timedelta
from data import sensores, actuadores
import random
from utiles import random_number_ranges, random_number_decimal_ranges, generate_location, generate_random_date, print_styled

def count_sensor_actuador(data, tipo, habitacion):
    total = 0
    for item in data:
        if item.get('type') == tipo and item.get('location') == habitacion:  
            total += 1
    return total



def generate_sensor_readings(room=None, sensor_name=None, value=None, propiedad=None, valor=None):
    if room is None:
        room = generate_location()

    if sensor_name is None:
        sensor_name = sensores[random_number_ranges(0, len(sensores) - 1)]['name']

    if sensor_name not in ["Temperatura y Humedad", "Fotoresistencia", "PIR", "Ultrasonico"]:
        return "Invalid sensor"

    if not any(sensor['name'] == sensor_name for sensor in sensores):
        return "Invalid sensor"

    if room not in ["Recámara 1", "Recámara 2", "Recámara 3", "Baño 1", "Baño 2", "Cocina", "Sala", "Garage"]:
        return "Invalid location"

    if value is None:
        if sensor_name == "Temperatura y Humedad":
            value = {
                "temperatura": random_number_decimal_ranges(0, 50, 2),
                "humedad": random_number_ranges(20, 80),
                "fecha": {"$date": generate_random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))}
            }
        elif sensor_name == "Fotoresistencia":
            value = {
                "luz": random_number_ranges(0, 1023),
                "fecha": {"$date": generate_random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))}
            }
        elif sensor_name == "PIR":
            value = {
                "movimiento": random.choice([True, False]),
                "fecha": {"$date": generate_random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))}
            }
        elif sensor_name == "Ultrasonico":
            value = {
                "distancia": random_number_decimal_ranges(0, 5, 2),
                "fecha": {"$date": generate_random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))}
            }
        else:
            return "Invalid sensor"

    if propiedad and valor:
        value[propiedad] = valor

    return {
        "room": room,
        "sensor": sensor_name,
        "value": value
    }



def generate_actuator_actions(room, actuator_name, value=None):
    if room is None:
        room = generate_location()

    if value is None:
        for actuator in actuadores:
            if actuator['name'] == actuator_name:
                specific_actions = actuator['specificactions']
                value = {}
                for action in specific_actions:
                    
                    min_value = int(action['minValue'])
                    max_value = int(action['maxValue'])
                    value[action['name']] = random_number_ranges(min_value, max_value)
                value['fecha'] = {"$date": generate_random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))}
                break
        else:
            return "Actuator not found"

    return {
        "room": room,
        "actuator": actuator_name,
        "value": value
    }
