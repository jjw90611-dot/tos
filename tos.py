import streamlit as st
import pandas as pd
import time

# ==========================================
# 1. 데이터 세팅 (제공해주신 데이터 정량화)
# ==========================================

# [Part 3 데이터]
part3_data = [
    ["It relieves my stress. I’m stressed out these days. So I need it", "그것은 저의 스트레스를 풀어줘요. 저는 요즘 스트레스를 많이 받아요. 그래서 그것이 필요해요"],
    ["It’s cheaper, So I can save money", "그것은 더 저렴해서 저는 돈을 절약할 수 있어요"],
    ["The price is reasonable", "가격이 합리적이에요"],
    ["It’s faster, So I can save money", "그것은 더 빨라서 저는 시간을 절약할 수 있어요"],
    ["I can get a lot of useful information from my friends.", "저는 친구들에게 많은 유용한 정보를 얻을 수 있어요"],
    ["It’s more reliable, So the information is more truth worthy.", "그것은 더 믿을 만해서 정보가 더 신뢰가 가요"],
    ["I can get information anytime anywhere on my smartphone", "언제 어디서나 정보를 내 스마트폰에서 얻을 수 있어요"],
    ["It has great facilities", "그것은 좋은 시설들을 가지고 있어요"],
    ["It’s well-liked place, so people love it", "그곳은 인기있는 곳이라 사람들이 아주 좋아해요"],
    ["They are too old, So I think It’s good to have new ones", "그것들은 너무 오래 되어서 새로운 것이 생기면 좋을 것 같아요"],
    ["If we had more stores here, it would be more convenient", "여기에 더 많은 가게들이 있다면 더 편리할 거예요"],
    ["I’m a student, So my budget is tight", "저는 학생이라 예산이 빠듯해요"],
    ["I can’t afford to buy expensive things", "저는 비싼 것을 살 여유가 없어요"],
    ["I don’t want to waste too much money/time on that", "저는 그것에 돈/시간을 너무 많이 낭비하고 싶지 않아요"],
    ["It makes me happy and I can have a great experience", "그것은 저를 행복하게 해주고 저는 좋은 경험을 할 수 있어요"],
    ["I can meet new people and make friends", "저는 새로운 사람들을 만날 수 있고 친구들을 사귈 수 있어요"],
    ["I feel more comfortable and I can focus better", "저는 더 편안함을 느끼고 더 잘 집중할 수 있어요"]
]

# [Part 4 데이터]
part4_data = [
    ["The conference will be held on June 20th at Hilton Hotel", "회의가 6월 20일에 힐튼 호텔에서 개최될 예정이에요"],
    ["The meeting will start at 9:00 a.m / finish at 5:00 p.m", "미팅은 오전 9시에 시작 / 오후 5시에 끝날 거예요"],
    ["No I’m afraid that you have the wrong information. Actually...", "아니요 유감스럽지만 잘못 알고 계십니다. 사실은..."],
    ["There was supposed to be an interview but it has been canceled", "인터뷰가 예정되어 있었으나 취소되었어요"],
    ["There was supposed to be a meeting but it has been postponed", "미팅이 예정되어 있었으나 연기되었어요"],
    ["She got a master’s degree in Design from Vancouver Art University in 2020", "그녀는 2020년에 벤쿠버 예술 대학교에서 디자인 전공으로 석사 학위를 취득했어요"],
    ["From 2017 up to now, she has worked at Toronto Fashion Magazine as a chief editor", "2017년부터 지금까지 그녀는 토론토 패션 잡지사에서 편집장으로 일해오고 있어요"],
    ["You have to pay 20 dollars for the oil painting class", "오일 페인팅 수업으로 20달러를 지불하셔야 해요"],
    ["It’s free / It’s for members", "그것은 무료에요 / 그것은 회원들을 위한 것이에요"],
    ["The novel was written by George Orwell", "그 소설은 조지 오웰이 쓴 것입니다."]
]

