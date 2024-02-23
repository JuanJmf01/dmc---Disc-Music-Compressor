# dmc - Disc Music Compressor

## Descripción
El proyecto dmc (Disc Music Compressor) es una herramienta diseñada para comprimir archivos de música del formato CD-A a formatos MP3 y OGG de manera simultánea, permitiendo así reducir el tamaño de la biblioteca de música mientras se mantiene una calidad aceptable. Este proyecto utiliza FFmpeg para realizar la conversión de archivos de música y aprovecha el procesamiento en paralelo para mejorar la eficiencia del proceso.

## Funcionalidades
- Conversión de archivos individuales y carpetas enteras de música del formato CD-A a formatos MP3 y OGG.
- Interfaz de línea de comandos para seleccionar archivos o carpetas de entrada y configurar opciones de conversión.
- Gestión automática de la creación de una carpeta de salida para almacenar los archivos convertidos.
- Soporte para mantener o eliminar los archivos convertidos en los formatos MP3 y OGG según la preferencia del usuario.
- Información detallada sobre el tamaño y la cantidad de archivos convertidos en cada formato.

## Requisitos Previos
- Python 3.x
- FFmpeg instalado y configurado en el sistema. Puedes descargar FFmpeg desde [aquí](https://ffmpeg.org/download.html) e instalarlo siguiendo las instrucciones de la documentación oficial.

## Instalación
1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala FFmpeg siguiendo las instrucciones proporcionadas en la documentación oficial.
4. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.

## Uso
1. Ejecuta el script `main.py`.
2. Selecciona la opción deseada: convertir un archivo individual o una carpeta entera.
3. Selecciona el archivo o carpeta de entrada.
4. Espera a que el proceso de conversión se complete. El tiempo de conversión puede variar según la cantidad y el tamaño de los archivos.
5. Al finalizar, se mostrará información detallada sobre los archivos convertidos y se te preguntará si deseas mantener los archivos en formato MP3 y OGG.

## Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras errores, tienes ideas para mejoras o deseas añadir nuevas funcionalidades, no dudes en abrir un issue o enviar un pull request.

## Licencia
Este proyecto está bajo la licencia [MIT](LICENSE).

