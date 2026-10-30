import os
from dotenv import load_dotenv

# Carga las variables del archivo .env desde la raíz
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

if not OPENAI_API_KEY:
    raise ValueError("⚠️ No se encontró la OPENAI_API_KEY en las variables de entorno (.env). Configúrala para continuar.")