import time
import schedule
from agent_runner import ejecutar_ciclo_autonomo

def tarea_programada():
    print(f"\n[⏰ ALARMA HORARIA] Disparando ciclo automático de prospección...")
    ejecutar_ciclo_autonomo()

# Configuración de las ventanas de disparo diario (10:00 AM y 11:00 AM)
schedule.every().day.at("10:00").do(tarea_programada)
schedule.every().day.at("11:00").do(tarea_programada)

print("🚀 [SCHEDULER ACTIVADO] El agente de Andalucía Beauty está en espera.")
print("🕒 Programado para disparar automáticamente todos los días a las: 10:00 y 11:00 AM.")
print("ℹ️ Mantén esta terminal abierta. (Presiona Ctrl + C para detenerlo cuando gustes).")

# Loop infinito ligero que vigila el reloj del sistema
while True:
    schedule.run_pending()
    time.sleep(1)