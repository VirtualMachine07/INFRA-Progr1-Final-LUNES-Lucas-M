"""
Módulo principal para la interfaz del usuario.
"""

from network_scanner import escanear_red, guardar_escaneo, cargar_escaneos, mostrar_tabla
from datetime import datetime


def main():
    while True:
        print("\n--- Verificador de Conectividad IP ---")
        print("1. Iniciar nuevo análisis")
        print("2. Ver último análisis")
        print("3. Buscar análisis por fecha (YYYY-MM-DD)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ip_base = input("Ingrese el prefijo de la red (Ej: 192.168.1): ")
            print("Escaneando red, por favor espere...")
            resultados = escanear_red(ip_base)
            guardar_escaneo(resultados)
            mostrar_tabla(resultados, titulo="Resultado del nuevo análisis")

        elif opcion == "2":
            escaneos = cargar_escaneos()
            if escaneos:
                ultima_fecha = sorted(escaneos.keys())[-1]
                mostrar_tabla(escaneos[ultima_fecha], titulo=f"Último análisis ({ultima_fecha})")
            else:
                print("No hay registros disponibles.")

        elif opcion == "3":
            fecha_busqueda = input("Ingrese la fecha (YYYY-MM-DD): ")
            escaneos = cargar_escaneos()
            encontrado = False
            for fecha, escanear_info in escaneos.items():
                if fecha.startswith(fecha_busqueda):
                    mostrar_tabla(escanear_info, titulo=f"Análisis del {fecha}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontraron registros para {fecha_busqueda}.")

        elif opcion == "4":
            print("Saliendo del escaner de redes.")
            break
        else:
            print("La opción no existe. Intente nuevamente.")


if __name__ == "__main__":
    main()