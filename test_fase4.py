from intelligence.openai_brain import analizar_comentario_prospecto
from crm.crm_manager import registrar_prospecto_detectado, listar_prospectos_crm

if __name__ == "__main__":
    print("--- PROBANDO FASE 4: BASE DE DATOS Y CRM ---")
    
    # Simulamos comentarios detectados por el radar social
    comentarios_simulados = [
        {"autor": "Karla Gómez", "texto": "Hola, tengo líneas de expresión muy marcadas y busco un sérum antiedad efectivo. ¿Cómo lo compro?"},
        {"autor": "Lucía Méndez", "texto": "Me urge una crema hidratante para piel seca, ¿cuál es su costo?"}
    ]
    
    print("\n[+] Analizando y guardando prospectos en SQLite...")
    for item in comentarios_simulados:
        resultado = analizar_comentario_prospecto(item["texto"])
        if resultado.get("es_prospecto_valido"):
            registrado = registrar_prospecto_detectado(item["autor"], resultado)
            print(f"    - Prospecto de {item['autor']} guardado exitosamente: {registrado}")

    print("\n[+] Consultando el CRM (Prospectos ordenados por Scoring):")
    prospectos_crm = listar_prospectos_crm()
    for p in prospectos_crm:
        print(f"    * [{p['scoring']} pts] {p['autor']} ({p['categoria']}): \"{p['evidencia']}\" - Estado: {p['estado']}")