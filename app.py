import streamlit as st

st.set_page_config(
    page_title="Cyber-Vesta", page_icon="🧥", layout="centered"
)

st.title("🧥 Cyber-Vesta: Control Térmico Inteligente")
st.write(
    "Sistema de termorregulación automatizada para prendas escolares."
)

temp_cuerpo = st.slider(
    "Temperatura corporal simulada (°C)", 30.0, 40.0, 36.5
)

if temp_cuerpo < 35.5:
    st.error(
        "❄️ Temperatura baja detectada. **Calefacción activada (Modo Ártico)**."
    )
elif temp_cuerpo > 38.0:
    st.warning(
        "🔥 Calor excesivo detectado. **Micro-ventiladores activados**."
    )
else:
    st.success("✅ Temperatura estable. Sistema en modo de espera.")

st.metric(label="Nivel de Batería de la Casaca", value="85%")
