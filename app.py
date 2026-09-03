import streamlit as st

st.set_page_config(
    page_title="Cyber-Vesta: Control Inteligente",
    page_icon="🧥",
    layout="centered",
)

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
    # Casaca escolar genérica apagada (azul/blanco/rojo)
    st.image(
        "https://i.ibb.co/3TqGjK9/casaca-escolar-base.png",
        caption="Sistema Inactivo",
        width=350,
    )
    st.metric(label="Estado del Sistema", value="Inactivo 🔴")
else:
    st.success("🟢 Sistema **ENCENDIDO** y operando en tiempo real.")

    # Controles de temperatura
    temp_cuerpo = st.slider(
        "Simular Temperatura Corporal (°C)", 30.0, 40.0, 36.5
    )

    # --- Lógica de Visualización de la Casaca (Diseño Escolar) ---
    col_img, col_info = st.columns([1, 1])

    with col_img:
        if temp_cuerpo < 35.5:
            # Casaca con efecto de calefacción
            st.image(
                "https://i.ibb.co/3F03dC5/casaca-escolar-calefaccion.gif",
                caption="❄️ CALEFACCIÓN ACTIVADA 🔥",
                width=350,
            )
        elif temp_cuerpo > 38.0:
            # Casaca con efecto de ventilación
            st.image(
                "https://i.ibb.co/WkXvj1J/casaca-escolar-ventilacion.gif",
                caption="🔥 VENTILADORES ACTIVADOS 🌀",
                width=350,
            )
        else:
            # Casaca base (estable)
            st.image(
                "https://i.ibb.co/3TqGjK9/casaca-escolar-base.png",
                caption="✅ Temperatura Estable",
                width=350,
            )

    with col_info:
        if temp_cuerpo < 35.5:
            st.error(
                "❄️ **Frío extremo detectado**\n\nLa calefacción interna se ha"
                " activado para proteger al estudiante. El sistema inteligente"
                " regula la temperatura a 22°C internos."
            )
        elif temp_cuerpo > 38.0:
            st.warning(
                "🔥 **Calor excesivo detectado**\n\nLos micro-ventiladores se han"
                " activado para disipar el calor y reducir la humedad."
            )
        else:
            st.success(
                "✅ **Temperatura óptima**\n\nEl sistema monitorea los"
                " biosensores y mantiene el confort, ahorrando energía."
            )

        st.metric(label="Nivel de Batería (Power Bank)", value="83%")

    st.markdown("---")
    st.info(
        "💡 **Nota de Exposición:** Esta interfaz web simula el control"
        " electrónico de la casaca. Al mover el deslizador en tu celular, la"
        " visualización se actualiza instantáneamente para demostrar la"
        " lógica de respuesta de los actuadores."
    )
