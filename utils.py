import os


def clear_screen():
    """Limpia la pantalla de la consola"""
    os.system("cls" if os.name == "nt" else "clear")
