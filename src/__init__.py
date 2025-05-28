"""
Sistema Experto Basado en Lógica Difusa para Perfiles de Inversión
================================================================

Este paquete contiene la implementación de un sistema experto que utiliza
lógica difusa para determinar perfiles de inversión basados en diferentes
parámetros del inversor.

Módulos:
--------
- sistema_experto: Contiene la lógica principal del sistema experto difuso
- utils: Funciones de utilidad para la interfaz de usuario
- visualizacion: Herramientas para visualización de funciones de membresía
"""

__version__ = "1.0.0"
__author__ = "Sistema Experto IA"

# Importaciones principales para facilitar el uso del paquete
from .sistema_experto import SistemaExpertoDifusoInversorFCL
from .visualizacion import VisualizadorSistemaExperto
from .utils import clear_screen

__all__ = [
    'SistemaExpertoDifusoInversorFCL',
    'VisualizadorSistemaExperto',
    'clear_screen'
]
