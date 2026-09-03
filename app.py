import streamlit as st

st.set_page_config(
    page_title="Cyber-Vesta: Control Inteligente",
    page_icon="🧥",
    layout="centered",
)

st.title("🧥 Cyber-Vesta: Casaca Inteligente")
st.write(
    "Proyecto de EPT: Sistema de termorregulación automatizada y monitoreo de energía."
)

# Botón de encendido principal de la casaca
estado_energia = st.toggle(
    "🔌 Encender / Apagar Sistema de la Casaca", value=True
)

if not estado_energia:
    st.warning(
        "⚠️ El sistema está **APAGADO**. Enciéndelo para activar el control"
        " térmico y los ventiladores."
    )
    st.metric(label="Estado del Sistema", value="Inactivo 🔴")
else:
    st.success("🟢 Sistema **ENCENDIDO** y operando en tiempo real.")

    # Controles de temperatura
    temp_cuerpo = st.slider(
        "Simular Temperatura Corporal (°C)", 30.0, 40.0, 36.5
    )

    col1, col2 = st.columns(2)

    with col1:
        if temp_cuerpo < 35.5:
            st.error(
                "❄️ **Frío extremo detectado**\n\nCalefacción interna:"
                " **ENCENDIDA** 🔥"
            )
        elif temp_cuerpo > 38.0:
            st.warning(
                "🔥 **Calor excesivo detectado**\n\nMicro-ventiladores:"
                " **GIRANDO A MÁXIMA VELOCIDAD** 🌀"
            )
        else:
            st.success(
                "✅ **Temperatura óptima**\n\nSistemas en reposo (Ahorro de"
                " energía)."
            )

    with col2:
        st.metric(label="Nivel de Batería (Power Bank)", value="84%")
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
        "💡 **Nota de exposición:** Este prototipo web reemplaza el circuito"
        " físico para demostrar la lógica de sensores y actuadores de forma"
        " interactiva desde cualquier smartphone."
    )
