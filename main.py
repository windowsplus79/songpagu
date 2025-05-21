import streamlit as st
import pandas as pd

# 일반계 고등학교 데이터만
school_data = [
    {"학교명": "가락고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://garak.sen.hs.kr"},
    {"학교명": "문현고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://munhyeon.sen.hs.kr"},
    {"학교명": "방산고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://bangsan.sen.hs.kr"},
    {"학교명": "오금고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://ogeum.sen.hs.kr"},
    {"학교명": "잠실고등학교", "성별": "남자", "설립": "공립", "홈페이지": "https://jamsil.sen.hs.kr"},
    {"학교명": "잠실여자고등학교", "성별": "여자", "설립": "공립", "홈페이지": "https://jamsilyeo.sen.hs.kr"},
    {"학교명": "잠신고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://jamsin.sen.hs.kr"},
    {"학교명": "영동일고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://youngdongil.sen.hs.kr"},
    {"학교명": "영파여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://youngpa.sen.hs.kr"},
    {"학교명": "정신여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://jeongsin.sen.hs.kr"},
    {"학교명": "창덕여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://changduk.sen.hs.kr"},
]

# DataFrame 생성
df = pd.DataFrame(school_data)

st.title("🏫 서울 송파구 일반계 고등학교")

# 학교명을 하이퍼링크로 변환
df["학교명"] = df.apply(
    lambda row: f"[{row['학교명']}]({row['홈페이지']})", axis=1
)

# 표시할 컬럼 순서
display_df = df[["학교명", "성별", "설립"]]

# 마크다운 테이블 출력
st.markdown(display_df.to_markdown(index=False), unsafe_allow_html=True)
