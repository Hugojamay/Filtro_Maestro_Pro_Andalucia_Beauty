import time
from connectors.youtube_connector import buscar_videos_youtube, obtener_comentarios_video
from intelligence.openai_brain import analizar_comentario_prospecto
from crm.crm_manager import registrar_prospecto_detectado
from config.settings import YOUTUBE_API_KEY

QUERIES_SKINCARE = [
    "cómo quitar manchas de paño en la cara",
    "remedios para manchas oscuras piel",
    "sérum antiedad arrugas opiniones",
    "crema para acné y manchas"
]

def ejecutar_ciclo_autonomo():
    print("🤖 [AGENTE AUTÓNOMO] Iniciando ciclo de escucha y prospección en tiempo real...")
    
    if not YOUTUBE_API_KEY:
        print("⚠️ Advertencia: YOUTUBE_API_KEY está vacía en el .env (Modo simulación o requiere clave real).")

    total_analizados = 0
    total_prospectos = 0

    for query in QUERIES_SKINCARE:
        print(f"\n🔍 Buscando videos en YouTube para: \"{query}\"...")
        videos = buscar_videos_youtube(query, max_results=2)
        
        for vid in videos:
            print(f"   📺 Analizando video: {vid['titulo']} (Canal: {vid['canal']})")
            comentarios = obtener_comentarios_video(vid['video_id'], max_comentarios=15)
            
            for c in comentarios:
                total_analizados += 1
                texto_comentario = c["texto"]
                autor_comentario = c["autor"]
                
                # Análisis mediante Cerebro Maestro y Antibasura
                resultado = analizar_comentario_prospecto(texto_comentario)
                
                if resultado.get("es_prospecto_valido", False):
                    guardado = registrar_prospecto_detectado(autor_comentario, resultado)
                    if guardado:
                        total_prospectos += 1
                        print(f"      🎯 ¡NUEVO PROSPECTO CAPTURADO! [{resultado.get('scoring_comercial')} pts] de {autor_comentario}")
                        print(f"         Evidencia: \"{resultado.get('evidencia_literal')}\"")
                
                time.sleep(0.5)

    print(f"\n✨ [CICLO FINALIZADO] Se analizaron {total_analizados} comentarios en total.")
    print(f"💾 Se guardaron {total_prospectos} nuevos prospectos comerciales en el CRM de SQLite.")

if __name__ == "__main__":
    ejecutar_ciclo_autonomo()