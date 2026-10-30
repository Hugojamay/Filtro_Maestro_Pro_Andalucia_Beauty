from intelligence.openai_brain import analizar_comentario_prospecto
from connectors.youtube_connector import buscar_videos_youtube, obtener_comentarios_video
from config.settings import YOUTUBE_API_KEY

if __name__ == "__main__":
    print("--- PROBANDO FASE 3: ESCUCHA SOCIAL Y FILTRADO AUTOMÁTICO ---")
    
    comentarios_a_probar = []

    if YOUTUBE_API_KEY:
        print("\n[+] Conectando a YouTube Data API oficial...")
        videos = buscar_videos_youtube("cómo quitar manchas de paño en la cara", max_results=1)
        if videos:
            vid = videos[0]
            print(f"Video encontrado: {vid['titulo']} ({vid['url']})")
            comentarios_raw = obtener_comentarios_video(vid['video_id'], max_comentarios=10)
            comentarios_a_probar = [c["texto"] for c in comentarios_raw]
    
    # Si no hay API Key configurada aún, usamos comentarios de prueba realistas
    if not comentarios_a_probar:
        print("\n[i] Usando set de comentarios de prueba (Modo Simulación YouTube)...")
        comentarios_a_probar = [
            "Excelente video, saludos desde CDMX.", # Ruido / spam
            "Oigan una duda, ¿alguien sabe si el retinol sirve para las arrugas?", # Educativo/Curiosidad
            "Hola chicas, la verdad gasté mucho en dermatólogos y sigo con las manchas oscuras en los pómulos, ¿qué crema me recomiendan comprar que sea efectiva?", # Prospecto Válido
            "Muy buen contenido, me encantó la explicación del bloqueador solar." # Educativo
        ]

    print(f"\nProcesando {len(comentarios_a_probar)} comentarios a través del Cerebro Maestro...\n")
    
    prospectos_validos = 0
    for idx, texto in enumerate(comentarios_a_probar, 1):
        print(f"[{idx}] Comentario: \"{texto}\"")
        resultado = analizar_comentario_prospecto(texto)
        
        if resultado.get("es_prospecto_valido"):
            prospectos_validos += 1
            print(f"    🎯 ¡PROSPECTO DETECTADO! (Score: {resultado.get('scoring_comercial')} pts)")
            print(f"    - Categoría: {resultado.get('categoria_skincare')}")
            print(f"    - Evidencia: \"{resultado.get('evidencia_literal')}\"")
        else:
            print(f"    ❌ Descartado: {resultado.get('razon_rechazo')}")
        print("-" * 50)

    print(f"\nResumen de Escucha: {prospectos_validos} prospectos comerciales válidos encontrados de {len(comentarios_a_probar)} analizados.")