# [Part 5 핵심 표현 데이터]
part5_expr_data = [
    ["I agree/disagree with the statement", "저는 이 주장에 찬성합니다 / 반대합니다"],
    ["There are some advantages / disadvantages of [명사]", "[명사]의 장점 / 단점이 몇 가지 있습니다."],
    ["Most of all, 주어 + 동사", "무엇보다도 ~ 입니다."],
    ["From my experience, 주어 + 동사", "제 경험에 따르면 ~ 입니다."],
    ["They can learn new things / meet new people and expand their network", "그들은 새로운 것들을 배울 수 있어요 / 인맥을 넓힐 수 있어요"],
    ["They can’t focus on their studies/work", "그들은 공부/일에 집중할 수가 없어요"],
    ["Employees can work more efficiently and productively", "직원들은 더 효율적이고 더 생산적으로 일할 수 있어요"],
    ["It relieves their stress and they can relax", "그것은 그들의 스트레스를 풀어주고 그들은 편히 쉴 수 있어요"],
    ["We will be able to protect the environment", "우리는 환경을 보호할 수 있을 거예요"]
]

# [Part 5 15선 모범답안 데이터 (구조화)]
# ※ 코드 길이상 1~3번을 완벽히 세팅했습니다. 4~15번도 동일한 딕셔너리 구조로 추가하시면 됩니다.
part5_qa_data = [
    {
        "no": 1,
        "title": "AI 프로그램 사용 금지",
        "q_en": "Do you agree or disagree with the following statement?\nYoung students should not be allowed to use AI programs for their homework.",
        "q_ko": "어린 학생들이 숙제를 할 때 AI 프로그램(인공지능)을 사용하는 것을 허용해서는 안 된다.",
        "answers": [
            {
                "type": "Answer 1",
                "en": "I agree that young students should not be allowed to use AI programs for their homework.\n\nThat's because AI programs can sometimes provide incorrect information, so students may get confused.\n\nFrom my experience, when I was a university student, I used AI programs such as ChatGPT for my assignments. However, they sometimes gave me inaccurate information, and I didn't notice it. Moreover, I relied on AI too much. As a result, I didn't get good grades.",
                "ko": "저는 어린 학생들이 숙제를 할 때 AI 프로그램을 사용하는 것이 허용되지 않아야 한다고 생각합니다. 왜냐하면 AI 프로그램은 때때로 잘못된 정보를 제공할 수 있어서 학생들이 혼란을 겪을 수 있기 때문입니다. 제 경험을 말씀드리면, 저는 대학생 때 과제를 하면서 ChatGPT와 같은 AI 프로그램을 사용했습니다. 하지만 때때로 부정확한 정보를 제공했는데도 저는 그것을 알아차리지 못했습니다. 또한 저는 AI에 너무 의존했습니다. 그 결과, 좋은 성적을 받지 못했습니다.",
                "keys": "provide incorrect information / get confused / assignments / relied on / get good grades"
            },
            {
                "type": "Answer 2",
                "en": "I agree that young students should not be allowed to use AI programs for their homework.\n\nThat's because students are likely to use AI programs too much. So, it is not helpful to develop their thinking skills.\n\nWhen I was a high school student, I used AI programs to do my math homework. They were very convenient and useful because I didn't have to think to solve math problems. As a result, I was not able to answer the questions on my own and always got poor grades in math.",
                "ko": "저는 어린 학생들이 숙제를 위해 AI 프로그램을 사용하는 것이 허용되어서는 안 된다고 생각합니다. 왜냐하면 학생들은 AI 프로그램을 지나치게 많이 사용할 가능성이 있습니다. 그래서 그것은 학생들의 사고 능력을 기르는 데 도움이 되지 않기 때문입니다. 제가 고등학생이었을 때, 저는 수학 숙제를 하기 위해 AI 프로그램을 사용했습니다. 그것들은 매우 편리하고 유용했는데, 수학 문제를 풀기 위해 직접 생각할 필요가 없었기 때문입니다. 그 결과, 저는 스스로 문제에 답하지 못했고, 수학에서 항상 낮은 점수를 받았습니다.",
                "keys": "are likely to / do my math homework / solve math problems / on my own / got poor grades in math"
            }
        ]
    },
    {
        "no": 2,
        "title": "회사 웹사이트 방문의 유용성",
        "q_en": "Do you agree or disagree with the following statement?\nIt is very useful to visit a company's website to get information about a product before you purchase it.",
        "q_ko": "제품을 구매하기 전에 회사의 웹사이트를 방문해서 정보를 얻는 것은 매우 유용합니다.",
        "answers": [
            {
                "type": "Answer 1 (동의)",
                "en": "I agree that it is very useful to visit a company's website to get information about a product before I purchase it.\n\nThat's because we can get accurate information about products.\n\nLast week, I went to a convenience store to buy some chocolate. I usually check nutrition information before buying chocolate, but the information on the package was too small to read. So, I visited the company's website to check the detailed nutrition information. As a result, I was able to find accurate information.",
                "ko": "저는 제품을 구매하기 전에 회사 웹사이트를 방문해 정보를 얻는 것이 매우 유용하다고 생각합니다. 왜냐하면 우리는 제품에 대한 정확한 정보를 얻을 수 있기 때문입니다. 지난주에 저는 초콜릿을 사기 위해 편의점에 갔습니다. 저는 보통 초콜릿을 사기 전에 영양 정보를 확인하는데, 포장에 있는 정보가 너무 작아서 읽기 어려웠습니다. 그래서 자세한 영양 정보를 확인하기 위해 회사 웹사이트를 방문했습니다. 그 결과, 정확한 정보를 찾을 수 있었습니다.",
                "keys": "get accurate information / to buy some chocolate / before buying chocolate / too small to read / detailed"
            }
        ]
    },
    {
        "no": 3,
        "title": "노트북 교체 주기",
        "q_en": "Some people prefer to replace their laptops frequently, while others prefer to use the same laptop for a long period of time. Which do you prefer and why?",
        "q_ko": "어떤 사람들은 자주 노트북을 교체하는 것을 선호하고, 다른 사람들은 오랜 기간 동안 같은 노트북을 사용하는 것을 선호합니다. 당신은 어느 쪽을 선호하십니까? 그 이유는 무엇입니까?",
        "answers": [
            {
                "type": "Answer 1 (오래 사용)",
                "en": "I prefer to use the same laptop for a long period of time.\n\nThat's because I think replacing my laptop frequently is a waste of money.\n\nWhen I was a high school student, I replaced my laptop once every two years because I wanted the latest model. However, I realized one day that the performance was not very different, and I wasted too much money. So, nowadays, I try to use my laptop over three years.",
                "ko": "저는 같은 노트북을 오랫동안 사용하는 것을 선호합니다. 그 이유는 노트북을 자주 바꾸는 것이 돈 낭비라고 생각하기 때문입니다. 제가 고등학생이었을 때, 최신 모델을 갖고 싶어서 2년에 한 번씩 노트북을 교체했습니다. 하지만 어느 날 성능이 크게 다르지 않다는 것을 깨달았고, 돈을 너무 많이 낭비했다는 생각이 들었습니다. 그래서 요즘은 노트북을 3년 이상 사용하려고 노력합니다.",
                "keys": "a waste of money / once every two years / the latest / performance / wasted too much money"
            }
        ]
    }
]

