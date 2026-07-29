import streamlit as st

st.set_page_config(page_title="MBTI 맞춤 학습법", page_icon="📚", layout="centered")

st.title("📚 [추천] MBTI별 맞춤 공부법 & 스트레스 해소 팁")
st.caption("중·고등학생을 위한 맞춤형 시험 대비 전략 및 멘탈 관리법")

st.info(
    "✏️ **나에게 꼭 맞는 공부법을 찾으면 효율이 2배!**\n\n"
    "친구들마다 집중이 잘 되는 환경과 공부 스타일이 모두 달라요.\n"
    "자신의 MBTI 대표 알파벳 선호도에 따른 **맞춤 공부법**과 **스트레스 관리법**을 확인해 보세요!"
)

# 4가지 축 선택
tab1, tab2, tab3, tab4 = st.tabs(["[E vs I] 에너지 방향", "[S vs N] 정보 인식", "[T vs F] 의사 결정", "[J vs P] 생활 양식"])

with tab1:
    st.subheader("⚡ 에너지 방향에 따른 공부법 (E vs I)")
    col_e, col_i = st.columns(2)
    with col_e:
        st.markdown("#### 🗣️ E (외향형)")
        st.write("- **추천 공부법:** 스터디 그룹 활용, 친구에게 설명하면서 외우기, 질문 주고받기")
        st.write("- **장점:** 말하면서 개념 정리할 때 기억이 오래 남음")
        st.write("- **주의점:** 너무 수다로 빠지지 않도록 시간 정해두기")
    with col_i:
        st.markdown("#### 🎧 I (내향형)")
        st.write("- **추천 공부법:** 조용한 독서실/자습실, 혼자 오답노트 작성하기, 인강 자습")
        st.write("- **장점:** 혼자 깊게 몰입할 때 최상의 집중력 발휘")
        st.write("- **주의점:** 모르는 문제는 혼자 끙끙대지 말고 질문하기")

with tab2:
    st.subheader("🔍 정보 인식에 따른 공부법 (S vs N)")
    col_s, col_n = st.columns(2)
    with col_s:
        st.markdown("#### 📝 S (감각형)")
        st.write("- **추천 공부법:** 단계별 문제 풀이, 요약 노트 필기, 기출문제 반복")
        st.write("- **장점:** 꼼꼼하고 실질적인 사실과 공식을 정확히 암기함")
        st.write("- **주의점:** 전체적인 큰 그림과 개념 흐름 놓치지 않기")
    with col_n:
        st.markdown("#### 💡 N (직관형)")
        st.write("- **추천 공부법:** 마인드맵 그리기, 개념 간의 연관성 파악, 원리와 배경 이해")
        st.write("- **장점:** 전체적인 맥락과 창의적 문제 해결력이 뛰어남")
        st.write("- **주의점:** 세부적인 계산 실수나 단어 암기 꼼꼼히 점검하기")

with tab3:
    st.subheader("⚖️ 의사 결정에 따른 공부법 (T vs F)")
    col_t, col_f = st.columns(2)
    with col_t:
        st.markdown("#### 📊 T (사고형)")
        st.write("- **추천 공부법:** 논리적 원리 분석, 오답 원인 정확히 분류, 목표 수치화")
        st.write("- **장점:** 객관적이고 냉철하게 자신의 부족한 점 판단")
        st.write("- **주의점:** 성적 결과만으로 자책하지 않기")
    with col_f:
        st.markdown("#### ❤️ F (감정형)")
        st.write("- **추천 공부법:** 칭찬과 긍정적 보상 활용, 공부하는 의미와 가치 부여")
        st.write("- **장점:** 동기 부여가 되면 엄청난 열정과 집중력 발휘")
        st.write("- **주의점:** 시험 결과에 감정적으로 너무 흔들리지 않기")

with tab4:
    st.subheader("📅 생활 양식에 따른 공부법 (J vs P)")
    col_j, col_p = st.columns(2)
    with col_j:
        st.markdown("#### 🗓️ J (판단형)")
        st.write("- **추천 공부법:** 주간/일간 플래너 작성, 쪼개서 일관되게 공부하기")
        st.write("- **장점:** 체계적인 계획 달성률이 매우 높음")
        st.write("- **주의점:** 계획이 틀어져도 유연하게 대처하기")
    with col_p:
        st.markdown("#### 🚀 P (인식형)")
        st.write("- **추천 공부법:** 뽀모도로 기법(25분 집중, 5분 휴식), 짧은 집중 몰입")
        st.write("- **장점:** 벼락치기나 단기 몰입력이 엄청남")
        st.write("- **주의점:** 시험 직전에 당황하지 않도록 최소한의 틀 잡기")

st.write("---")

st.markdown("### 🌿 시험 기간 MBTI별 스트레스 해소법")
st.success(
    "🧘 **상담 선생님의 팁:**\n"
    "- **E/P 친구들:** 가벼운 산책, 음악 듣기, 친구와 짧은 힐링 수다로 기분 전환!\n"
    "- **I/J 친구들:** 따뜻한 차 마시기, 다이어리 적기, 충분한 수면으로 뇌 휴식 주기!"
)
