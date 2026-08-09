import streamlit as st
from google import genai

st.set_page_config(page_title="Акылман AI", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2C3E50;'>🧠 Акылман AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Рекламасыз, толугу менен акысыз акылдуу ассистент</p>", unsafe_allow_html=True)

st.sidebar.header("⚙️ Жөндөөлөр")
api_key = st.sidebar.text_input("Gemini API Key киргизиңиз:", type="password")

SYSTEM_PROMPT = "Сиз 'Акылман AI' атуу кыргыз тилинде сүйлөгөн акылдуу, сылык жана пайдалуу ассистентсиз. Суроолорго кыска, так жана түшүнүктүү жооп бериңиз."

if api_key:
    try:
        client = genai.Client(api_key=api_key)

        st.subheader("🎤 Суроо бериңиз:")
        user_text = st.text_input("Сурооңузду жазыңыз:")

        if user_text:
            with st.spinner("Акылман AI ойлонуп жатат..."):
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"{SYSTEM_PROMPT}\n\nКолдонуучу: {user_text}"
                )
                st.markdown(f"### 🤖 Жооп:\n{response.text}")

    except Exception as e:
        st.error(f"Ката кетти: {e}")
else:
    st.info("💡 Иштетүү үчүн сол менюга API ачкычыңызды жазыңыз.")