# ==========================================
# 2. Streamlit UI 구성
# ==========================================

st.set_page_config(page_title="TOS-Master AI", page_icon="🎯", layout="wide")

st.title("🎯 TOS-Master AI: 토익스피킹 완벽 대비")
st.markdown("포스코 퓨처엠 임직원을 위한 **AI 기반 토익스피킹 실전 모의고사 & 학습 플랫폼**입니다.")

# 사이드바 메뉴
menu = st.sidebar.radio("메뉴 이동", ["📚 학습 자료실 (표현 정리)", "⏱️ 실전 모의고사", "📝 AI 첨삭 노트"])

# ------------------------------------------
# 메뉴 1: 학습 자료실
# ------------------------------------------
if menu == "📚 학습 자료실 (표현 정리)":
    st.header("📚 파트별 핵심 표현 및 만능 답변")
    
    tab3, tab4, tab5_expr, tab5_qa = st.tabs(["Part 3 (듣고 답하기)", "Part 4 (표 보고 답하기)", "Part 5 (의견 제시 표현)", "Part 5 (15선 모범답안)"])
    
    with tab3:
        st.subheader("💡 Part 3 핵심 치트키")
        df3 = pd.DataFrame(part3_data, columns=["English", "Korean"])
        st.dataframe(df3, use_container_width=True, hide_index=True)
        
    with tab4:
        st.subheader("💡 Part 4 핵심 치트키")
        df4 = pd.DataFrame(part4_data, columns=["English", "Korean"])
        st.dataframe(df4, use_container_width=True, hide_index=True)
        
    with tab5_expr:
        st.subheader("💡 Part 5 의견 제시 만능 표현")
        df5 = pd.DataFrame(part5_expr_data, columns=["English", "Korean"])
        st.dataframe(df5, use_container_width=True, hide_index=True)
        
    with tab5_qa:
        st.subheader("🔥 Part 5 실전 예상문제 15선 완벽 분석")
        for qa in part5_qa_data:
            with st.expander(f"📝 NO.{qa['no']} - {qa['title']}"):
                st.markdown(f"**Q. {qa['q_en']}**")
                st.caption(f"해석: {qa['q_ko']}")
                st.divider()
                
                for ans in qa['answers']:
                    st.markdown(f"### ✅ {ans['type']}")
                    st.info(ans['en'])
                    st.write(f"**한글 해석:** {ans['ko']}")
                    st.markdown(f"🔑 **핵심 표현:** `{ans['keys']}`")
                    st.write("---")

