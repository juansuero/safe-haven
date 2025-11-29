# 🎲 Safe Haven Dashboard - Parte 1

Dashboard interactivo basado en el libro **"Safe Haven"** de **Mark Spitznagel**, creado con Streamlit.

Este proyecto ilustra conceptos clave sobre gestión de riesgo, rentabilidad geométrica vs aritmética, y estrategias de safe haven a través de visualizaciones interactivas y simulaciones de Monte Carlo.

## 📋 Contenido

El dashboard incluye 6 secciones principales:

1. **📊 Paradoja de San Petersburgo**: Simulación del famoso juego de azar y sus implicaciones para la teoría de la utilidad esperada
2. **⚓ Comerciante de San Petersburgo**: Análisis de la paradoja desde la perspectiva de un comerciante
3. **🌌 Dados de Schrödinger**: Comparación entre trayectorias únicas vs distribuciones probabilísticas
4. **⚡ Dados de Nietzsche**: Exploración de retornos geométricos vs aritméticos y el impacto de rebalanceo
5. **🎯 Truco (Kelly Criterion)**: Análisis del criterio de Kelly y gestión óptima de capital
6. **🛡️ Apuestas Secundarias**: Estrategias de safe haven y su impacto en el crecimiento geométrico de la cartera

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/safe-haven-dashboard.git
   cd safe-haven-dashboard
   ```

2. **Crea un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Uso

Para ejecutar el dashboard localmente:

```bash
streamlit run safe_haven_dashboard.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📊 Datos

## 🎨 Características

- **Visualizaciones Interactivas**: Gráficos dinámicos con Matplotlib
- **Simulaciones de Monte Carlo**: Miles de trayectorias simuladas para análisis estadístico
- **Controles Personalizables**: Sliders y selectores para experimentar con diferentes parámetros
- **Tema Oscuro**: Diseño visual atractivo con fondo oscuro
- **Responsive**: Se adapta a diferentes tamaños de pantalla

## 📚 Conceptos Clave

### Rentabilidad Geométrica vs Aritmética

El dashboard demuestra la diferencia fundamental entre:
- **Media Aritmética**: Simple promedio de retornos
- **Media Geométrica**: Tasa de crecimiento compuesta real

### Safe Haven vs Diversificación

Explora cómo los activos safe haven difieren de la diversificación tradicional:
- **Diversificación**: Reduce varianza pero puede reducir el crecimiento geométrico
- **Safe Haven**: Puede aumentar el crecimiento geométrico mediante payoff asimétrico

### Criterio de Kelly

Implementa y visualiza el criterio de Kelly para tamaño óptimo de posiciones en función de:
- Probabilidad de éxito
- Ratio ganancia/pérdida
- Impacto en el crecimiento geométrico

## 🛠️ Estructura del Proyecto

```
safe-haven-dashboard/
│
├── safe_haven_dashboard.py    # Script principal del dashboard
├── requirements.txt            # Dependencias de Python
├── README.md                   # Este archivo
├── LICENSE                     # Licencia MIT
├── .gitignore                  # Archivos a ignorar por Git
```

## 📖 Referencias

- **Libro**: "Safe Haven: Investing for Financial Storms" - Mark Spitznagel
- **Podcast/YouTube**: [Solo Señal](https://youtube.com/@soloseñal) por Juan Suero
- **Twitter/X**: [@thejuansuero](https://x.com/thejuansuero)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes sugerencias:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Juan Suero**

- X/Twitter: [@thejuansuero](https://x.com/thejuansuero)
- YouTube: [Solo Señal](https://youtube.com/@soloseñal)
- Spotify: [Solo Señal Podcast](https://open.spotify.com/show/0xvP4JF7dJm5SjF8vfA9u6)

## ⚠️ Disclaimer

Este dashboard tiene fines educativos y de divulgación. No constituye asesoramiento financiero. Las simulaciones utilizan datos históricos y no garantizan resultados futuros.

---

⭐ Si te resulta útil este proyecto, ¡considera darle una estrella en GitHub!

