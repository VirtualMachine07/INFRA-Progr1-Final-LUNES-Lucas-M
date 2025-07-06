"""
Módulo para el escaneo de redes, y registro de resultados.
"""

import json
import platform
import subprocess
from datetime import datetime
from typing import List, Dict
from rich.table import Table
from rich.console import Console

consola = Console()


def hacer_ping(ip: str) -> bool:


    """
    Realiza un ping a una dirección IP y devuelve True si responde.

    
    :param ip: Dirección IP a analizar.
    :return: True si la IP responde, False si no.
    """


    sistema = platform.system().lower()
    if sistema == "windows":
        comando = ["ping", "-n", "1", "-w", "500", ip]  # -w 500 = 500ms timeout máximo.
    else:
        comando = ["ping", "-c", "1", "-W", "1", ip]     # -W 1 = 1s timeout máximo.

    try:
        resultado = subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return resultado.returncode == 0
    except Exception as error:
        print(f"[ERROR] No se pudo hacer ping a {ip}: {error}")
        return False


def escanear_red(ip_base: str) -> List[str]:


    """
    Escanea la red y devuelve una lista de los dispositivos conectados (IPs activas).

    ip_base = Prefijo de la red (Ej: 192.168.1)
    return = Lista de IPs activas.

    Se añade un mensaje para ir informando avances.
    """


    resultados = []
    for i in range(1, 255):
        ip = f"{ip_base}.{i}"
        print(f"Probando {ip}...")
        if hacer_ping(ip):
            resultados.append(ip)
    return resultados


def guardar_escaneo(resultados: List[str], archivo: str = "scan_results.json") -> None:


    """
    Guarda los resultados del análisis en un archivo JSON.

    resultados = Lista de IPs activas.
    archivo = Nombre del archivo JSON.
    """


    marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    datos = {marca_tiempo: resultados}

    try:
        with open(archivo, "r") as file:
            escaneos_existentes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        escaneos_existentes = {}

    escaneos_existentes.update(datos)

    with open(archivo, "w") as file:
        json.dump(escaneos_existentes, file, indent=4)


def cargar_escaneos(archivo: str = "scan_results.json") -> Dict[str, List[str]]:


    """
    Carga los análisis desde el archivo JSON.

    archivo = Nombre del archivo JSON.
    return = Diccionario con las fechas como claves y listas de IPs como valores.
    """


    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def mostrar_tabla(escanear_info: List[str], titulo: str = "Dispositivos Detectados") -> None:


    """
    Muestra los resultados en formato de tabla con Rich.

    escanear_info = Lista de IPs activas.
    titulo = Título de la tabla.
    """


    tabla = Table(title=titulo)
    tabla.add_column("N°", justify="right", style="cyan")
    tabla.add_column("Dirección IP", style="green")

    for numero, ip in enumerate(escanear_info, 1):
        tabla.add_row(str(numero), ip)

    consola.print(tabla)