import json
from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL
from intelligence.evidence_validator import validar_cita_en_texto
from processing.scoring_engine import calcular_scoring_prospecto

client = OpenAI(api_key=OPENAI_API_KEY)

def analizar_comentario_prospecto(texto_comentario: str) -> dict:
    """
    Motor maestro de análisis anti-basura de Andalucía Beauty.
    Evalúa las tres señales, exige JSON estricto, valida la evidencia por código
    y calcula el scoring comercial.
    """
    prompt_sistema = """
    Eres el motor maestro de análisis anti-basura de Andalucía Beauty. 
    Tu trabajo es evaluar comentarios públicos y detectar exclusivamente prospectos reales que cumplan simultáneamente:
    1. Necesidad personal comprobable (la persona habla de su propia piel).
    2. Búsqueda activa de solución.
    3. Intención comercial explícita.
    
    Debes rechazar estrictamente contenido educativo, ironías, spam, preguntas sobre terceros o consultas médicas generales.
    Devuelve un JSON válido con la siguiente estructura exacta:
    {
        "es_prospecto_valido": true/false,
        "necesidad_personal": true/false,
        "busqueda_activa": true/false,
        "intencion_comercial": true/false,
        "categoria_skincare": "antiaging" | "manchas_pano" | "imperfecciones" | "hidratacion" | "ninguna",
        "evidencia_literal": "Cita exacta extraída palabra por palabra del texto original que justifica la decisión",
        "confianza": 0-100,
        "razon_rechazo": "Explicación breve si se rechaza"
    }
    """

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"Analiza el siguiente comentario: \"{texto_comentario}\""}
            ],
            response_format={"type": "json_object"}
        )
        
        resultado_json = json.loads(response.choices[0].message.content)
        
        # 1. Validación cruzada de evidencia por código Python (Candado anti-alucinación)
        evidencia = resultado_json.get("evidencia_literal", "")
        if resultado_json.get("es_prospecto_valido", False):
            evidencia_valida = validar_cita_en_texto(texto_comentario, evidencia)
            if not evidencia_valida:
                resultado_json["es_prospecto_valido"] = False
                resultado_json["razon_rechazo"] = "Rechazado por código: La evidencia literal no coincide exactamente con el texto original."
        
        # 2. Cálculo de Scoring Comercial
        resultado_json["scoring_comercial"] = calcular_scoring_prospecto(resultado_json)
        
        return resultado_json

    except Exception as e:
        return {
            "error": str(e),
            "es_prospecto_valido": False,
            "razon_rechazo": f"Error técnico en API: {str(e)}",
            "scoring_comercial": 0
        }