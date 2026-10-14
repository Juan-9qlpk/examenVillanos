"""Menú de consola de la aplicación."""

import logging
from gestion import Gestion
from models import Jugador, CuerpoTecnico
from datetime import datetime
import os
logger = logging.getLogger(__name__)


class Menu:
    def __init__(self, gestion: Gestion):
        self.gestion = gestion

    def mostrar(self) -> None:
        """Muestra el menú principal y procesa las opciones."""
        while True:
            print("\n=== HÉROES Y VILLANOS DEL VIRGEN ===")
            print("1. Crear héroe")
            print("2. Crear villano")
            print("3. Listar personajes")
            print("4. Buscar por atributo")
            print("5. Emparejar héroe y villano")
            print("6. Eliminar personaje")
            print("0. Salir")

            try:
                opcion = input("Elige una opción: ").strip()
                if opcion == "1":
                    self._crear("heroe")
                elif opcion == "2":
                    self._crear("villano")
                elif opcion == "3":
                    self._listar()
                elif opcion == "4":
                    self._buscar()
                elif opcion == "5":
                    self._emparejar()
                elif opcion == "6":
                    self._eliminar()
                elif opcion == "0":
                    logger.info("Volviendo al menu principal")
                    print("Volviendo al menu principal.")
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")

    def _crear(self, tipo: str) -> None:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        fecha = input("Fecha de nacimiento (AAAA-MM-DD): ").strip()
        personaje = self.gestion.crear_personaje(tipo, nombre, apellidos, fecha)
        print(f"Personaje creado: {personaje}")

    def _listar(self) -> None:
        tipo = input("¿Qué quieres listar? (heroe/villano/todos): ").strip()
        personajes = self.gestion.listar_personajes(tipo)
        if not personajes:
            print("No hay personajes para mostrar.")
            return
        for personaje in personajes:
            print(personaje)

    def _buscar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        print("Atributos: identificador, nombre, apellidos, fecha_nacimiento, edad,")
        print("          puntuacion_total y las cualidades propias de cada tipo.")
        atributo = input("Atributo: ").strip()
        operador = input("Operador (=, !=, >, >=, <, <=, contiene): ").strip()
        valor = input("Valor a buscar: ").strip()
        resultados = self.gestion.buscar_por_atributo(tipo, atributo, operador, valor)
        if not resultados:
            print("No se han encontrado coincidencias.")
        else:
            for personaje in resultados:
                print(personaje)

    def _emparejar(self) -> None:
        heroe, villano, diferencia, valoracion = self.gestion.emparejar_aleatoriamente()
        print(f"Héroe: {heroe}")
        print(f"Villano: {villano}")
        print(f"Diferencia de puntuación: {diferencia}")
        print(valoracion)

    def _eliminar(self) -> None:
        tipo = input("Tipo (heroe/villano): ").strip()
        identificador = int(input("Identificador: "))
        if self.gestion.eliminar_personaje(tipo, identificador):
            print("Personaje eliminado.")
        else:
            print("No existe un personaje con ese identificador.")

    def _crear_miembro(self):
            nombre = input("Nombre: ").strip()
            apellidos = input("Apellidos: ").strip()
            posicion = input("Posicion").strip()
            jugador = self.gestion.crear_jugador(nombre, apellidos, posicion)
            print(f"Personaje creado: {jugador}")

    def _crear_tecnico(self):
            nombre = input("Nombre: ").strip()
            apellidos = input("Apellidos: ").strip()
            rol = input("rol").strip()
            tecnico = self.gestion.crear_jugador(nombre, apellidos, rol)
            print(f"Personaje creado: {tecnico}")

    def menu_futbol(self):
        jugador = {}
        tecnico = {}
        while True:
            print("=================================\n"
                  "       PLANTILLAS DE FÚTBOL\n"
                  "=================================\n"
                  "1. Agregar miembro\n"
                  "2. Listar plantilla\n"
                  "3. Crear plantilla\n"
                  "4. Salir\n"
                  "=================================\n")
            try:
                opcion = int(input("Elige una opción:"))
                if opcion == 1:
                    tipo_miembro = int(input("Elige una opcion\n1º Añadir Jugador\n2º Añadir Cuerpo Tecnico"))
                    match tipo_miembro:
                        case 1:
                            m = Jugador(
                            input("Nombre: "),
                            input("Apellidos: "),
                            input("Posicion"))
                            jugador[m.get_id()] = m
                            logger.info(
                                f"Se ha creado un jugador con id: {m.get_id()}, [nombre] {m.get_nombre()}, [apellido] {m.get_apellido()}"
                                "posicion {}"
                            )
                            escribir(f"INSERT INTO jugador (id, nombre, apellidos, posicion) VALUES "
                                     f"({m.get_id()}, '{m.get_nombre()}', '{m.get_apellido()}', '{m.get_pos()}');")
                        case 2:
                            m = CuerpoTecnico(
                            input("Nombre: "),
                            input("Apellidos: "),
                            input("rol"))
                            tecnico[m.get_id()] = m
                            logger.info(
                                f"Se ha creado un jugador con id: {m.get_id()}, [nombre] {m.get_nombre()}, [apellido] {m.get_apellido()}"
                                "posicion {}"
                            )
                            escribir(f"INSERT INTO jugador (id, nombre, apellidos, posicion) VALUES "
                                     f"({m.get_id()}, '{m.get_nombre()}', '{m.get_apellido()}', '{m.get_pos()}');")
                        case _:
                            print("Introduce un número válido")
                            logger.warning("Opción de menú no válida: %s", opcion)
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    break
                else:
                    print("Opción no válida.")
                    logger.warning("Opción de menú no válida: %s", opcion)
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")
                logger.warning("Entrada no válida: %s", exc)
            except (KeyboardInterrupt, EOFError):
                logger.info("Salida solicitada desde teclado.")
                print("\nAplicación finalizada.")
                break
            except Exception:
                logger.exception("Error no controlado en el menú.")
                print("Se ha producido un error. Consulta el archivo aplicacion.log.")


def escribir(self, mensaje):
    fecha = datetime.now().strftime("%Y%m%d")
    self.ruta = f"sql/{fecha}-miembros.sql"

    if not os.path.exists("sql"):
        os.mkdir("sql")

    with open(self.ruta, "a") as fichero:
        fichero.write(f"{mensaje}\n")
