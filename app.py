import streamlit as st
from ai_core import generate_idea

st.set_page_config(page_title="LowkeyCreator AI", page_icon="🎯")

st.title("🎯 LowkeyCreator AI")
st.markdown("Hızlı içerik fikirleri üretin!")

user_prompt = st.text_input("💡 Ne hakkında içerik üretmek istiyorsunuz?")

if st.button("Fikir Üret"):
    if user_prompt.strip():
        with st.spinner("Fikirler üretiliyor..."):
            result = generate_idea(user_prompt)
        st.subheader("✨ AI Önerileri:")
        st.write(result)
    else:
        st.warning("Lütfen bir konu girin.")
