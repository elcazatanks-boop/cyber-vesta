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
    # Visualización de sistema apagado
    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>❌</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: red;'>Sistema Inactivo</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.metric(label="Estado", value="Inactivo 🔴")
else:
    st.success("🟢 Sistema **ENCENDIDO** y operando en tiempo real.")

    # Controles de temperatura
    temp_cuerpo = st.slider(
        "Simular Temperatura Corporal (°C)", 30.0, 40.0, 36.5
    )

    # --- Lógica de Visualización (Usando Emojis en vez de Imágenes) ---
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Mostrar el estado visual grande
        if temp_cuerpo < 35.5:
            st.markdown("<h1 style='text-align: center; font-size: 150px;'>❄️🔥🔥</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center; color: blue;'>CALEFACCIÓN ACTIVADA</h2>", unsafe_allow_html=True)
            st.error("El sistema detectó frío extremo y está elevando la temperatura interna.")
        elif temp_cuerpo > 38.0:
            st.markdown("<h1 style='text-align: center; font-size: 150px;'>🔥🔥🌀🌀</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center; color: orange;'>VENTILADORES ACTIVADOS</h2>", unsafe_allow_html=True)
            st.warning("El sistema detectó calor excesivo y activó la ventilación para enfriar.")
        else:
            st.markdown("<h1 style='text-align: center; font-size: 150px;'>✅🌡️</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='text-align: center; color: green;'>TEMPERATURA ESTABLE</h2>", unsafe_allow_html=True)
            st.success("El estudiante se encuentra en su zona de confort. Sistemas en reposo.")

    with col2:
        # Mostrar datos de telemetría
        st.metric(label="Nivel de Batería", value="83%")
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
        "💡 **Nota de Exposición:** Esta interfaz web simula el control"
        " electrónico de la casaca. Al mover el deslizador en tu celular, la"
        " visualización responde instantáneamente para demostrar la lógica del"
        " prototipo."
    )
