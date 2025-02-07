import shutil
import time

# Imágenes capturadas por las cámaras
imagen_original_este = "C:\\Users\\cesar\\OneDrive\\Desktop\\CAM_SERVER\\SITIO WEB\\Recursos\\Live\\ESTE.jpg"
imagen_original_oeste = "C:\\Users\\cesar\\OneDrive\\Desktop\\CAM_SERVER\\SITIO WEB\\Recursos\\Live\\OESTE.jpg"

# Ruta de destino en el servidor web
imagen_destino_este = "C:\\Users\\cesar\\OneDrive\\Desktop\\CAM_SERVER\\SITIO WEB\\Recursos\\Live\\ESTE.jpg"
imagen_destino_oeste = "C:\\Users\\cesar\\OneDrive\\Desktop\\CAM_SERVER\\SITIO WEB\\Recursos\\Live\\OESTE.jpg"

while True:
    try:
        # Copia la nueva imagen sobrescribiendo la anterior
        shutil.copy(imagen_original_este, imagen_destino_este)
        shutil.copy(imagen_original_oeste, imagen_destino_oeste)
        print("Imágenes actualizadas correctamente.")

    except Exception as e:
        print(f"Error al actualizar imágenes: {e}")

    time.sleep(60)  # Espera 1 minuto antes de actualizar nuevamente
