def validar_cita_en_texto(texto_original: str, evidencia_literal: str) -> bool:
    """
    Verifica estrictamente que la evidencia literal devuelta por la IA
    exista textualmente dentro del comentario original para evitar alucinaciones.
    Se normalizan las cadenas a minúsculas y se quitan espacios excedentes.
    """
    if not evidencia_literal or not texto_original:
        return False
        
    texto_limpio = texto_original.strip().lower()
    evidencia_limpia = evidencia_literal.strip().lower()
    
    return evidencia_limpia in texto_limpio