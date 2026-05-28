from fastapi import FastAPI

# Instanciamos la aplicación
app = FastAPI(
    title="Asistente de Calificaciones IA",
    description="Backend para el procesamiento de tareas escolares con Visión por Computadora"
)

@app.get("/")
def ruta_raiz():
    return {"status": "online", "mensaje": "Servidor del Asistente de Calificaciones listo"}

@app.get("/test-ia")
def probar_conexion():
    # Aquí es donde eventualmente llamaremos a la IA
    return {"mensaje": "Próximamente: Conexión con el modelo de Visión"}