import streamlit as st
import time

# ---------- CONFIGURACIÓN DE LA PÁGINA ----------
st.set_page_config(
    page_title="Love Letter | De mi para tu",
    page_icon="♡",
    layout="centered"
)

# Estilos CSS personalizados para mantener tus colores originales
st.markdown("""
    <style>
    .stApp {
        background-color: #10070D;
    }
    .main-panel {
        background-color: #1D0D17;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #49202F;
    }
    h1, h2, h3, p, label {
        color: #FFF0F4 !important;
        font-family: 'Segoe UI', sans-serif;
    }
    .subtitle {
        color: #FF7895 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- ENCABEZADO ----------
st.markdown("<div style='text-align: center; font-size: 35px; color: #FF315A;'>♡</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 28px;'>Para mi persona favorita</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FF7895; font-size: 13px;'>konichiwa</p>", unsafe_allow_html=True)

# ---------- PANEL PRINCIPAL ----------
st.markdown('<div class="main-panel">', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; font-family: Georgia, serif; font-style: italic; font-size: 18px;'>Oye my princess, te hize este programa brodio :)</h3>", unsafe_allow_html=True)

# Entrada de texto (interactiva para celular o compu)
texto_usuario = st.text_input("Escribe tu nombre, princesa:", placeholder="Escribe aquí...")

if st.button("CREAR MI CORAZÓN ♡", type="primary"):
    texto = texto_usuario.strip().upper()
    
    if not texto:
        st.warning("Nesecito tu nameeee ♡")
    else:
        with st.spinner("ESCRIBIENDO..."):
            time.sleep(1) # Pequeña pausa emotiva
            
            # Generación de la matriz del corazón usando tu lógica matemática
            corazon_lineas = []
            y = 1.25
            while y >= -1.25:
                x = -1.45
                linea_actual = ""
                while x <= 1.45:
                    forma = (x*x + y*y - 1)**3 - x*x*y**3
                    if forma <= 0:
                        # Selecciona la letra del nombre de forma cíclica
                        letra = texto[len(corazon_lineas) % len(texto)]
                        linea_actual += letra + " "
                    else:
                        linea_actual += "  "
                    x += 0.085
                corazon_lineas.append(linea_actual)
                y -= 0.105

            # Mostrar el resultado en pantalla
            resultado_final = "\n".join(corazon_lineas)
            st.text_code(resultado_final)
            
            st.balloons() # ¡Efecto de globos en la web!
            
            st.markdown(f"<h2 style='text-align: center; color: #FF7895; font-family: Georgia, serif;'>I love you {texto.title()} &lt;3</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #886775; font-size: 11px;'>Un intento de hacerte el trend... ♡</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
