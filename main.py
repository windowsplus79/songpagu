import streamlit as st
import pandas as pd

# 데이터
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

df = pd.DataFrame(school_data)

st.title("🏫 서울 송파구 일반계 고등학교")

# 학교명 하이퍼링크 HTML 생성
def make_html_table(df):
    html = """
    <table style='width:100%; border-collapse: collapse;' border='1'>
        <thead>
            <tr>
                <th>학교명</th>
                <th>성별</th>
                <th>설립</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        html += f"""
            <tr>
                <td><a href="{row['홈페이지']}" target="_blank">{row['학교명']}</a></td>
                <td>{row['성별']}</td>
                <td>{row['설립']}</td>
            </tr>
        """
    html += "</tbody></table>"
    return html

html_table = make_html_table(df)
st.markdown(html_table, unsafe_allow_html=True)
