
import streamlit as st
import pandas as pd
from datetime import datetime

# 설정
st.set_page_config(page_title="직무스트레스 설문 시스템", layout="centered")

# 로고 표시
st.image("직무스트레스.png", use_container_width=True)
st.title("직무스트레스 설문 시스템")

# 대상자 명단 불러오기
@st.cache_data
def load_user_data():
    return pd.read_excel("(R01)롯데첨단_근골(설문,작업목록).xlsx")

user_df = load_user_data()

# 본인 인증
st.subheader("본인 인증")
name = st.text_input("이름을 입력하세요")
phone = st.text_input("전화번호 끝 4자리를 입력하세요")

authenticated = False
user_info = None

if name and phone:
    matched = user_df[
        (user_df["성명"].astype(str).str.strip() == name.strip()) &
        (user_df["휴대폰"].astype(str).str[-4:] == phone.strip())
    ]
    if not matched.empty:
        authenticated = True
        user_info = matched.iloc[0]
        st.success(f"{name}님, 인증되었습니다. 설문을 시작하세요.")
    else:
        st.error("대상자 명단에 등록되어 있지 않거나 전화번호가 일치하지 않습니다.")

# 설문 시작
if authenticated:
    st.subheader("기본정보")
    st.text_input("성명", value=user_info["성명"], disabled=True)
    st.text_input("성별", value=user_info["성별"], disabled=True)
    st.text_input("부서", value=user_info["작업부서"], disabled=True)
    st.text_input("생년월일", value=str(user_info["생년월일"]), disabled=True)

    birth = pd.to_datetime(user_info["생년월일"], errors='coerce')
    if pd.notnull(birth):
        today = pd.to_datetime("today")
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        st.text_input("만 나이", value=f"{age}세", disabled=True)

    st.write("---")
    st.subheader("설문 예시 (문항 일부 구현)")

    q1 = st.radio("1. 근무 장소가 깨끗하고 쾌적하다.", ["전혀 그렇지 않다", "그렇지 않다", "그렇다", "매우 그렇다"])
    q2 = st.radio("2. 내 일은 사고를 당할 가능성이 있다.", ["전혀 그렇지 않다", "그렇지 않다", "그렇다", "매우 그렇다"])

    submitted = st.button("제출")
    if submitted:
        st.success("설문이 제출되었습니다. 감사합니다.")
