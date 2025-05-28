import matplotlib.pyplot as plt


class VisualizadorSistemaExperto:
    @staticmethod
    def visualizar_variables(sistema_experto):
        try:
            variables = [
                {
                    "nombre": "Edad del Inversor (años)",
                    "variable": sistema_experto.edad,
                    "xlabel": "Edad (años)"
                },
                {
                    "nombre": "Ingresos Mensuales",
                    "variable": sistema_experto.ingresos,
                    "xlabel": "Ingresos (unidades monetarias)"
                },
                {
                    "nombre": "Nivel de Conocimiento Financiero",
                    "variable": sistema_experto.conocimiento,
                    "xlabel": "Conocimiento (escala 0-10)"
                },
                {
                    "nombre": "Tolerancia al Riesgo",
                    "variable": sistema_experto.tolerancia,
                    "xlabel": "Tolerancia (escala 0-10)"
                },
                {
                    "nombre": "Potencial de Inversión (Variable Intermedia)",
                    "variable": sistema_experto.potencial,
                    "xlabel": None
                },
                {
                    "nombre": "Nivel de Riesgo (Variable Intermedia)",
                    "variable": sistema_experto.riesgo,
                    "xlabel": None
                },
                {
                    "nombre": "Perfil del Inversor (Variable de Salida)",
                    "variable": sistema_experto.perfil_inversor,
                    "xlabel": None
                }
            ]

            for v in variables:
                v["variable"].view(sim=sistema_experto.simulacion)
                ax = plt.gca()
                ax.set_title(f"Variable: {v['nombre']}")
                if v["xlabel"]:
                    ax.set_xlabel(v["xlabel"])
                ax.set_ylabel("Grado de pertenencia")
                ax.legend()
                plt.tight_layout()

            plt.show()

        except Exception as e:
            print(f"\nError al visualizar las funciones de membresía: {e}")
            print("Tipo de error:", type(e).__name__)
