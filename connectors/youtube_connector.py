import requests
from config.settings import YOUTUBE_API_KEY

def buscar_videos_youtube(query: str, max_results: int = 5) -> list:
    """
    Busca videos relevantes en YouTube utilizando la API oficial v3.
    """
    if not YOUTUBE_API_KEY:
        print("⚠️ Advertencia: YOUTUBE_API_KEY no está configurada en el .env. Modo simulación activado.")
        return []

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY,
        "relevanceLanguage": "es"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        videos = []
        for item in data.get("items", []):
            videos.append({
                "video_id": item["id"]["videoId"],
                "titulo": item["snippet"]["title"],
                "canal": item["snippet"]["channelTitle"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })
        return videos
    except Exception as e:
        print(f"Error al conectar con YouTube Search API: {e}")
        return []

def obtener_comentarios_video(video_id: str, max_comentarios: int = 20) -> list:
    """
    Extrae los comentarios públicos accesibles de un video específico de YouTube de forma oficial.
    """
    if not YOUTUBE_API_KEY:
        return []

    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": max_comentarios,
        "key": YOUTUBE_API_KEY,
        "textFormat": "plainText"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        comentarios = []
        for item in data.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comentarios.append({
                "autor": snippet["authorDisplayName"],
                "texto": snippet["textDisplay"],
                "fecha": snippet["publishedAt"]
            })
        return comentarios
    except Exception as e:
        print(f"Error al extraer comentarios del video {video_id}: {e}")
        return []