# ------------------------------------------
# 메뉴 2: 실전 모의고사 (타이머 기능)
# ------------------------------------------
elif menu == "⏱️ 실전 모의고사":
    st.header("⏱️ 실전 모의고사 (Part 5)")
    
    # 문제 선택
    q_titles = [f"NO.{q['no']} {q['title']}" for q in part5_qa_data]
    selected_title = st.selectbox("연습할 문제를 선택하세요:", q_titles)
    
    # 선택된 문제 데이터 찾기
    selected_idx = int(selected_title.split("NO.")[1].split(" ")[0]) - 1
    current_q = part5_qa_data[selected_idx]
    
    st.markdown("### 🗣️ Question")
    st.error(f"**{current_q['q_en']}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1️⃣ 준비 시간 (Preparation)")
        if st.button("준비 시작 (45초)", use_container_width=True):
            prep_bar = st.progress(0)
            prep_text = st.empty()
            for i in range(45, -1, -1):
                prep_bar.progress((45 - i) / 45)
                prep_text.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>{i} 초</h2>", unsafe_allow_html=True)
                time.sleep(1)
            st.success("준비 시간 종료! 삐- 소리와 함께 답변을 시작하세요.")
            
    with col2:
        st.subheader("2️⃣ 답변 시간 (Speaking)")
        if st.button("답변 녹음 시작 (60초)", use_container_width=True):
            speak_bar = st.progress(0)
            speak_text = st.empty()
            st.toast("🔴 녹음이 시작되었습니다.")
            for i in range(60, -1, -1):
                speak_bar.progress((60 - i) / 60)
                speak_text.markdown(f"<h2 style='text-align: center; color: #1f77b4;'>{i} 초</h2>", unsafe_allow_html=True)
                time.sleep(1)
            st.success("답변이 완료되었습니다! 'AI 첨삭 노트' 탭에서 결과를 확인하세요.")

# ------------------------------------------
# 메뉴 3: AI 첨삭 노트 (로직 시뮬레이션)
# ------------------------------------------
elif menu == "📝 AI 첨삭 노트":
    st.header("📝 AI 피드백 및 점수 판독")
    st.write("실전 모의고사에서 녹음된 답변을 AI가 분석한 결과입니다. (시뮬레이션)")
    
    # 가상의 STT 결과 (사용자가 Q1을 풀었다고 가정)
    st.subheader("🎙️ 인식된 답변 (STT)")
    user_answer = "I agree that young students should not use AI programs. That's because AI programs provide incorrect information, so students get confused. When I was a university student, I used ChatGPT. But I relied on AI too much. So I didn't get good grades."
    st.text_area("Your Answer:", user_answer, height=150)
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="예상 레벨", value="AL (Advanced Low)", delta="목표 달성!")
        st.metric(label="발음/억양 점수", value="High", delta="명확함")
        
    with col2:
        st.subheader("🔍 AI 교정 및 피드백")
        st.markdown("""
        - **문법 교정:** 완벽합니다! 시제(과거형 `used`, `relied`, `didn't get`)를 아주 잘 사용하셨습니다.
        - **논리성:** 주장 -> 이유 -> 경험 -> 결과의 구조가 매우 논리적입니다.
        - **💡 AI 추천 추가 문장:** 결론을 한 번 더 강조해주면 완벽합니다.
          > *"As a result, I didn't get good grades. **Therefore, I strongly believe AI should not be allowed for homework.**"*
        """)
        
    st.subheader("🎯 사용된 핵심 키워드 매칭율")
    st.progress(0.8, text="제공된 모범 답안의 키워드 중 80%를 사용하셨습니다! (provide incorrect information, get confused, relied on, get good grades)")
