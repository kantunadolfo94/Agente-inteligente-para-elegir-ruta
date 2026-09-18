# Rutas disponibles
rutas = [
    {
        "nombre": "Ruta A",
        "distancia": 5,
        "tiempo": 10,
        "trafico": 1
    },
    {
        "nombre": "Ruta B",
        "distancia": 3,
        "tiempo": 15,
        "trafico": 3
    },
    {
        "nombre": "Ruta C",
        "distancia": 7,
        "tiempo": 8,
        "trafico": 1
    }
]

#heuristias

def calcular_heuristica(ruta):
    
    puntuacion = (
        ruta["distancia"] * 0.4 +
        ruta["tiempo"] * 0.4 +
        ruta["trafico"] * 2
        
    )
    
    return puntuacion

#analizamos las rutad

mejor_ruta = None
mejor_puntuacion = 999
