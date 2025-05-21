import streamlit as st
import pandas as pd

# 데이터 정의
school_data = [
    # 일반계
    {"유형": "일반계", "학교명": "가락고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://garak.sen.hs.kr"},
    {"유형": "일반계", "학교명": "문현고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://munhyeon.sen.hs.kr"},
    {"유형": "일반계", "학교명": "방산고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://bangsan.sen.hs.kr"},
    {"유형": "일반계", "학교명": "오금고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://ogeum.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠실고등학교", "성별": "남자", "설립": "공립", "홈페이지": "https://jamsil.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠실여자고등학교", "성별": "여자", "설립": "공립", "홈페이지": "https://jamsilyeo.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠신고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://jamsin.sen.hs.kr"},
    {"유형": "일반계", "학교명": "영동일고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://youngdongil.sen.hs.kr"},
    {"유형": "일반계", "학교명": "영파여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://youngpa.sen.hs.kr"},
    {"유형": "일반계", "학교명": "정신여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://jeongsin.sen.hs.kr"},
    {"유형": "일반계", "학교명": "창덕여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://changduk.sen.hs.kr"},
    
    # 특목고
    {"유형": "특목고", "학교명": "서울체육고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://seoulsports.sen.hs.kr"},
    
    # 자사고
    {"유형": "자사고", "학교명": "보인고등학교", "성별": "남자", "설립": "사립", "홈페이지": "https://boin.hs.kr"},
]

# DataFrame 생성
df = pd.DataFrame(school_data)

st.title("서울 송파구 고등학교 목록")

# 유형별 출력
for school_type in ["일반계", "특목고", "자사고"]:
    st.header(f"🏫 {school_type} 고등학교")
    filtered = df[df["유형"] == school_type].copy()
    filtered["홈페이지"] = filtered["홈페이지"].apply(lambda url: f"[{url}]({url})")
    st.write(
        filtered[["학교명", "성별", "설립", "홈페이지"]].reset_index(drop=True).to_markdown(index=False),
        unsafe_allow_html=True
    )
