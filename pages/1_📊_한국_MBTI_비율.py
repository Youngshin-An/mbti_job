import streamlit as st

st.set_page_config(page_title="한국 MBTI 비율", page_icon="📊", layout="centered")

st.title("📊 우리나라 MBTI 비율 분포")
st.caption("대한민국 청소년 및 성인 응답자 기준 (16Personalities 통계 기반 데이터)")

st.info(
    "💡 **우리나라 사람들은 어떤 MBTI 유형이 가장 많을까요?**\n\n"
    "온라인 조사 통계에 따르면 대한민국에서는 **INFP, ENFP, ESFJ, ISFP** 등이 높은 비중을 차지합니다.\n"
    "그래프를 통해 한국인의 성향 분포를 직접 확인해보세요!"
)

# 대한민국 MBTI 비율 데이터 (약)
korea_mbti_data = {
    "INFP": 13.39,
    "ENFP": 12.60,
    "ESFJ": 8.35,
    "ISFP": 7.65,
    "INTP": 6.30,
    "INFJ": 6.25,
    "ENFJ": 6.10,
    "ESFP": 5.80,
    "ENTP": 5.04,
    "ESTJ": 4.56,
    "ISTJ": 4.28,
    "INTJ": 3.75,
    "ISTP": 3.11,
    "ESTP": 2.94,
    "ENTJ": 2.73,
    "ISFJ": 7.15
}

# 정렬
sorted_data = dict(sorted(korea_mbti_data.items(), key=lambda x: x[1], reverse=True))

st.markdown("### 🇰🇷 대한민국 16가지 MBTI 비율 (%)")
st.bar_chart(sorted_data)

st.write("---")
st.markdown("### 🏆 한국에서 가장 높은 MBTI TOP 3")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🥇 1위 (13.39%)", value="INFP", delta="열정적인 중재자")
with col2:
    st.metric(label="🥈 2위 (12.60%)", value="ENFP", delta="재기발랄한 활동가")
with col3:
    st.metric(label="🥉 3위 (8.35%)", value="ESFJ", delta="사교적인 외교관")

st.write("")
st.markdown("### 💡 상담 선생님의 인사이트")
st.write(
    "- **N(직관형)과 F(감정형) 비율이 높아요:** 한국의 온라인 응답자 중에는 감수성이 풍부하고 "
    "내면의 가치와 성장에 관심이 많은 **INFP / ENFP** 청소년 및 청년층이 많은 편이에요.\n"
    "- **유형이 적다고 이상한 게 아니에요:** ENTJ나 ESTP처럼 비율이 상대적으로 낮더라도, "
    "그만큼 우리 사회에서 희소성 있고 독창적인 리더십과 순발력을 발휘할 수 있다는 뜻이랍니다! 🌱"
)
