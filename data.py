from datetime import datetime

sensores =  [
    {
        "type": "Sensor", 
        "name": "Temperatura y Humedad",
        "brand": "Genérico", 
        "model": "DHT-11", 
        "specificactions": [
            {
                "name": "Rango Temperatura", 
                "maxValue": 0 ,
                "minValue": 50,
                "meausurementUnit": "°C", 
                "acurrancy" : "+-2"
            },
            {   
                "name": "Rango de Humedad", 
                "maxValue": 20, 
                "minValue": 80, 
                "meausurementUnit": "% HR",
                "acurrancy" : "+-5"
            }, 
            {
                "name": "Alimentación de Energía", 
                "maxValue": 5, 
                "minValue": 3.3, 
                "meausurementUnit": "V"
            },
            
        ],
        "location": "Recámara 1",
        "status": "Disponible",
        "initialDate": {"$date": datetime(2024, 3, 7, 8, 0, 0)},  #REVISAR COMPATIBILIDAD CON MONGO
        "owner": "SI",

    },

    {
        "name": "Fotoresistencia",
        "type": "Sensor", 
        "brand": "Genérico", 
        "model": "LDR", 
        "specificactions": [
            
        ],
        "owner": "SI",
        "location": "Recámara 1"
    },
    {
        "name": "Temperatura y Humedad",
        "type": "Sensor", 
        "brand": "Genérico", 
        "model": "DHT-11", 
        "specificactions": [
            
        ],
        "owner": "JD-NESH",
        "location": "Recámara 2"
    },
    {
        "name": "Fotoresistencia",
        "type": "Sensor", 
        "brand": "Genérico", 
        "model": "LDR", 
        "specificactions": [
            
        ],
        "owner": "JD-NESH",
        "location": "Recámara 2"
    },
        {
        "name": "Temperatura y Humedad",
        "type": "Sensor", 
        "brand": "Genérico", 
        "model": "DHT-11", 
        "specificactions": [
            
        ],
        "owner": "MAHITECH",
        "location": "Recámara 3"
    },
    {
        "name": "Fotoresistencia",
        "type": "Sensor", 
        "brand": "Genérico", 
        "model": "LDR", 
        "specificactions": [
            
        ],
        "owner": "MAHITECH",
        "location": "Recámara 3"
    }
]


actuadores = [
    {
        "type": "Actuador",
        "name": "Servomotor",
        "brand": "Genérico",
        "model": "Modelo del Servomotor",
        "specificactions": [
            {
                "name": "Ángulo de Rotación",
                "maxValue": 180,
                "minValue": 0,
                "meausurementUnit": "grados",
                "acurrancy": "+-2"
            },
            {
                "name": "Alimentación de Energía", 
                "maxValue": 5,
                "minValue": 3.3,
                "meausurementUnit": "V"
            }
        ],
        "location": "Cocina",
        "status": "Disponible",
        "initialDate": {"$date": datetime(2024, 3, 7, 8, 0, 0)},
        "owner": "TechCorp"
    },
    {
        "type": "Actuador",
        "name": "Relay",
        "brand": "Genérico",
        "model": "Modelo del Relay",
        "specificactions": [
            {
                "name": "Voltaje de Activación",
                "maxValue": 5,
                "minValue": 3.3,
                "meausurementUnit": "V"
            }
        ],
        "location": "Baño",
        "status": "Disponible",
        "initialDate": {"$date": datetime(2024, 3, 7, 8, 0, 0)},
        "owner": "TechSoft"
    },
    {
        "type": "Actuador",
        "name": "Ventilador",
        "brand": "Genérico",
        "model": "Modelo del Ventilador",
        "specificactions": [
            {
                "name": "Velocidad",
                "maxValue": 3,
                "minValue": 0,
                "meausurementUnit": "Niveles"
            },
            {
                "name": "Alimentación de Energía",
                "maxValue": 5,
                "minValue": 3.3,
                "meausurementUnit": "V"
            }
        ],
        "location": "Sala",
        "status": "Disponible",
        "initialDate": {"$date": datetime(2024, 3, 7, 8, 0, 0)},
        "owner": "TechInd"
    }
]


ubicaciones = ["Recámara 1", "Recámara 2", "Recámara 3", "Baño 1", "Baño 2", "Cocina", "Sala", "Garage"]