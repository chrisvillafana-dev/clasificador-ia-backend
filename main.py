import os
from fastapi import FastAPI, HTTPException
from google import genai

app = FastAPI(
    title="Asistente de Calificaciones IA",
    description="Backend para el procesamiento de tareas escolares con Visión por Computadora"
)

# Inicializamos el cliente de Gemini. 
# La librería de Google es inteligente: busca automáticamente una variable de entorno 
# llamada GEMINI_API_KEY en tu sistema. Si no la encuentra, lanzará un error.
try:
    client = genai.Client()
except Exception as e:
    print(f"Error de configuración: Asegúrate de haber ejecutado 'export GEMINI_API_KEY=...' en tu terminal. Detalle: {e}")
    client = None

@app.get("/")
def ruta_raiz():
    return {"status": "online", "mensaje": "Servidor del Asistente de Calificaciones listo"}

# Creamos una ruta tipo POST porque en el futuro la app móvil nos ENVIARÁ datos (la imagen y la rúbrica)
@app.post("/calificar-tarea")
def calificar_tarea():
    if not client:
        raise HTTPException(status_code=500, detail="El cliente de IA no está configurado en el servidor.")
    
    # Por ahora, para probar que la comunicación con Google funcione antes de enviarle fotos reales,
    # haremos una petición de texto simple simulando que analizamos una rúbrica.
    prompt_prueba = (
        "Actúa como un profesor experto de primaria. Dame un criterio corto de un solo párrafo "
        "sobre qué evaluarías en un cuaderno de un alumno de 8 años respecto al tema de las tablas de multiplicar."
    )
    
    try:
        # Llamamos al modelo más rápido y eficiente de Gemini
        respuesta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_prueba
        )
        
        # Retornamos la respuesta de la IA procesada por nuestro servidor
        return {
            "conexion_ia": "exitosa",
            "modelo_utilizado": "gemini-2.5-flash",
            "criterio_sugerido": respuesta.text
        }
        
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al conectar con Gemini: {str(error)}")