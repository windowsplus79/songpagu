import streamlit as st
import pandas as pd

# 데이터 정의
school_data = [
    {"유형": "일반계", "학교명": "가락고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://garak.sen.hs.kr"},
    {"유형": "일반계", "학교명": "문현고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://munhyeon.sen.hs.kr"},
    {"유형": "일반계", "학교명": "방산고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://bangsan.sen.hs.kr"},
    {"유형": "일반계", "학교명": "오금고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://ogeum.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠실고등학교", "성별": "남자", "설립": "공립", "홈페이지": "https://jamsil.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠실여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://jamsilg.sen.hs.kr"},
    {"유형": "일반계", "학교명": "잠신고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://jamsin.sen.hs.kr"},
    {"유형": "일반계", "학교명": "영동일고등학교", "성별": "남녀공학", "설립": "사립", "홈페이지": "https://ydi.sen.hs.kr"},
    {"유형": "일반계", "학교명": "영파여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://youngpa.sen.hs.kr"},
    {"유형": "일반계", "학교명": "정신여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://chungshin.sen.hs.kr"},
    {"유형": "일반계", "학교명": "창덕여자고등학교", "성별": "여자", "설립": "사립", "홈페이지": "https://changduk.sen.hs.kr"},
    {"유형": "특목고", "학교명": "서울체육고등학교", "성별": "남녀공학", "설립": "공립", "홈페이지": "https://seoul-ph.sen.hs.kr"},
    {"유형": "자사고", "학교명": "보인고등학교", "성별": "남자", "설립": "사립", "홈페이지": "https://boin.hs.kr"},
]

# DataFrame 생성
df = pd.DataFrame(school_data)

st.title("📘 서울 송파구 고등학교 정보")

for school_type in ["일반계", "특목고", "자사고"]:
    st.subheader(f"🏫 {school_type} 고등학교")
    filtered = df[df["유형"] == school_type].copy()

    # 학교명에 하이퍼링크 추가
    filtered["학교명"] = filtered.apply(
        lambda row: f"[{row['학교명']}]({row['홈페이지']})", axis=1
    )

    # 표 출력 (학교명은 링크, 홈페이지 주소는 그대로 표시)
    st.markdown(
        filtered[["학교명", "성별", "설립", "홈페이지"]]
        .reset_index(drop=True)
        .to_markdown(index=False),
        unsafe_allow_html=True
    )
