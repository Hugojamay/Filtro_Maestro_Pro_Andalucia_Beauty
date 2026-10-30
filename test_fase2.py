from intelligence.openai_brain import analizar_comentario_prospecto

if __name__ == "__main__":
    print("--- PROBANDO FASE 2: CEREBRO MAESTRO Y ANTIBASURA ---")
    
    comentarios_prueba = [
        "Hola, tengo líneas de expresión muy marcadas alrededor de los ojos y busco un sérum antiedad efectivo. ¿Tienen envíos en Guadalajara?",
        "Mi tía sufre de acné severo, ¿qué le recomiendan?", # Caso sobre terceros (debe rechazarse)
        "Jajaja la crema milagrosa que no sirve para nada", # Ironía / spam (debe rechazarse)
        "Me urge una crema hidratante para piel seca, ¿cuál es su costo y cómo la compro?"
    ]
    
    for i, texto in enumerate(comentarios_prueba, 1):
        print(f"\n--- Comentario {i} ---")
        print(f"Texto: \"{texto}\"")
        resultado = analizar_comentario_prospecto(texto)
        print("Resultado del Análisis Maestro:", resultado)