# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto Safe Haven Dashboard! Este documento proporciona directrices para contribuir al proyecto.

## 📋 Código de Conducta

Este proyecto se adhiere a un código de conducta básico:

- Sé respetuoso con todos los colaboradores
- Acepta críticas constructivas
- Enfócate en lo que es mejor para la comunidad
- Muestra empatía hacia otros miembros de la comunidad

## 🚀 Cómo Contribuir

### Reportar Bugs

Si encuentras un bug, por favor crea un issue en GitHub incluyendo:

1. **Descripción clara del problema**
2. **Pasos para reproducir:**
   - Paso 1
   - Paso 2
   - Paso 3
3. **Comportamiento esperado**
4. **Comportamiento actual**
5. **Screenshots** (si aplica)
6. **Entorno:**
   - OS: (Windows/Mac/Linux)
   - Python version:
   - Streamlit version:

### Sugerir Mejoras

Para sugerir una mejora o nueva funcionalidad:

1. **Verifica** que no exista ya un issue similar
2. **Crea un issue** describiendo:
   - ¿Qué problema resuelve?
   - ¿Cómo funcionaría?
   - ¿Por qué sería útil?

### Pull Requests

1. **Fork el repositorio**

2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/NombreDelFeature
   ```

3. **Haz tus cambios** siguiendo las guías de estilo

4. **Prueba tus cambios:**
   ```bash
   streamlit run safe_haven_dashboard.py
   ```

5. **Commit con mensajes claros:**
   ```bash
   git commit -m "Add: descripción clara del cambio"
   ```
   
   Prefijos recomendados:
   - `Add:` - Nueva funcionalidad
   - `Fix:` - Corrección de bug
   - `Update:` - Actualización de funcionalidad existente
   - `Refactor:` - Refactorización de código
   - `Docs:` - Cambios en documentación
   - `Style:` - Cambios de formato/estilo

6. **Push a tu fork:**
   ```bash
   git push origin feature/NombreDelFeature
   ```

7. **Abre un Pull Request** en GitHub

## 📝 Guías de Estilo

### Python

- Sigue [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Usa 4 espacios para indentación
- Nombres de funciones en `snake_case`
- Nombres de clases en `PascalCase`
- Constantes en `UPPER_CASE`

**Ejemplo:**
```python
def calcular_media_geometrica(valores):
    """
    Calcula la media geométrica de un array de valores.
    
    Args:
        valores (array): Array de números positivos
        
    Returns:
        float: Media geométrica
    """
    return stats.gmean(valores)
```

### Documentación

- Añade docstrings a todas las funciones
- Usa comentarios para explicar código complejo
- Actualiza el README si añades nuevas funcionalidades

### Commits

Mensajes de commit claros y descriptivos:

```bash
# ✅ Bueno
git commit -m "Add: simulación de Dados de Schrödinger con 10,000 trayectorias"

# ❌ Malo
git commit -m "cambios"
```

## 🧪 Testing

Aunque actualmente no hay tests automatizados, asegúrate de:

1. **Probar manualmente** todas las funcionalidades afectadas
2. **Verificar** que no hay errores en la consola
3. **Comprobar** que los gráficos se renderizan correctamente
4. **Testear** en diferentes tamaños de pantalla

## 📊 Añadir Nuevas Secciones

Si quieres añadir una nueva sección al dashboard:

1. **Estructura sugerida:**
   ```python
   # ============================================================================
   # NOMBRE DE LA SECCIÓN
   # ============================================================================
   
   with tabX:
       st.header("📊 Título de la Sección")
       
       # Explicación teórica
       st.markdown("""
       Explicación clara del concepto...
       """)
       
       # Controles interactivos
       col1, col2 = st.columns(2)
       with col1:
           param1 = st.slider("Parámetro 1", ...)
       with col2:
           param2 = st.slider("Parámetro 2", ...)
       
       # Simulación/Cálculo
       @st.cache_data
       def simular_concepto(param1, param2):
           # Tu código aquí
           return resultados
       
       # Visualización
       fig, ax = plt.subplots(figsize=(10, 6))
       # Tu gráfico aquí
       st.pyplot(fig)
       
       # Conclusiones
       st.info("💡 **Conclusión clave:** ...")
   ```

2. **Añade documentación** en el README

3. **Incluye referencias** si corresponde

## 🎨 Diseño Visual

Mantén consistencia con el tema oscuro:

```python
# Colores del tema
BACKGROUND = '#000000'
TEXT_COLOR = 'white'
ACCENT_COLOR = '#FFDD55'
GRID_COLOR = '#444444'

# Configuración de matplotlib
plt.rcParams['figure.facecolor'] = BACKGROUND
plt.rcParams['axes.facecolor'] = BACKGROUND
plt.rcParams['text.color'] = TEXT_COLOR
```

## 📦 Dependencias

Si necesitas añadir una nueva dependencia:

1. **Añádela a `requirements.txt`** con versión específica:
   ```
   nueva-libreria>=X.Y.Z
   ```

2. **Justifica** por qué es necesaria en el PR

3. **Mantén** el número de dependencias al mínimo

## ✅ Checklist Pre-PR

Antes de abrir un Pull Request, verifica:

- [ ] El código sigue las guías de estilo
- [ ] Has probado los cambios localmente
- [ ] Has actualizado la documentación si es necesario
- [ ] Los commits tienen mensajes descriptivos
- [ ] No hay conflictos con la rama main
- [ ] Has añadido comentarios donde sea necesario
- [ ] El código es eficiente (usa `@st.cache_data` cuando corresponda)

## 🏆 Reconocimientos

Los contribuidores serán reconocidos en:
- README.md (sección de contribuidores)
- Release notes del proyecto

## 📞 ¿Preguntas?

Si tienes dudas sobre cómo contribuir:

1. Revisa los issues y PRs existentes
2. Crea un issue con tu pregunta
3. Contacta al mantenedor: [@thejuansuero](https://x.com/thejuansuero)

---

¡Gracias por contribuir! 🙌
