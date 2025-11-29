"""
SAFE HAVEN DE MARK SPITZNAGEL - PARTE 1
Dashboard interactivo con Streamlit
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy import stats

# Configuración de página
st.set_page_config(
    page_title="Safe Haven - Parte 1",
    page_icon="🎲",
    layout="wide"
)

st.title("🎲 'Safe Haven' de Mark Spitznagel - Parte 1")

# EDITA AQUÍ TU INFORMACIÓN
NOMBRE = "Juan Suero"
PERFIL_X = "@thejuansuero"
LINK_YOUTUBE = "https://youtu.be/0xUUzlusyyk"
LINK_SPOTIFY = "https://open.spotify.com/show/0xvP4JF7dJm5SjF8vfA9u6?si=f9ba713100d1484f"
MENSAJE = "Este dashboard está basado en mi episodio sobre la Parte 1 de Safe Haven de Mark Spitznagel, el cual está subido en YouTube, Spotify y otras plataformas de pódcast. ¡Si te gusta este dashboard, seguramente te interese echarle un vistazo!"

# Caja de información del autor
st.info(f"""
👤 **Creado por:** {NOMBRE}  

{MENSAJE}

🔗 **Sígueme en X:** [{PERFIL_X}](https://x.com/{PERFIL_X.replace('@', '')})  |  📺 **YouTube:** [Ver Episodio]({LINK_YOUTUBE})  |  🎧 **Spotify:** [Escuchar Aquí]({LINK_SPOTIFY})
""")

st.markdown("---")


# Crear tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Paradoja San Petersburgo",
    "⚓ Comerciante de San Petersburgo",
    "🌌 Dados Schrödinger",
    "⚡ Dados Nietzsche",
    "🎯 Truco (Kelly)",
    "🛡️ Apuestas Secundarias"
])

# ============================================================================
# TAB 1: PARADOJA SAN PETERSBURGO
# ============================================================================
with tab1:
    st.header("Paradoja de San Petersburgo")

    st.markdown("""
    ### 🎲 ¿Qué es la Paradoja de San Petersburgo?
    
    En 1713, Nicolaus Bernoulli propuso un juego con **valor esperado infinito** pero que nadie pagaría 
    una fortuna por jugar. Su primo Daniel Bernoulli (1738) resolvió esta paradoja introduciendo el 
    concepto de **"emolumentum medium"** o utilidad media geométrica.
    
    **El juego:** Se lanza una moneda repetidamente hasta que salga un número determinado (por ejemplo, el 1). Puede tardar mucho en salir, por lo que el valor esperado es infinito. Pero ¿cuánto pagarías por jugar?
    
    **La solución de Bernoulli:** No midas el valor en dinero absoluto, sino en **utilidad logarítmica**. 
    La media geométrica captura mejor la experiencia real del jugador que debe arriesgar capital finito.
    
    ---
    
    ### 🎯 Cómo Usar Esta Simulación:
    
    1. **Riqueza Inicial**: Tu capital total antes de apostar
    2. **% Apostado**: Qué fracción de tu riqueza arriesgas en el juego. Más tarde, el valor justo te mostrará que tan buena es tu elección.
    3. **Payoffs del Dado**: Lo que te pagan si sale cada cara del dado (1-6). Ej, si sale 1 te pagan $1, si sale 4 te pagan $22 (por default, puedes modificar los valores)
    
    El gráfico muestra la **media geométrica** de tu riqueza final para diferentes fracciones apostadas. 
    El punto donde cruza tu riqueza inicial es el **valor justo máximo** que deberías pagar por jugar.
    
    💡 **Idea clave**: Aunque la media aritmética puede ser muy alta, la media geométrica (lo que realmente 
    experimentarías en el largo plazo) suele ser mucho menor. ¡El valor esperado no es tu esperanza!
    """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        riqueza_inicial = st.number_input(
            "Riqueza Inicial ($)", 
            min_value=1000, 
            max_value=1000000, 
            value=100000, 
            step=1000
        )
        
        porcentaje_apostado = st.slider(
            "% Apostado", 
            min_value=0.0, 
            max_value=1.0, 
            value=0.5, 
            step=0.01
        )
    
    with col2:
        st.markdown("**Payoffs del Dado:**")
        pago_1 = st.number_input("Cara 1 ($)", value=1, min_value=0)
        pago_2 = st.number_input("Cara 2 ($)", value=2, min_value=0)
        pago_3 = st.number_input("Cara 3 ($)", value=6, min_value=0)
    
    with col3:
        st.write("")  # spacing
        pago_4 = st.number_input("Cara 4 ($)", value=22, min_value=0)
        pago_5 = st.number_input("Cara 5 ($)", value=200, min_value=0)
        pago_6 = st.number_input("Cara 6 ($)", value=1000000, min_value=0)
    
    resultados = {1: pago_1, 2: pago_2, 3: pago_3, 4: pago_4, 5: pago_5, 6: pago_6}
    apuesta = riqueza_inicial * porcentaje_apostado
    
    # Cálculos
    riquezas_finales = [riqueza_inicial - apuesta + resultados[i] for i in range(1, 7)]
    media_arit = sum(riquezas_finales) / 6
    
    # Emolumentum Medium (logaritmo)
    em = sum(np.log(max(riqueza_inicial - apuesta + resultados[i], 1e-10)) for i in range(1, 7)) / 6
    bev = np.exp(em)
    
    # Media Geométrica
    media_geom = np.prod([max(w, 1e-10) for w in riquezas_finales]) ** (1/6)
    
    st.markdown("### Resultados")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Media Aritmética", f"${media_arit:,.0f}")
    col_b.metric("Valor Esp. Bernoulli (El dinero con el que puedes esperar acabar)", f"${bev:,.0f}")
    col_c.metric("Media Geométrica", f"${media_geom:,.0f}")
    
    st.latex(r"\text{Emolumentum Medium: } EM = \frac{1}{6}\sum_{i=1}^{6} \ln(W_i)")
    st.latex(r"BEV = e^{EM}")
    
    # Gráfico: Media Geométrica vs Fracción Apostada
    st.markdown("### Media Geométrica vs Fracción Apostada")
    
    def geom_mean_func(frac):
        stake = riqueza_inicial * frac
        wealths = [riqueza_inicial - stake + resultados[i] for i in range(1, 7)]
        if any(w <= 0 for w in wealths):
            return np.nan
        return np.prod(wealths) ** (1/6)
    
    fracs = np.linspace(0.0, 1.0, 501)
    gmeans = np.array([geom_mean_func(f) for f in fracs])
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(fracs * 100, gmeans, color='#2E86AB', lw=2, label='Media Geométrica')
    ax.axhline(riqueza_inicial, color='gray', linestyle='--', alpha=0.7, label=f'Riqueza Inicial = ${riqueza_inicial:,}')
    
    # Encontrar cruce
    diff = gmeans - riqueza_inicial
    valid = ~np.isnan(diff)
    cross_frac = None
    for i in range(len(fracs) - 1):
        if valid[i] and valid[i+1] and diff[i] * diff[i+1] < 0:
            a, b = fracs[i], fracs[i+1]
            for _ in range(50):
                m = (a + b) / 2
                if geom_mean_func(m) > riqueza_inicial:
                    a = m
                else:
                    b = m
            cross_frac = (a + b) / 2
            break
    
    if cross_frac is not None:
        ax.axvline(cross_frac * 100, color='red', linestyle='--', alpha=0.7, label=f'Cruce ≈ {cross_frac*100:.2f}%')
        ax.scatter([cross_frac * 100], [geom_mean_func(cross_frac)], color='red', s=100, zorder=5)
    
    ax.set_xlabel('Porcentaje Apostado (%)')
    ax.set_ylabel('Media Geométrica ($)')
    ax.set_title('Valor Justo de la Apuesta')
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    if cross_frac is not None:
        st.success(f"💡 **Valor Justo**: ${cross_frac * riqueza_inicial:,.2f} ({cross_frac*100:.2f}% de tu riqueza)")

# ============================================================================
# TAB 2: COMERCIANTE DE SAN PETERSBURGO
# ============================================================================
with tab2:
    st.header("El Comerciante de San Petersburgo")
    st.markdown("**¿Vale la pena pagar por un seguro actuarialmente desfavorable?**")

    st.markdown(""" 
    Daniel Bernoulli planteó este escenario real del comercio marítimo del siglo XVIII:
    
    Un comerciante en Ámsterdam envía mercancías a San Petersburgo por mar. Históricamente:
    - **95% de los barcos** llegan a salvo
    - **5% se pierden** por tormentas, piratas o naufragios
    
    Una compañía aseguradora ofrece cubrir la pérdida total, pero cobra una prima que **excede** 
    el valor actuarial esperado. En términos aritméticos, el seguro 
    parece una mala inversión.
    
    **La Paradoja:** ¿Por qué un comerciante racional debería pagar estas primas "excesivas"?
    
    ---
    
    ### 🎯 La Solución: Geometría vs Aritmética
    
    Bernoulli demostró que aunque el seguro reduce la **media aritmética** (es actuarialmente desfavorable), 
    **aumenta la media geométrica** (mejora el crecimiento compuesto del capital).
    
    **Clave:** Las pérdidas tienen impacto **logarítmico** (multiplicativo) mayor que su impacto aritmético (aditivo).
    
    ---
    
    ### 🛠️ Instrucciones de Uso:
    
    1. **Ahorros**: Capital líquido del comerciante (independiente de las mercancías)
    2. **Valor de Mercancías**: Lo que vale el cargamento si llega a destino
    3. **Probabilidad de Pérdida**: Histórica del 5%, pero puedes ajustarla
    4. **Prima del Seguro**: Lo que cobra la aseguradora (prueba valores > pérdida esperada)

    Todo estos valores pueden ser cambiados por vosotros.
    
    Observa cómo el **mapa logarítmico** revela que pagar 100 primas pequeñas duele menos (en términos 
    geométricos) que sufrir 5 pérdidas totales, aunque aritméticamente parezca costoso.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**⚙️ Parámetros del Comerciante**")
        ahorros = st.number_input("Ahorros ($)", min_value=1000, max_value=100000, value=3000, step=100, key='merchant_savings')
        valor_mercancia = st.number_input("Valor de Mercancías ($)", min_value=1000, max_value=100000, value=10000, step=500, key='merchant_goods')
        prob_perdida = st.slider("Probabilidad de Pérdida (%)", 0.0, 20.0, 5.0, 0.5, key='merchant_prob') / 100
        
        riqueza_total_comerciante = ahorros + valor_mercancia
        st.metric("Riqueza Total (si llega)", f"${riqueza_total_comerciante:,}")
    
    with col2:
        st.markdown("**🛡️ Parámetros del Seguro**")
        prima_seguro = st.number_input("Prima del Seguro ($)", min_value=0, max_value=5000, value=800, step=50, key='merchant_premium')
        
        # Cálculos actuariales
        perdida_esperada_actuarial = valor_mercancia * prob_perdida
        coste_actuarial_neto = prima_seguro - perdida_esperada_actuarial
        
        st.metric("Pérdida Esperada Actuarial", f"${perdida_esperada_actuarial:,.0f}")
        st.metric("Coste Neto Aritmético", f"${coste_actuarial_neto:,.0f}", 
                 delta=f"{coste_actuarial_neto:,.0f}", delta_color="inverse")
    
    st.markdown("---")
    
    # Cálculos de las medias geométricas
    # SIN SEGURO: 95% éxito (ahorros + mercancía), 5% pérdida (solo ahorros)
    n_envios = 100
    n_exito = int((1 - prob_perdida) * n_envios)
    n_perdida = n_envios - n_exito
    
    # Riquezas finales sin seguro
    riqueza_exito = ahorros + valor_mercancia
    riqueza_perdida = ahorros
    
    # Media geométrica sin seguro (usando logs para evitar overflow)
    log_geom_sin_seguro = (n_exito * np.log(riqueza_exito) + n_perdida * np.log(riqueza_perdida)) / n_envios
    media_geom_sin_seguro = np.exp(log_geom_sin_seguro)
    
    # CON SEGURO: 100% garantizado (ahorros + mercancía - prima)
    riqueza_con_seguro = ahorros + valor_mercancia - prima_seguro
    media_geom_con_seguro = riqueza_con_seguro
    
    # CAGR (Tasa de Crecimiento Anual Compuesta)
    inversion_necesaria = valor_mercancia * 0.8  # Asumimos que invirtió el 80% del valor de venta
    capital_inicial = ahorros + inversion_necesaria
    
    # Retornos totales
    retorno_exito = riqueza_exito / capital_inicial
    retorno_perdida = riqueza_perdida / capital_inicial
    retorno_con_seguro = riqueza_con_seguro / capital_inicial
    
    # CAGR sin seguro
    cagr_sin_seguro = (retorno_exito ** n_exito * retorno_perdida ** n_perdida) ** (1/n_envios)
    # CAGR con seguro
    cagr_con_seguro = retorno_con_seguro
    
    # Ganancia geométrica del seguro
    ganancia_geometrica = media_geom_con_seguro - media_geom_sin_seguro
    
    st.markdown("### 📊 Comparación: Con vs Sin Seguro")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("**Sin Seguro**")
        st.metric("Media Geométrica", f"${media_geom_sin_seguro:,.0f}")
        st.metric("CAGR", f"{(cagr_sin_seguro - 1)*100:.2f}%")
    
    with col_b:
        st.markdown("**Con Seguro**")
        st.metric("Media Geométrica", f"${media_geom_con_seguro:,.0f}")
        st.metric("CAGR", f"{(cagr_con_seguro - 1)*100:.2f}%")
    
    with col_c:
        st.markdown("**Ganancia**")
        st.metric("Mejora Geométrica", f"${ganancia_geometrica:,.0f}", 
                 delta=f"+{ganancia_geometrica:,.0f}" if ganancia_geometrica > 0 else f"{ganancia_geometrica:,.0f}")
        mejora_cagr = (cagr_con_seguro - cagr_sin_seguro) * 100
        st.metric("Mejora CAGR", f"{mejora_cagr:+.2f}%",
                 delta=f"+{mejora_cagr:.2f}%" if mejora_cagr > 0 else f"{mejora_cagr:.2f}%")
    
    st.markdown("---")
    
    # Gráfico logarítmico: mapeo de puntos A, B, C, D, E
    st.markdown("### 📈 Mapa Logarítmico de Pérdidas")
    
    # Puntos clave
    A_x = ahorros + valor_mercancia  # Riqueza total con éxito
    B_x = A_x - prima_seguro          # Después de pagar prima
    C_x = B_x                          # Proyección en la curva
    D_x = ahorros                      # Pérdida total (solo ahorros)
    E_x = D_x                          # Proyección en la curva
    
    A_y = np.log(A_x)
    B_y = A_y                          # Horizontal desde A
    C_y = np.log(C_x)
    D_y = A_y                          # Horizontal desde A
    E_y = np.log(E_x)
    
    # Pérdidas logarítmicas
    perdida_log_bc = B_y - C_y  # Coste logarítmico del seguro
    perdida_log_de = D_y - E_y  # Coste logarítmico de la pérdida total
    
    # Generar curva
    x_curve = np.linspace(ahorros * 0.8, A_x * 1.1, 500)
    y_curve = np.log(x_curve)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Panel izquierdo: vista general
    ax1.plot(x_curve, y_curve, linewidth=2, color='#2E86AB', label='log(riqueza)')
    ax1.scatter([A_x, C_x, E_x], [A_y, C_y, E_y], s=100, color='#A23B72', zorder=5)
    
    # Líneas horizontales (pérdidas aritméticas)
    ax1.hlines(A_y, xmin=D_x, xmax=A_x, linestyles='dotted', color='gray', alpha=0.7)
    
    # Líneas verticales (pérdidas logarítmicas)
    ax1.vlines(B_x, ymin=C_y, ymax=B_y, linestyles='solid', color='red', linewidth=2, label='Coste log seguro')
    ax1.vlines(D_x, ymin=E_y, ymax=D_y, linestyles='solid', color='darkred', linewidth=2, label='Pérdida log total')
    
    ax1.annotate("A", (A_x, A_y), xytext=(5, 5), textcoords="offset points", fontsize=12, fontweight='bold')
    ax1.annotate("C", (C_x, C_y), xytext=(5, -15), textcoords="offset points", fontsize=12, fontweight='bold')
    ax1.annotate("E", (E_x, E_y), xytext=(5, -15), textcoords="offset points", fontsize=12, fontweight='bold')
    
    ax1.set_xlabel("Riqueza ($)", fontsize=11)
    ax1.set_ylabel("log(Riqueza)", fontsize=11)
    ax1.set_title("Vista General: Pérdidas Logarítmicas vs Aritméticas", fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right')
    ax1.grid(alpha=0.3)
    
    # Panel derecho: zoom en región A-B-C
    ax2.plot(x_curve, y_curve, linewidth=2, color='#2E86AB')
    ax2.scatter([A_x, C_x], [A_y, C_y], s=100, color='#A23B72', zorder=5)
    ax2.hlines(A_y, xmin=B_x, xmax=A_x, linestyles='dotted', color='gray', alpha=0.7)
    ax2.vlines(B_x, ymin=C_y, ymax=B_y, linestyles='solid', color='red', linewidth=2)
    
    ax2.annotate("A", (A_x, A_y), xytext=(5, 5), textcoords="offset points", fontsize=12, fontweight='bold')
    ax2.annotate("B", (B_x, B_y), xytext=(5, 5), textcoords="offset points", fontsize=12, fontweight='bold')
    ax2.annotate("C", (C_x, C_y), xytext=(5, -15), textcoords="offset points", fontsize=12, fontweight='bold')
    
    # Zoom limits
    margin = prima_seguro * 2
    ax2.set_xlim(B_x - margin, A_x + margin)
    ax2.set_ylim(C_y - 0.05, A_y + 0.05)
    
    ax2.set_xlabel("Riqueza ($)", fontsize=11)
    ax2.set_ylabel("log(Riqueza)", fontsize=11)
    ax2.set_title("Zoom: Coste del Seguro (A→B→C)", fontsize=12, fontweight='bold')
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""
    **Interpretación del Gráfico:**
    - **Pérdidas Horizontales** (aritméticas): Distancia de A a B (coste de la prima) vs A a D (pérdida total de mercancías)
    - **Pérdidas Verticales** (logarítmicas): Distancia de B a C (impacto log del seguro) vs D a E (impacto log de la pérdida)
    - La suma de 100 pérdidas B→C es **menor** que la suma de 5 pérdidas D→E, a pesar de que el coste aritmético parece desfavorable
    - Esto muestra por qué el seguro mejora la **media geométrica** aunque reduzca la **media aritmética**
    """)
    
    st.latex(r"\text{Pérdida log (seguro)} = \ln(A) - \ln(C) = \ln\left(\frac{A}{C}\right)")
    st.latex(r"\text{Pérdida log (siniestro)} = \ln(A) - \ln(E) = \ln\left(\frac{A}{E}\right)")
    
    st.markdown("---")
    
    # Comparación de pérdidas acumuladas
    st.markdown("### 🔢 Comparación de Pérdidas Acumuladas (100 envíos)")
    
    suma_perdidas_h_ab = prima_seguro * n_envios
    suma_perdidas_h_ad = valor_mercancia * n_perdida
    
    suma_perdidas_v_bc = perdida_log_bc * n_envios
    suma_perdidas_v_de = perdida_log_de * n_perdida
    
    col_x, col_y = st.columns(2)
    
    with col_x:
        st.markdown("**Pérdidas Horizontales (Aritméticas)**")
        st.metric("100× Prima del Seguro", f"${suma_perdidas_h_ab:,.0f}")
        st.metric(f"{n_perdida}× Pérdida de Mercancías", f"${suma_perdidas_h_ad:,.0f}")
        diferencia_h = suma_perdidas_h_ad - suma_perdidas_h_ab
        st.metric("Diferencia", f"${abs(diferencia_h):,.0f}", 
                 delta=f"Asegurador gana ${abs(coste_actuarial_neto * n_envios):,.0f}")
    
    with col_y:
        st.markdown("**Pérdidas Verticales (Logarítmicas)**")
        st.metric("100× Coste Log Seguro", f"{suma_perdidas_v_bc:.4f}")
        st.metric(f"{n_perdida}× Pérdida Log Total", f"{suma_perdidas_v_de:.4f}")
        diferencia_v = suma_perdidas_v_de - suma_perdidas_v_bc
        st.metric("Diferencia", f"{diferencia_v:.4f}", 
                 delta=f"Comerciante mejora {diferencia_v:.4f}" if diferencia_v > 0 else f"Comerciante empeora {abs(diferencia_v):.4f}",
                 delta_color="normal" if diferencia_v > 0 else "inverse")
    
    if ganancia_geometrica > 0:
        st.success(f"""
        El seguro MEJORA la media geométrica en {ganancia_geometrica:,.0f} dólares a pesar de ser 
        actuarialmente desfavorable por {coste_actuarial_neto:,.0f} dólares. 
        
        ¡No es un juego de suma cero! El comerciante gana en términos geométricos (+ ${ganancia_geometrica:,.0f}) 
        y el asegurador gana en términos aritméticos (+ ${coste_actuarial_neto * n_envios:,.0f} en {n_envios} envíos).
        """)
    else:
        st.warning(f"⚠️ Con estos parámetros, el seguro NO es beneficioso para el comerciante. La prima es demasiado alta.")
    st.markdown("""
    ---
    ### 🧠 Lecciones Clave:
    
    1. **El valor esperado aritmético NO es tu esperanza** cuando los resultados se componen multiplicativamente
    2. **La media geométrica** captura mejor la experiencia real de un agente con capital finito
    3. **Asimetría de pérdidas**: Perder 50% requiere ganar 100% para recuperarse → Impacto logarítmico
    4. **El seguro como anti-fragilidad**: Convierte riesgo multiplicativo en coste aditivo predecible
    5. **Marcos complementarios**: Aritmética para el asegurador (diversificación), geometría para el comerciante (concentración)

    """)

# ============================================================================
# TAB 3: DADOS SCHRÖDINGER
# ============================================================================
with tab3:
    st.header("Dados de Schrödinger (Multiverso Ergódico)")
    st.markdown("**Experimentas TODOS los resultados simultáneamente** — N = ∞")

    st.markdown("""
    ### 🔬 Ergodicidad y el Multiverso Cuántico
    
    En mecánica cuántica, Schrödinger propuso que los sistemas existen en **superposición** — múltiples 
    estados simultáneamente hasta la observación. Aplicado a las finanzas:
    
    **Mundo Ergódico (Schrödinger):**
    - Experimentas **todos** los resultados posibles en cada tirada
    - Tu N efectivo es **infinito** → Siempre obtienes el valor esperado exacto
    - La media del conjunto (ensemble average) = media temporal (time average)
    - **Ley de los Grandes Números** funciona perfectamente
    
    **Por qué NO vivimos aquí:**
    - En realidad, solo experimentas UN resultado por tirada (N=1)
    - No puedes diversificar a través de universos paralelos
    - El valor esperado es una ilusión que nunca experimentarás
    
    ---
    
    ### 🎯 Cómo Usar Esta Simulación:
    
    Esta sección muestra el **mundo ideal** donde el valor esperado aritmético sí predice tu resultado. 
    Es el mundo que asumen los modelos tradicionales de finanzas (CAPM, teoría de portafolio moderna).
    
    1. **Probabilidades**: Ajusta la probabilidad de cada resultado
    2. **Observa**: La trayectoria es completamente determinista
    3. **Compara**: Contrasta con la pestaña "Dados de Nietzsche" para ver la realidad
    
    """)

    st.markdown("---")'''
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        n_tiradas_s = st.number_input("Número de Tiradas", min_value=10, max_value=1000, value=300, step=10, key='sch_tiradas')
        prob_perder_s = st.slider("P(Perder 50%)", 0.0, 1.0, 1/6, 0.01, key='sch_perder')
        prob_ganar_50_s = st.slider("P(Ganar 50%)", 0.0, 1.0, 1/6, 0.01, key='sch_ganar50')
        prob_ganar_5_s = 1.0 - prob_perder_s - prob_ganar_50_s
        
        st.metric("P(Ganar 5%)", f"{prob_ganar_5_s:.2%}")
    
    # Cálculos
    valor_esperado_s = (prob_ganar_50_s * 50) + (prob_perder_s * -50) + (prob_ganar_5_s * 5)
    riqueza_final_s = (1 + valor_esperado_s/100)**n_tiradas_s
    
    with col2:
        st.latex(r"E[R] = p_1 \cdot (+50\%) + p_2 \cdot (-50\%) + p_3 \cdot (+5\%)")
        st.metric("Valor Esperado Aritmético", f"{valor_esperado_s:.2f}%")
        st.metric("Riqueza Final (300 tiradas)", f"{riqueza_final_s:.2f}×")
    
    # Gráfico
    n = np.arange(0, n_tiradas_s + 1)
    riquezas_s = (1 + valor_esperado_s/100) ** n
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(n, riquezas_s, color='#A23B72', lw=2.5)
    ax.scatter(n[::25], riquezas_s[::25], color='#F18F01', s=60)
    ax.set_xlabel('Tirada')
    ax.set_ylabel('Riqueza (× inicial)')
    ax.set_title('Evolución Determinista (Multiverso)')
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# ============================================================================
# TAB 4: DADOS NIETZSCHE
# ============================================================================
with tab4:
    st.header("Dados de Nietzsche (Una Sola Realidad)")
    st.markdown("**Experimentas UN SOLO resultado por tirada** — N = 1")

    st.markdown("""
    ### 🎭 El Eterno Retorno y la No-Ergodicidad
    
    Friedrich Nietzsche propuso el experimento mental del "eterno retorno": imagina que vivirás tu vida exactamente igual, infinitas veces. 
    No puedes promediar sobre vidas alternativas — estás atrapado en UNA trayectoria.
    
    **Mundo No-Ergódico (Nietzsche):**
    - Solo experimentas **un** resultado por tirada
    - Tu N = 1 → Gran variabilidad en resultados posibles
    - Ensemble average ≠ Time average
    - **Crecimiento multiplicativo** crea asimetría brutal
    
    **La Gran Ilusión:**
    - Valor esperado aritmético: +3.3% (suena bien)
    - Retorno geométrico mediano: Negativo (ruina eventual)
    - **La mayoría de los caminos terminan mal**
    
    ---
    
    ### 📊 Por Qué Ocurre Esto:
    
    En un proceso multiplicativo:
    - Perder 50% requiere ganar 100% para recuperarte
    - Las pérdidas duelen más (logarítmicamente) que las ganancias equivalentes
    - Unos pocos resultados extremos elevan el promedio aritmético
    - Pero TÚ probablemente experimentarás la mediana (mucho menor)
    
    ---
    
    ### 🎯 Cómo Usar Esta Simulación:
    
    1. **Ejecuta miles de simulaciones** para ver la distribución real
    2. **Observa la mediana** (línea negra) — esto es lo que típicamente experimentarías
    3. **Compara P5 vs P95** — la dispersión de resultados posibles
    4. **Mira el histograma** — la mayoría termina en pérdida, unos pocos con ganancias extremas
    
    💡 **Lección**: En finanzas reales (reinversión de ganancias), el valor esperado aritmético 
    es una **métrica engañosa**. La mediana (experiencia típica) puede ser completamente diferente.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        n_sim_n = st.number_input("Simulaciones (Recomendadas al menos 1000)", min_value=100, max_value=20000, value=1000, step=100, key='niet_sim')
        n_tiradas_n = st.number_input("Tiradas", min_value=10, max_value=1000, value=300, step=10, key='niet_tiradas')
        
        ret_perder = st.slider("Retorno (Sacar un 1)", -1.0, 0.0, -0.5, 0.05, key='niet_perder')
        ret_medio = st.slider("Retorno (Sacar un 2, 3, 4, 5)", -0.5, 1.0, 0.05, 0.01, key='niet_medio')
        ret_ganar = st.slider("Retorno (Sacar un 6)", -0.5, 2.0, 0.5, 0.05, key='niet_ganar')
    
    retornos_n = np.array([ret_perder, ret_medio, ret_ganar])
    probs_n = np.array([1/6, 4/6, 1/6])
    
    # Simulación
    rng_n = np.random.default_rng(42)
    factores_n = np.array([1.05, 1.05, 1.05, 1.05, 1.5, 0.5])
    caras_n = rng_n.integers(0, 6, size=(n_sim_n, n_tiradas_n))
    retornos_sim_n = factores_n[caras_n]
    riqueza_n = np.concatenate([np.ones((n_sim_n, 1)), np.cumprod(retornos_sim_n, axis=1)], axis=1)
    tiempos_n = np.arange(n_tiradas_n + 1)
    
    p5_n = np.percentile(riqueza_n, 5, axis=0)
    p50_n = np.percentile(riqueza_n, 50, axis=0)
    p95_n = np.percentile(riqueza_n, 95, axis=0)
    
    finales_n = riqueza_n[:, -1]
    
    with col2:
        st.metric("Mediana Final", f"{p50_n[-1]:.4f}×")
        st.metric("P5 Final", f"{p5_n[-1]:.4f}×")
        st.metric("P95 Final", f"{p95_n[-1]:.4f}×")
        
        # Retorno geométrico
        r_geom_n = finales_n ** (1/n_tiradas_n) - 1.0
        st.metric("Retorno Geom. Mediana", f"{np.median(r_geom_n)*100:.2f}%")
    
    # Gráfico de recorridos
    st.markdown("### Recorridos Simulados")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tiempos_n, riqueza_n.T, color='steelblue', alpha=0.01, linewidth=0.7)
    ax.plot(tiempos_n, p50_n, color='black', lw=2.5, label='Mediana (P50)')
    ax.plot(tiempos_n, p5_n, color='red', lw=2, ls='--', label='Percentil 5')
    ax.fill_between(tiempos_n, p5_n, p95_n, color='gray', alpha=0.15)
    ax.set_yscale('log')
    ax.set_xlabel('Tirada')
    ax.set_ylabel('Riqueza (× inicial) — escala log')
    ax.set_title(f'{n_sim_n} Simulaciones de {n_tiradas_n} Tiradas')
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    # Histograma
    st.markdown("### Distribución de Retornos Geométricos")
    r_geom_pct_n = r_geom_n * 100
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.hist(r_geom_pct_n, bins=60, color='teal', alpha=0.75, edgecolor='black')
    
    rp5, rmed, rp95 = np.percentile(r_geom_pct_n, [5, 50, 95])
    ax2.axvline(rp5, color='red', linestyle='--', lw=2, label=f'P5 = {rp5:.2f}%')
    ax2.axvline(rmed, color='black', linestyle='--', lw=2, label=f'Mediana = {rmed:.2f}%')
    ax2.axvline(rp95, color='green', linestyle='--', lw=2, label=f'P95 = {rp95:.2f}%')
    
    ax2.set_xlabel('Retorno Geométrico por Tirada (%)')
    ax2.set_ylabel('Frecuencia')
    ax2.set_title('Distribución del Retorno Geométrico')
    ax2.legend()
    ax2.grid(alpha=0.3)
    st.pyplot(fig2)

# ============================================================================
# TAB 5: TRUCO (KELLY)
# ============================================================================
with tab5:
    st.header("El Truco: Kelly y Reserva de Efectivo")


    st.markdown("""
    
    John Larry Kelly Jr. (Bell Labs) descubrió la fórmula para maximizar la tasa de crecimiento logarítmico 
    del capital en apuestas repetidas. Es la **única** estrategia que maximiza el crecimiento geométrico.
    
    **Fórmula Kelly (caso general):**
    ```
    f* = arg max Σ p_i · ln(1 + f · r_i)
    ```
    
    Donde:
    - **f**: Fracción del capital a apostar
    - **p_i**: Probabilidad del resultado i
    - **r_i**: Retorno del resultado i
    
    ---
    
    ### 🛡️ El Truco: Kelly Fraccional
    
    Aunque Kelly maximiza la **mediana**, apostar menos puede mejorar dramáticamente el **percentil 5** 
    (tus peores escenarios) con solo una pequeña reducción en el crecimiento mediano.
    
    **Por qué funciona:**
    - Mantener efectivo en reserva **amortigua** las malas rachas
    - Transforma dinámicas multiplicativas en más "aditivas"
    - Reduce el **riesgo de ruina** sustancialmente
    - Sacrificio de mediana: Mínimo
    - Mejora de P5: Masiva 
    
    ---
    
    ### 📈 Dos Estrategias Óptimas:
    
    1. **Kelly Óptimo** (línea sólida verde): Maximiza la mediana → Mejor crecimiento promedio
    2. **Kelly Fraccional** (línea punteada naranja): Maximiza el P5 → Mejor protección contra ruina
    
    **Trade-off**: ¿Prefieres ganar más "en promedio" o dormir mejor (menos riesgo de pérdidas catastróficas)?
    
    ---
    
    ### 🎯 Cómo Usar Esta Simulación:
    
    1. **Configura los retornos** del dado (peor caso, caso medio, mejor caso)
    2. **Observa las dos fracciones óptimas** calculadas automáticamente
    3. **Analiza el gráfico**: Mediana vs P5 para diferentes fracciones apostadas
    4. **Decide tu estrategia**: ¿Full Kelly o Kelly fraccional?
    
    💡 **Aplicación práctica**: Warren Buffett usa ~Kelly/2 (mitad de Kelly). Ed Thorp recomendaba Kelly/4 o Kelly/3. 
    La teoría dice "Kelly óptimo", pero la práctica favorece Kelly fraccional para evitar ruina psicológica.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Configuración del Dado:**")
        ret_1_k = st.slider("Retorno Cara 1", -1.0, 0.0, -0.5, 0.05, key='kelly_r1')
        ret_2_k = st.slider("Retorno Cara 2-5", -0.5, 1.0, 0.05, 0.01, key='kelly_r2')
        ret_3_k = st.slider("Retorno Cara 6", -0.5, 2.0, 0.5, 0.05, key='kelly_r3')
        
        n_tiradas_k = st.number_input("Tiradas", min_value=10, max_value=1000, value=300, step=10, key='kelly_tiradas')
    
    retornos_k = np.array([ret_1_k, ret_2_k, ret_3_k])
    probs_k = np.array([1/6, 4/6, 1/6])
    
    # Calcular Kelly
    f_values_k = np.linspace(0.0, 1.5, 1000)
    log_factors_k = np.log1p(np.outer(f_values_k, retornos_k))
    g_f_k = (probs_k * log_factors_k).sum(axis=1)
    idx_kelly_k = np.nanargmax(g_f_k)
    f_kelly_k = f_values_k[idx_kelly_k]
    
    # Retornos geométricos
    retorno_geom_k = np.exp(g_f_k) - 1.0
    
    # Percentil 5
    z_05 = -1.6448536269514722
    second_moment_k = (probs_k * (log_factors_k ** 2)).sum(axis=1)
    var_log_k = np.maximum(second_moment_k - g_f_k**2, 0.0)
    std_log_k = np.sqrt(var_log_k)
    g_p5_k = g_f_k + std_log_k * z_05 / np.sqrt(n_tiradas_k)
    retorno_geom_p5_k = np.exp(g_p5_k) - 1.0
    
    idx_p5_k = np.nanargmax(g_p5_k)
    f_p5_k = f_values_k[idx_p5_k]
    
    with col2:
        st.latex(r"g(f) = \sum p_i \cdot \ln(1 + f \cdot r_i)")
        st.latex(r"f^* = \arg\max g(f)")
        
        col_ka, col_kb = st.columns(2)
        col_ka.metric("Kelly Óptimo", f"{f_kelly_k*100:.1f}%")
        col_kb.metric("Kelly Fraccional (máx P5)", f"{f_p5_k*100:.1f}%")
    
    # Gráfico
    st.markdown("### Retorno Geométrico vs % Apostado")
    
    riqueza_mediana_k = np.exp(n_tiradas_k * g_f_k)
    riqueza_p5_k = np.exp(n_tiradas_k * g_p5_k)
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.semilogy(f_values_k * 100, riqueza_mediana_k, color='purple', lw=2, alpha=0.8, label='Riqueza Mediana')
    ax1.semilogy(f_values_k * 100, riqueza_p5_k, color='purple', lw=2, ls='--', alpha=0.6, label='Riqueza P5')
    ax1.set_xlabel('% Apostado')
    ax1.set_ylabel('Riqueza Final (escala log)')
    ax1.set_xlim(0, 100)
    
    ax2 = ax1.twinx()
    ax2.plot(f_values_k * 100, retorno_geom_k * 100, color='darkgreen', lw=2.5, label='Mediana')
    ax2.plot(f_values_k * 100, retorno_geom_p5_k * 100, color='orange', lw=2, ls='--', label='Percentil 5%')
    ax2.set_ylabel('Retorno Geométrico por Tirada (%)')
    ax2.axhline(0, color='gray', ls=':', lw=1, alpha=0.5)
    
    ax2.axvline(f_kelly_k * 100, color='red', ls=':', lw=1.5, alpha=0.7)
    ax2.axvline(f_p5_k * 100, color='orange', ls=':', lw=1.5, alpha=0.8)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.grid(alpha=0.3)
    ax1.set_title('Criterio de Kelly y Kelly Fraccional')
    
    st.pyplot(fig)
    
    st.info(f"""
    💡 **Kelly Óptimo**: {f_kelly_k*100:.1f}% al dado + {(1-f_kelly_k)*100:.1f}% en efectivo
    
    🛡️ **Kelly Fraccional**: {f_p5_k*100:.1f}% al dado + {(1-f_p5_k)*100:.1f}% en efectivo (maximiza P5)
    """)

# ============================================================================
# TAB 6: APUESTAS SECUNDARIAS (SEGURO)
# ============================================================================
with tab6:
    st.header("Apuestas Secundarias: Seguro como Safe Haven")

    st.markdown("""
    ### 💎 La Paradoja del Safe Haven
    
    Un perfil de pagos de seguro (** insurance safe haven**) de Spitznagel tiene estas características aparentemente contradictorias:
    
    ✅ **Retorno aritmético esperado NEGATIVO** → Pierdes dinero "en promedio"  
    ✅ **Retorno geométrico de cartera POSITIVO** → Crecimiento compuesto mejorado  
    ✅ **Correlación negativa en crisis** → Paga cuando más lo necesitas  
    ✅ **Mejora dramática del P5** → Protección contra ruina  
    
    **¿Cómo es posible?** Porque en un mundo multiplicativo, la aritmética miente.
    
    ---
    
    ### 🔍 Diferencia con Diversificación Tradicional:
    
    **Diversificación (ej. bonos):**
    - Reduce volatilidad → ✓
    - Reduce retorno aritmético → ✗ (típicamente también reduce geometría)
    - Payoff simétrico → No ayuda específicamente en crisis
    
    **Safe Haven (ej. puts, oro, TIPs):**
    - Aumenta volatilidad aritmética → ✗ (parece costoso)
    - **Aumenta** retorno geométrico → ✓✓✓
    - Payoff asimétrico → Paga explosivamente en crisis, pierde 1× en tiempos normales
    
    ---
    
    ### 📐 La Geometría del Seguro:
    
    **Ejemplo numérico:**
    - Dado solo: P(perder 50%) = 1/6, P(ganar 5%) = 4/6, P(ganar 50%) = 1/6
    - Valor esperado aritmético: +3.3% ← Suena bien
    - Retorno geométrico: Negativo ← Ruina eventual
    
    **Con seguro (91% dado + 9% seguro que paga 6× cuando cae el dado):**
    - Retorno aritmético del seguro: **-50%** ← Parece terrible
    - Retorno geométrico combinado: **+0.5%** ← ¡Ahora positivo!
    - Mejora de P5: **+300%** ← Protección masiva
    
    **La magia:** El seguro "tapa" la pérdida del -50% (el evento ruinoso) sacrificando solo un poco 
    de rendimiento en los casos +5%. La asimetría logarítmica hace que valga la pena.
    
    ---
    
    ### 🎯 Cómo Usar Esta Simulación:
    
    1. **Configura el dado** (tu activo principal arriesgado)
    2. **Configura el seguro**:
       - **Pago si Cara 1**: Cuántas veces la prima paga el seguro en crisis (ej. 6×)
       - **Pérdida si Otra Cara**: Típicamente -1× (pierdes toda la prima)
    3. **Ajusta el peso**: ¿Qué % de tu cartera dedicas al seguro? (Óptimo típico: 5-15%)
    4. **Observa los resultados**:
       - Retorno aritmético del seguro (negativo)
       - Retorno geométrico combinado (ojalá positivo)
       - Mejora del P5 (protección)
    
    💡 **Insight clave**: Un activo puede tener **valor esperado negativo** y aún así ser una inversión 
    racional si mejora tu geometría. No todo es suma cero cuando operas en marcos matemáticos diferentes.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Configuración del Dado:**")
        ret_1_seg = st.slider("Retorno Cara 1", -1.0, 0.0, -0.5, 0.05, key='seg_r1')
        ret_2_seg = st.slider("Retorno Cara 2-5", -0.5, 1.0, 0.05, 0.01, key='seg_r2')
        ret_3_seg = st.slider("Retorno Cara 6", -0.5, 2.0, 0.5, 0.05, key='seg_r3')
        
        st.markdown("**Perfil del Seguro:**")
        pago_seguro = st.slider("Pago si Cara 1 (× prima)", 1.0, 10.0, 6.0, 0.5, key='seg_pago')
        perdida_seguro = st.slider("Pérdida si Otra Cara (× prima)", -1.0, 0.0, -1.0, 0.1, key='seg_perdida')
        
        peso_dado = st.slider("% en Dado", 0.0, 1.0, 0.91, 0.01, key='seg_peso')
        peso_seguro = 1.0 - peso_dado
        
        n_sim_seg = st.number_input("Simulaciones", min_value=100, max_value=20000, value=10000, step=100, key='seg_sim')
        n_tiradas_seg = st.number_input("Tiradas", min_value=10, max_value=1000, value=300, step=10, key='seg_tiradas')
    
    retornos_seg = np.array([ret_1_seg, ret_2_seg, ret_3_seg])
    probs_seg = np.array([1/6, 4/6, 1/6])
    mults_dado_seg = 1.0 + retornos_seg
    
    # Multiplicadores del seguro: paga pago_seguro cuando sale 1, pierde todo en otros casos
    mults_seguro = np.array([pago_seguro, 1.0 + perdida_seguro, 1.0 + perdida_seguro])
    
    # Retorno aritmético del seguro standalone
    retornos_seguro = mults_seguro - 1.0
    ret_arit_seguro = float(np.sum(probs_seg * retornos_seguro))
    
    # Multiplicadores combinados
    mults_comb_seg = peso_dado * mults_dado_seg + peso_seguro * mults_seguro
    
    # Retornos geométricos
    if np.all(mults_comb_seg > 0):
        log_mults_comb = np.log(mults_comb_seg)
        g_comb = float(np.sum(probs_seg * log_mults_comb))
        ret_geom_comb = np.exp(g_comb) - 1.0
    else:
        ret_geom_comb = -1.0
    
    with col2:
        st.latex(r"M_{combinado} = w_{dado} \cdot M_{dado} + w_{seguro} \cdot M_{seguro}")
        
        col_sa, col_sb, col_sc = st.columns(3)
        col_sa.metric("Retorno Arit. Seguro", f"{ret_arit_seguro*100:.2f}%")
        col_sb.metric("Retorno Geom. Combinado", f"{ret_geom_comb*100:.2f}%")
        col_sc.metric("Riqueza Final (Mediana)", f"{np.exp(n_tiradas_seg * g_comb):.2f}×")
    
    # Simulación
    rng_seg = np.random.default_rng(12345)
    indices_seg = rng_seg.choice(len(retornos_seg), size=(n_sim_seg, n_tiradas_seg), p=probs_seg)
    
    m_dado_mat = mults_dado_seg[indices_seg]
    m_seguro_mat = mults_seguro[indices_seg]
    
    factores_seg = peso_dado * m_dado_mat + peso_seguro * m_seguro_mat
    factores_seg = np.where(factores_seg > 0, factores_seg, 1e-12)
    
    riqueza_seg = np.concatenate([np.ones((n_sim_seg, 1)), np.cumprod(factores_seg, axis=1)], axis=1)
    tiempos_seg = np.arange(n_tiradas_seg + 1)
    
    p5_seg = np.percentile(riqueza_seg, 5, axis=0)
    p50_seg = np.percentile(riqueza_seg, 50, axis=0)
    p95_seg = np.percentile(riqueza_seg, 95, axis=0)
    
    # Gráfico de recorridos
    st.markdown("### Recorridos Simulados con Seguro")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tiempos_seg, riqueza_seg.T, color='steelblue', alpha=0.01, linewidth=0.7)
    ax.plot(tiempos_seg, p50_seg, color='black', lw=2.5, label='Mediana (P50)')
    ax.plot(tiempos_seg, p5_seg, color='red', lw=2, ls='--', label='Percentil 5')
    ax.fill_between(tiempos_seg, p5_seg, p95_seg, color='gray', alpha=0.15)
    ax.set_yscale('log')
    ax.set_xlabel('Tirada')
    ax.set_ylabel('Riqueza (× inicial) — escala log')
    ax.set_title(f'{peso_dado*100:.0f}% Dado + {peso_seguro*100:.0f}% Seguro')
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    # Comparación P5
    st.markdown("### Comparación de Estrategias (P5)")
    
    # Calcular Kelly sin seguro
    f_values_comp = np.linspace(0.0, 1.5, 1000)
    log_factors_comp = np.log1p(np.outer(f_values_comp, retornos_seg))
    g_f_comp = (probs_seg * log_factors_comp).sum(axis=1)
    idx_kelly_comp = np.nanargmax(g_f_comp)
    f_kelly_comp = f_values_comp[idx_kelly_comp]
    
    # Simular 3 estrategias
    estrategias = {
        'Apostar 100%': 1.0,
        f'Kelly ({f_kelly_comp*100:.0f}%)': f_kelly_comp,
        f'Seguro ({peso_dado*100:.0f}/{peso_seguro*100:.0f})': None  # usamos la combinación ya simulada
    }
    
    p5_valores = {}
    
    for nombre, f in estrategias.items():
        if f is None:
            # Ya tenemos la simulación del seguro
            p5_valores[nombre] = p5_seg[-1]
        else:
            # Simular estrategia sin seguro
            factores_comp = 1.0 + f * retornos_seg[indices_seg]
            factores_comp = np.where(factores_comp > 0, factores_comp, 1e-12)
            riqueza_comp = np.cumprod(factores_comp, axis=1)[:, -1]
            p5_valores[nombre] = np.percentile(riqueza_comp, 5)
    
    nombres_est = list(p5_valores.keys())
    valores_p5 = [p5_valores[n] * 100 for n in nombres_est]
    colores_est = ['blue', 'orange', 'green']
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    bars = ax2.bar(nombres_est, valores_p5, color=colores_est, edgecolor='black', linewidth=1.5, alpha=0.85)
    
    for bar, val in zip(bars, valores_p5):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 2, f"P5={val:.1f}%", 
                 ha='center', va='bottom', fontsize=10, weight='bold')
    
    ax2.set_ylabel('Riqueza P5 (% del capital inicial)')
    ax2.set_title('Comparación de Percentil 5 entre Estrategias')
    ax2.grid(alpha=0.3, axis='y')
    st.pyplot(fig2)
    
    st.success(f"""
    🎯 **Retorno Aritmético del Seguro**: {ret_arit_seguro*100:.2f}% (standalone)
    
    📈 **Retorno Geométrico Combinado**: {ret_geom_comb*100:.2f}%
    
    🛡️ **Protección P5**: El seguro mejora el peor escenario (P5) significativamente, 
    incluso con retorno aritmético negativo.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Dashboard interactivo basado en los conceptos de Safe Haven de Mark Spitznagel</small>
</div>
""", unsafe_allow_html=True)









