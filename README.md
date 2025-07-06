# Verificador de conectividad IP

Este programa realiza un análisis de conectividad en una red local e identifica qué hosts están activos. Los resultados se muestran en una tabla y se almacenan en un archivo JSON para su posterior consulta (Si este no existe, lo crea). Tener en cuenta que el escaner, se efectúa de manera secuencial. Es decir, realiza un ping por IP en todo el prefijo IP especificado desde la IP .1 a la .254. Si bien, se limito el tiempo de ejecución según la respuesta y el time out, un análisis completo puede demorar entre 2-5 minutos.

El objetivo de la herramienta, es llevar un registro de hosts activos para el mapeo de una red. Útíl para entornos donde los rangos sean limitados, y sea necesario realizar una limpieza de pool DHCP de forma periodica, o simplemente conocer que IPs se encuentran libres para su uso.

## Requisitos

- Python 3.7+
- Librerías: rich (Entorno Virtual)     # Se utiliza para instalar la librería externa rich. El beneficio de hacerlo en un entorno es evitar conflictos con otras librerías.
- Compatible con Windows y Linux

## Estructura

Final/
main.py                # Archivo principal que ejecuta la interfaz de usuario.
network_scanner.py     # Módulo para el escaneo de redes y registro de resultados.
requirements.txt       # Dependencias externas
README.md              # Descripción del programa, requisitos, y detalles para su aplicación.

Una vez ejecutado el programa, añadirá a su estructura el archivo scan_results.json.

## Interfaz
1. Iniciar nuevo análisis                   # Ejecuta un análisis de la red según el prefijo suministrado.
2. Ver último análisis                      # Muestra el último análisis con detalles de fecha/hora del registro.
3. Buscar análisis por fecha (YYYY-MM-DD)   # Busca el registro acorde a la fecha.
4. Salir                                    # Finaliza la ejecución del programa.

## Instalación según Sistema Operativo

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
