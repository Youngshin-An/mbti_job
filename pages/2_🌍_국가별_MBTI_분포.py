import streamlit as st

st.set_page_config(page_title="국가별 MBTI 분포", page_icon="🌍", layout="centered")

st.title("🌍 나라별 MBTI 대표 성향 & 분포")
st.caption("세계 여러 나라 사람들의 MBTI 분포 특징과 문화적 성향 비교")

st.info(
    "🌏 **국가마다 사회 문화에 따라 많이 나타나는 MBTI 성향이 다를까요?**\n\n"
    "각 국가별로 데이터에서 상대적으로 높게 나타나는 주요 유형들을 선택해서 비교해보세요!"
)

# 주요 국가별 대표 MBTI 비율 데이터 (샘플 통계)
country_data = {
    "대한민국 🇰🇷": {
        "INFP": 13.4, "ENFP": 12.6, "ESFJ": 8.4, "ISFP": 7.7, "ISTJ": 4.3, "INTJ": 3.8
    },
    "미국 🇺🇸": {
        "ENFP": 11.2, "ESFJ": 10.5, "INFP": 9.8, "ESTJ": 8.7, "ISTJ": 8.1, "INTJ": 4.2
    },
    "일본 🇯🇵": {
        "INFP": 12.8, "ISFJ": 11.2, "ENFP": 9.5, "ISTJ": 8.5, "ISFP": 7.9, "INFJ": 6.8
    },
    "독일 🇩🇪": {
        "ISTJ": 12.5, "INFP": 11.1, "INTJ": 8.4, "INTP": 7.8, "ESTJ": 7.2, "ENFP": 8.9
    },
    "싱가포르 🇸🇬": {
        "ISTJ": 11.8, "ESTJ": 9.4, "INFP": 10.2, "ENFP": 8.8, "INTJ": 6.5, "ISFJ": 8.1
    }
}

selected_country = st.selectbox("📌 국가를 선택하세요:", list(country_data.keys()))

st.markdown(f"### {selected_country} 주요 MBTI 비율 (%)")
st.bar_chart(country_data[selected_country])

st.write("---")

st.markdown("### 🔎 국가별 대표 특징 정리")

st.markdown("""
- **🇰🇷 대한민국:** N(직관)과 F(감정) 비율이 높으며, 개인의 꿈과 표현, 공감 능력을 중시하는 성향이 강해지는 추세입니다.
- **🇺🇸 미국:** E(외향)와 J(판단) 비율이 상대적으로 높으며, 외향적 소통과 자기주장, 실용적인 성과를 선호하는 문화입니다.
- **🇯🇵 일본:** I(내향)와 S(감각), J(판단) 비율이 높아서, 타인에 대한 배려, 질서 유지, 신중함을 중요하게 생각합니다.
- **🇩🇪 독일:** T(사고)와 J(판단), I(내향) 비율이 높아, 논리적이고 규칙을 준수하며 효율적인 시스템을 선호합니다.
""")

st.success("💡 **상담 선생님의 팁:** 다른 나라도 저마다 매력적인 문화적 성향을 지니고 있듯이, 어떤 MBTI든 우월함이 없고 서로 다른 장점을 가지고 있답니다!")
