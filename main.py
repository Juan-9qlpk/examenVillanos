"""Punto de entrada de la aplicación."""

import logging
from datetime import datetime
from gestion import Gestion
from menu import Menu
import os


def configurar_logging() -> None:
    # Crear la carpeta logs si no existe
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(
                "logs/villanoYHeroe.log",
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ]
    )

def main() -> None:
    configurar_logging()
    logger = logging.getLogger(__name__)
    logger.info("Inicio de la aplicación.")


    while True:
        try:
            opcion_menu = int(input("Escoge menu\n1º Heroes y Villanos\n2º Plantillas Futbol\n3ºSalir"))
            match opcion_menu:
                case 1:
                    gestion = Gestion()
                    menu = Menu(gestion)
                    menu.mostrar()

                case 2:
                    gestion = Gestion()
                    menu = Menu(gestion)
                    menu.menu_futbol()

                case 3:
                    print("Saliendo")
                    break

                case _:
                    print("Escoge una opcion valida")
        except Exception:
            logger.exception("Error fatal en la aplicación.")
            print("La aplicación ha finalizado por un error. Consulta aplicacion.log.")
        finally:
            logger.info("Reiniciando aplicacion")


if __name__ == "__main__":
    main()
