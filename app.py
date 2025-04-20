
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="직무스트레스 설문 시스템", layout="centered")

if Path("직무스트레스.png").exists():
    st.image("직무스트레스.png", use_container_width=True)
else:
    st.warning("로고 이미지가 없습니다.")

st.title("직무스트레스 설문 시스템")
st.write("안녕하세요. 본 설문은 직무스트레스 수준을 확인하기 위한 목적이며, 응답 내용은 익명으로 처리됩니다.")
