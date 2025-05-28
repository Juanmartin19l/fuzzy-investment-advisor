import matplotlib.pyplot as plt


class VisualizadorSistemaExperto:
    @staticmethod
    def visualizar_variables(sistema_experto):
        try:
            # GRÁFICA 1: Edad del inversor
            # Muestra las funciones de membresía para las categorías: joven, adulto y mayor
            sistema_experto.edad.view(sim=sistema_experto.simulacion)
            plt.title("Variable: Edad del Inversor (años)")
            plt.xlabel("Edad (años)")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 2: Ingresos mensuales
            # Muestra las funciones de membresía para: bajos, medios y altos ingresos
            sistema_experto.ingresos.view(sim=sistema_experto.simulacion)
            plt.title("Variable: Ingresos Mensuales")
            plt.xlabel("Ingresos (unidades monetarias)")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 3: Conocimiento financiero
            # Muestra las funciones de membresía para: bajo, medio y alto conocimiento
            sistema_experto.conocimiento.view(sim=sistema_experto.simulacion)
            plt.title("Variable: Nivel de Conocimiento Financiero")
            plt.xlabel("Conocimiento (escala 0-10)")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 4: Tolerancia al riesgo
            # Muestra las funciones de membresía para: conservador, moderado y arriesgado
            sistema_experto.tolerancia.view(sim=sistema_experto.simulacion)
            plt.title("Variable: Tolerancia al Riesgo")
            plt.xlabel("Tolerancia (escala 0-10)")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 5: Potencial de inversión (Variable intermedia)
            # Muestra el resultado de combinar edad e ingresos
            sistema_experto.potencial.view(sim=sistema_experto.simulacion)
            plt.title("Variable Intermedia: Potencial de Inversión")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 6: Nivel de riesgo (Variable intermedia)
            # Muestra el resultado de combinar conocimiento y tolerancia
            sistema_experto.riesgo.view(sim=sistema_experto.simulacion)
            plt.title("Variable Intermedia: Nivel de Riesgo")
            plt.ylabel("Grado de pertenencia")

            # GRÁFICA 7: Perfil del inversor (Variable de salida)
            # Muestra el perfil final: conservador, moderado o agresivo
            sistema_experto.perfil_inversor.view(
                sim=sistema_experto.simulacion)
            plt.title("Variable de Salida: Perfil del Inversor")
            plt.ylabel("Grado de pertenencia")

            # Mantener todas las ventanas abiertas
            plt.show()
        except Exception as e:
            print(f"\nError al visualizar las funciones de membresía: {e}")
            print("Tipo de error:", type(e).__name__)
