def calcular_scoring_prospecto(analisis_ia: dict) -> int:
    """
    Calcula el puntaje comercial (0 a 100) basado en criterios estrictos:
    - Necesidad personal: 30 pts
    - Búsqueda activa: 30 pts
    - Intención comercial: 30 pts
    - Nivel de confianza del modelo: 10 pts (proporcional)
    """
    if not analisis_ia.get("es_prospecto_valido", False):
        return 0
        
    puntaje = 0
    
    if analisis_ia.get("necesidad_personal", False):
        puntaje += 30
        
    if analisis_ia.get("busqueda_activa", False):
        puntaje += 30
        
    if analisis_ia.get("intencion_comercial", False):
        puntaje += 30
        
    # Bonificación por nivel de confianza (hasta 10 puntos)
    confianza = analisis_ia.get("confianza", 0)
    puntaje += int((confianza / 100) * 10)
    
    return min(puntaje, 100)