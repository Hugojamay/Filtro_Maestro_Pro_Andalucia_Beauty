from intelligence.openai_brain import analizar_comentario_prospecto

if __name__ == "__main__":
    print("--- PROBANDO CONEXIÓN Y CEREBRO GPT MINI ---")
    
    # Caso de prueba 1: Prospecto válido con las tres señales
    texto_prueba_1 = "Hola, la verdad estoy buscando algo urgente para las manchas de paño que me salieron en las mejillas por el sol, ¿qué crema me recomiendan y dónde la puedo comprar?"
    print(f"\nAnalizando texto 1: \"{texto_prueba_1}\"")
    resultado_1 = analizar_comentario_prospecto(texto_prueba_1)
    print("Resultado JSON:", resultado_1)

    # Caso de prueba 2: Contenido educativo / ruido (debe ser rechazado)
    texto_prueba_2 = "El ácido hialurónico sirve para retener la humedad en la piel de forma cosmética."
    print(f"\nAnalizando texto 2: \"{texto_prueba_2}\"")
    resultado_2 = analizar_comentario_prospecto(texto_prueba_2)
    print("Resultado JSON:", resultado_2)