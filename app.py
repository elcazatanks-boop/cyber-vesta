import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cyber-Vesta: Control Inteligente",
    page_icon="🧥",
    layout="centered",
)

# Título y descripción
st.title("🧥 Cyber-Vesta: Casaca Inteligente")
st.write(
    "Proyecto de EPT: Sistema de termorregulación y seguridad automatizada."
)

# --- Panel de Control ---
st.markdown("---")
st.subheader("Panel de Control del Estudiante")

# Botón de encendido principal
estado_energia = st.toggle(
    "🔌 Encender / Apagar Sistema de la Casaca", value=True
)

if not estado_energia:
    st.warning(
        "⚠️ El sistema está **APAGADO**. Enciéndelo para activar la simulación."
    )
    st.markdown(
        "<h1 style='text-align: center; font-size: 100px;'>❌</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center; color: red;'>Sistema Inactivo</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.metric(label="Estado", value="Inactivo 🔴")
else:
    st.success("🟢 Sistema **ENCENDIDO** y operando en tiempo real.")

    # Controles de temperatura
    temp_cuerpo = st.slider(
        "Simular Temperatura Corporal (°C)", 30.0, 40.0, 36.5
    )

    # --- Lógica de Batería Dinámica y Fondos por Estado ---
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        if temp_cuerpo < 35.5:
            # Fondo e indicador de Frío / Calefacción
            st.markdown(
                """
                <div style='background-color: #1a365d; padding: 20px; border-radius: 10px; text-align: center;'>
                    <h1 style='font-size: 100px; margin: 0;'>❄️ 🔥</h1>
                    <h2 style='color: #63b3ed; margin: 10px 0;'>MODO CALEFACCIÓN ACTIVO</h2>
                    <p style='color: #e2e8f0;'>El sensor detectó frío extremo. Las resistencias térmicas están elevando la temperatura interna.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            bateria_actual = "74% (Consumo Alto 🔥)"
        elif temp_cuerpo > 38.0:
            # Fondo e indicador de Calor / Ventilación
            st.markdown(
                """
                <div style='background-color: #742a2a; padding: 20px; border-radius: 10px; text-align: center;'>
                    <h1 style='font-size: 100px; margin: 0;'>🔥 🌀</h1>
                    <h2 style='color: #fc8181; margin: 10px 0;'>MODO VENTILACIÓN ACTIVO</h2>
                    <p style='color: #e2e8f0;'>El sensor detectó calor excesivo. Los micro-ventiladores expulsan el aire caliente.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            bateria_actual = "78% (Consumo Moderado 🌀)"
        else:
            # Fondo e indicador Estable / Reposo
            st.markdown(
                """
                <div style='background-color: #22543d; padding: 20px; border-radius: 10px; text-align: center;'>
                    <h1 style='font-size: 100px; margin: 0;'>✅ 🌡️</h1>
                    <h2 style='color: #68d391; margin: 10px 0;'>ESTADO ESTABLE (CONFORT)</h2>
                    <p style='color: #e2e8f0;'>El estudiante está en temperatura ideal. Los sistemas entran en reposo (Ahorro).</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            bateria_actual = "85% (Ahorro de Energía 🔋)"

    with col2:
        st.metric(label="Nivel de Batería", value=bateria_actual)
        st.metric(
            label="Modo Actual",
            value=(
                "Calefacción"
                if temp_cuerpo < 35.5
                else ("Ventilación" if temp_cuerpo > 38.0 else "Estable")
            ),
        )

    st.markdown("---")
    st.info(
        "💡 **Nota de Exposición:** La batería desciende según el esfuerzo del"
        " sistema y los paneles cambian de color automáticamente para reflejar"
        " la respuesta térmica en tiempo real."
    )
