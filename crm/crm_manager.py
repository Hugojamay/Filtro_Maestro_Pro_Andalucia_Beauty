from database.db_manager import guardar_prospecto, obtener_todos_prospectos

def registrar_prospecto_detectado(autor: str, resultado_analisis: dict) -> bool:
    """
    Toma el resultado del Cerebro Maestro y lo registra en el CRM si es válido.
    """
    if not resultado_analisis.get("es_prospecto_valido", False):
        return False
        
    guardado = guardar_prospecto(
        autor=autor,
        texto=resultado_analisis.get("evidencia_literal", ""), # o texto completo
        categoria=resultado_analisis.get("categoria_skincare", "ninguna"),
        evidencia=resultado_analisis.get("evidencia_literal", ""),
        scoring=resultado_analisis.get("scoring_comercial", 0)
    )
    
    return guardado

def listar_prospectos_crm() -> list:
    """
    Devuelve la lista completa de prospectos en el CRM.
    """
    return obtener_todos_prospectos()