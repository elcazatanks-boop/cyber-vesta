import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cyber-Vesta: Control Inteligente",
    page_icon="🧥",
    layout="centered",
)

# Control de temperatura por defecto para evaluar el fondo
# (Evaluamos el slider antes para aplicar el color de fondo general)
temp_cuerpo = 36.5

# Título y descripción
st.title("🧥 Cyber-Vesta: Casaca Inteligente")
st.write(
    "Proyecto de EPT: Sistema de termorregulación y seguridad automatizada."
)

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

    # Definir colores de fondo según la temperatura
    if temp_cuerpo < 35.5:
        bg_color = "#1a365d"  # Azul frío
        modo_texto = "❄️ MODO CALEFACCIÓN ACTIVO"
        bateria_actual = "74% (Consumo Alto 🔥)"
        desc_estado = (
            "El sensor detectó frío extremo. Las resistencias térmicas están"
            " elevando la temperatura interna."
        )
    elif temp_cuerpo > 38.0:
        bg_color = "#742a2a"  # Rojo calor
        modo_texto = "🔥 MODO VENTILACIÓN ACTIVO"
        bateria_actual = "78% (Consumo Moderado 🌀)"
        desc_estado = (
            "El sensor detectó calor excesivo. Los micro-ventiladores expulsan"
            " el aire caliente."
        )
    else:
        bg_color = "#1c4532"  # Verde estable
        modo_texto = "✅ ESTADO ESTABLE (CONFORT)"
        bateria_actual = "85% (Ahorro de Energía 🔋)"
        desc_estado = (
            "El estudiante está en temperatura ideal. Los sistemas entran en"
            " reposo."
        )

    # Inyectar CSS dinámico para cambiar el fondo de la app completa
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.subheader(modo_texto)
    st.write(desc_estado)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Nivel de Batería", value=bateria_actual)
    with col2:
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
        "💡 **Nota de Exposición:** El fondo de toda la interfaz cambia de color"
        " automáticamente según la climatización y el esfuerzo del sistema."
    )
