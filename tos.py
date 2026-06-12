import streamlit as st
import pandas as pd
import time

# ==========================================
# 0. 페이지 설정 및 폰트/디자인 (서울남산체 & 글자 크기 확대)
# ==========================================
st.set_page_config(page_title="TOS-Master AI", page_icon="🎯", layout="wide")

# CSS를 통한 서울남산체 폰트 적용 및 전체 글자 크기 확대
st.markdown("""
    <style>
    @font-face {
        font-family: 'SeoulNamsanM';
        src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/SeoulNamsanM.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }
    
    html, body, [class*="css"] {
        font-family: 'SeoulNamsanM', sans-serif !important;
        font-size: 18px !important; /* 기본 글자 크기 확대 */
    }
    
    h1 { font-size: 40px !important; font-weight: bold !important; }
    h2 { font-size: 32px !important; font-weight: bold !important; }
    h3 { font-size: 26px !important; font-weight: bold !important; }
    p, li, span, div { font-size: 18px !important; line-height: 1.6 !important; }
    
    /* 데이터프레임(표) 글자 크기 확대 */
    .dataframe { font-size: 18px !important; }
    
    /* 팁 박스 스타일 */
    .stAlert { font-size: 18px !important; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 1. 데이터 세팅 (제공해주신 모든 데이터 100% 반영)
# ==========================================

# [Part 3 데이터 전체]
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
    ["I don’t want to waste too much money on that", "저는 그것에 돈을 너무 많이 낭비하고 싶지 않아요"],
    ["I don’t want to waste time on that", "저는 그것에 시간을 낭비하고 싶지 않아요"],
    ["It’s waste of money/time", "그건 돈/시간 낭비예요"],
    ["It’s necessary for me", "그것은 저에게 꼭 필요해요"],
    ["I frequently use it", "저는 그것을 자주 이용해요"],
    ["It makes me happy and I can have a great experience", "그것은 저를 행복하게 해주고 저는 좋은 경험을 할 수 있어요"],
    ["They provide a good environment and a pleasant experience", "그들은 좋은 환경과 즐거운 경험을 제공해요"],
    ["I like to try new things", "저는 새로운 것들을 도전해 보는 것을 좋아해요"],
    ["It’s reliable So I can trust the product", "그것은 믿을 만해서 저는 그 제품을 신뢰할 수 있어요"],
    ["It’s a popular item, so people will love it", "그것은 인기 있는 것이며 사람들이 좋아할 거예요"],
    ["It has sentimental value", "그것은 정서적인 가치가 담겨 있어요"],
    ["It’s a good gift", "그것은 좋은 선물이예요"],
    ["It’s a part of my routine", "그것은 제 일상의 일부예요"],
    ["It’s my habit", "그것은 제 습관이에요"],
    ["I really liked it", "저는 그것이 정말 좋았어요"],
    ["It was great", "그것은 훌륭했어요"],
    ["It was awesome", "그것은 근사했어요"],
    ["It’s cheaper and faster", "그것은 더 싸고 더 빨라요"],
    ["It’s very convenient and useful", "그것은 매우 편리하고 유용해요"],
    ["It’s very helpful to me", "그것은 저에게 매우 도움이 돼요"],
    ["It’s my favorite thing to do", "그것은 제가 가장 좋아하는 일이에요"],
    ["It makes me happy, So I can forget about my worries", "그것은 저를 행복하게 해줘서 저는 걱정을 잊을 수 있어요"],
    ["It’s more fun and entertaining so I don’t get bored", "그것은 더 재미있고 즐거움을 줘서 저는 지루해지지 않아요"],
    ["I think It’s more fun to do things in a group", "저는 여럿이 함께하는 것이 더 재미있다고 생각해요"],
    ["I can meet new people and make friends", "저는 새로운 사람들을 만날 수 있고 친구들을 사귈 수 있어요"],
    ["I feel more comfortable and I can focus better", "저는 더 편안함을 느끼고 더 잘 집중할 수 있어요"],
    ["I don’t have to waste time waiting for others", "저는 다른 사람들을 기다리느라 시간을 낭비할 필요가 없어요"],
    ["I feel more comfortable at home", "저는 집에서 더 편안함을 느껴요"],
    ["I can save time because I don’t have to waste time going out", "외출하느라 시간을 낭비할 필요가 없기 때문에 저는 시간을 절약할 수 있어요"],
    ["It’s more personal and builds a closer relationship", "그것은 더 개인적이고 더 밀접한 관계를 쌓을 수 있어요"],
    ["It causes less misunderstanding", "그것은 오해를 덜 불러일으켜요"]
]

# [Part 4 데이터 전체]
part4_data = [
    ["The conference will be held on June 20th at Hilton Hotel", "회의가 6월 20일에 힐튼 호텔에서 개최될 예정이에요"],
    ["The meeting will start at 9:00 a.m", "미팅은 오전 9시에 시작할 거예요"],
    ["The seminar will finish at 5:00 p.m", "세미나는 오후 5시에 끝날 거예요"],
    ["No I’m afraid that you have the wrong information. Actually the registration and coffee session will start at 9:00 am", "아니요 유감스럽지만 잘못 알고 계십니다. 사실은 등록 및 커피타임은 오전 9시에 시작할 거예요"],
    ["There are two session. First, at 1 pm. There is a workshop on Social Media Marketing by Ray Kingston. Next at 2:30 pm, there is a discussion on Appealing to Sports Fans through Marketing by Kevin Delmont", "두 개의 세션이 있어요. 먼저 오후 1시에는 레이 킹스턴의 “소설 미디어 마케팅”에 관한 워크숍이 있어요. 다음으로 오후 2시 30분에는 “마케팅을 통해 스포츠 팬들에게 어필하기”에 대한 케빈 델몬트의 토론이 있어요"],
    ["You will depart from San Francisco at 10 a.m", "당신은 오전 10시에 샌프란시스코에서 출발할 거예요"],
    ["You will arrive in Los Angeles at 3 p.m", "당신은 오후 3시에 로스엔젤레스에 도착할 거예요"],
    ["You will take Korean Air 105", "당신은 대한항공 105기를 탈 거예요"],
    ["You will stay at Glen Hotel", "당신은 글렌 호텔에 머무를 거예요"],
    ["You will have lunch/dinner/a meeting", "당신은 점심식사/저녁식사/회의를 할 거예요"],
    ["You will give a speech/a presentation/a lecture", "당신은 연설/프레젠테이션/강의를 할 거예요"],
    ["There was supposed to be an interview but it has been canceled", "인터뷰가 예정되어 있었으나 취소되었어요"],
    ["There was supposed to be a meeting but it has been postponed", "미팅이 예정되어 있었으나 연기되었어요"],
    ["There was supposed to be a meeting with Jane White at 2 p.m on Tuesday, but it has been rescheduled to Friday", "화요일 오후 2시에 제인 화이트씨와 미팅이 예정되어 있었으나 금요일로 조정되었어요"],
    ["She got a master’s degree in Design from Vancouver Art University in 2020", "그녀는 2020년에 벤쿠버 예술 대학교에서 디자인 전공으로 석사 학위를 취득했어요"],
    ["From 2015 to 2017, she worked at Jasper Fashion Magazine as a director", "2015년부터 2017년까지 그녀는 제스퍼 패션 잡지사에서 이사로 일했어요"],
    ["From 2017 up to now, she has worked at Toronto Fashion Magazine as a chief editor", "2017년부터 지금까지 그녀는 토론토 패션 잡지사에서 편집장으로 일해오고 있어요"],
    ["I think she is qualified because ~", "저는 그녀가 자격을 갖췄다고 생각해요. 왜냐하면 ~"],
    ["He is fluent in Spanish", "그는 스페인어를 유창하게 구사해요"],
    ["She is certified in Pilates", "그녀는 필라테스 자격증이 있어요"],
    ["He has experience in education", "그는 교육 분야에 경험이 있어요"],
    ["You will interview Jessica Anderson at 9:00 a.m", "당신은 제시카 앤더슨과 오전 9시에 면접을 볼 거예요"],
    ["There is an interview with John White from Eco Electronics who is applying for the marketing director position.", "마케팅 부장직에 지원하는 에코전자의 존 화이트씨와 면접이 있어요"],
    ["She has 5 years of experience", "그녀는 5년의 업무경력이 있어요"],
    ["He is applying for the editor position", "그는 편집자 직책에 지원하고 있어요"],
    ["You have to pay 20 dollars for the oil painting class", "오일 페인팅 수업으로 20달러를 지불하셔야 해요"],
    ["It’s 20 dollars", "그것은 20달러에요"],
    ["You should register by January 3rd", "1월 3일까지 등록하셔야 해요"],
    ["If you are a member, It’s 20 dollars", "당신이 회원이라면 20달러에요"],
    ["It’s free", "그것은 무료에요"],
    ["It’s for members", "그것은 회원들을 위한 것이에요"],
    ["There is a Cooking for Beginners class", "초보자를 위한 요리 수업이 있어요"],
    ["Sean Kim will teach the Painting Class", "션 킴 강사가 회화 수업을 지도할 거예요"],
    ["There is a class on French art History", "프랑스 예술사에 관한 수업이 있어요"],
    ["Jennifer Huston will teach a class on computer skills", "제니퍼 휴스턴 강사가 컴퓨터 기술에 관한 수업을 지도할 예정이에요"],
    ["The novel was written by George Orwell", "그 소설은 조지 오웰이 쓴 것입니다."],
    ["The movie was directed by Christopher Nolan", "그 영화는 크리스토퍼 놀란 감독이 연출한 것입니다."],
    ["The report is titled Global Supply Chains New Strategies.", "그 리포트의 제목은 글로벌 공급망 새로운 전략입니다."],
    ["The concert will be performed at the New York Theater", "그 콘서트는 뉴욕 극장에서 공연될 예정입니다."],
    ["The movie will be shown at the Grand Theater", "그 영화는 그랜드 극장에서 상영될 예정입니다."],
    ["The article will be published in September", "그 기사는 9월에 발간될 예정입니다."],
    ["The new smartphone will be released on July 15th", "신형 스마트폰은 7월 15일에 출시될 예정입니다."],
    ["The film will be released in December", "그 영화는 12월에 개봉될 예정입니다."]
]

# [Part 5 핵심 표현 데이터 전체]
part5_expr_data = [
    ["I agree/disagree with the statement", "저는 이 주장에 찬성합니다 / 반대합니다"],
    ["There are some advantages / disadvantages of [명사]", "[명사]의 장점 / 단점이 몇 가지 있습니다."],
    ["I think [명사] is the most important", "저는 [명사]가 가장 중요하다고 생각합니다."],
    ["I think that 주어 + 동사 / I don’t think that 주어 + 동사", "저는 ~라고 생각합니다. 저는 ~라고 생각하지 않습니다."],
    ["I prefer A to B / I prefer A rather than B", "저는 B보다 A를 선호합니다."],
    ["Let me explain why I think so", "제가 그렇게 생각하는 이유를 설명해볼게요"],
    ["Most of all, 주어 + 동사", "무엇보다도 ~ 입니다."],
    ["From my experience, 주어 + 동사", "제 경험에 따르면 ~ 입니다."],
    ["Also, 주어 + 동사", "또한, ~ 입니다."],
    ["According to a recent news report, the majority of 사람들 in Korea said that 주어 + 동사", "최근 뉴스 보도에 따르면 한국 사람들 대다수가 ~라고 말했습니다."],
    ["Therefore, 서론 문장 반복", "그러므로 ~ 입니다."],
    ["They can learn new things", "그들은 새로운 것들을 배울 수 있어요"],
    ["They can meet new people and expand their network", "그들은 새로운 사람들을 만나고 인맥을 넓힐 수 있어요"],
    ["They can have a lot of new experiences and broaden their perspective", "그들은 많은 새로운 것을 경험하고 그들의 견문을 넓힐 수 있어요"],
    ["They can’t make good decisions because they are not mature enough", "그들은 올바른 결정을 하지 못하는데 왜냐하면 그들은 아직 충분히 성숙하지 못하기 때문이에요"],
    ["They will be distracted", "그들은 집중력이 분산될 거예요"],
    ["They can’t focus on their studies/work", "그들은 공부/일에 집중할 수가 없어요"],
    ["They can’t get good grades at school", "그들은 학교에서 좋은 성적을 받을 수 없어요"],
    ["They will fall behind in class", "그들은 학급에서 뒤처질 거예요"],
    ["They can’t work efficiently", "그들은 효율적으로 일할 수 없어요"],
    ["They can save money", "그들은 돈을 절약할 수 있어요"],
    ["The cost of living is too high", "생활비가 너무 비싸요"],
    ["They can’t make a living", "그들은 생계를 유지할 수 없어요"],
    ["I can get a higher salary", "저는 더 높은 급여를 받을 수 있어요"],
    ["That’s a good investment because it makes lives better", "그것은 삶을 더 낫게 만들어주기 때문에 좋은 투자에요"],
    ["They can focus better", "그들은 더 잘 집중할 수 있어요"],
    ["They will not be distracted by others", "그들은 다른 사람들 때문에 방해받지 않을 거예요"],
    ["They can set their own schedule", "그들은 그들만의 일정을 짤 수 있어요"],
    ["They can have more freedom", "그들은 더 많은 자유를 가질 수 있어요"],
    ["They can get information and share it with other people", "그들은 정보를 얻고 그것들은 다른 사람들과 공유할 수 있어요"],
    ["It feels more like a family", "그것은 더 가족처럼 느껴져요"],
    ["They can get a lot of useful information / the latest information on the internet", "그들은 인터넷상에서 많은 유용한 정보 / 최신정보를 얻을 수 있어요"],
    ["It’s faster and more convenient", "그것은 더 빠르고 더 편리해요"],
    ["There is a lot of inaccurate information on the internet, so it’s not reliable", "인터넷에는 많은 부정확한 정보가 있어서 믿을 만하지가 않아요"],
    ["It is very distracting for students, so students can’t focus on their studies/work", "그것은 학생들의 집중을 분산시켜서 학생들은 공부/일에 집중할 수 없어요"],
    ["I can get responses right away", "저는 즉시 답변을 받을 수 있어요"],
    ["I can understand the speaker’s feeling more accurately", "저는 화자의 감정을 더 정확하게 이해할 수 있어요"],
    ["They can create a friendly (work) atmosphere", "그들은 친근한 업무 분위기를 만들 수 있어요"],
    ["They can communicate with others better", "그들은 다른 사람들과 더 잘 소통할 수 있어요"],
    ["They can be good team players and make good relationships with others", "그들은 훌륭한 팀원이 될 수 있고 다른 사람들과 좋은 관계를 맺을 수 있어요"],
    ["They can have a good reputation", "그들은 좋은 평판을 받을 수 있어요"],
    ["They can be very influential", "그들은 매우 영향력이 있을 수 있어요"],
    ["They can motivate others", "그들은 다른 사람들을 동기부여 할 수 있어요"],
    ["Everything is always changing and there is a lot of competition", "모든 것이 항상 변화하고 경쟁이 치열해요"],
    ["They face a lot of challenges and difficulties", "그들은 많은 도전과 어려움에 직면해요"],
    ["He is able to handle a variety of situations due to his confidence", "그는 그의 자신감 덕분에 다양한 상황을 처리할 수 있어요"],
    ["They have a lot of experience / knowledge", "그들은 많은 경험 / 지식을 가지고 있어요"],
    ["Employees can work more efficiently and productively", "직원들은 더 효율적이고 더 생산적으로 일할 수 있어요"],
    ["Employees can be more satisfied with their jobs", "직원들은 그들의 직업에 더 만족할 수 있어요"],
    ["It can make a better work environment", "그것은 더 나은 업무 환경을 만들 수 있어요"],
    ["They might appear less professional", "그들은 덜 전문적으로 보일 수 있어요"],
    ["Customers will feel satisfied and remain loyal", "고객들은 만족감을 느낄 것이고 계속 충성할 거예요"],
    ["It will attract more customers", "그것은 더 많은 고객을 유치할 거예요"],
    ["The business will be more successful", "그 사업은 더 성공할 거예요"],
    ["People frequently use social media, so it will be very effective", "사람들은 소셜미디어를 자주 이용해서 그것은 매우 효과적일 거예요"],
    ["It relieves their stress and they can relax", "그것은 그들의 스트레스를 풀어주고 그들은 편히 쉴 수 있어요"],
    ["It is good for their physical / metal health", "그것은 그들의 신체적 / 정신적 건강에 좋아요"],
    ["It is not good for their health", "그것은 그들의 건강에 좋지 않아요"],
    ["It can develop healthy habits", "그것은 건강한 습관들을 기를 수 있어요"],
    ["It can develop unhealthy habits", "그것은 건강하지 않은 습관들을 기를 수 있어요"],
    ["It is good for the environment", "그것은 환경에 좋아요"],
    ["Pollution is a serious issue these days", "환경오염은 요즘 심각한 문제예요"],
    ["It can make a cleaner environment", "그것은 더 깨끗한 환경을 만들 수 있어요"],
    ["We will be able to protect the environment", "우리는 환경을 보호할 수 있을 거예요"]
]

# [Part 5 15선 모범답안 데이터 전체 (1~15번 100% 반영)]
part5_qa_data = [
    {
        "no": 1, "title": "AI 프로그램 사용 금지",
        "q_en": "Do you agree or disagree with the following statement?\nYoung students should not be allowed to use AI programs for their homework.",
        "q_ko": "어린 학생들이 숙제를 할 때 AI 프로그램(인공지능)을 사용하는 것을 허용해서는 안 된다.",
        "answers": [
            {"type": "Answer 1", "en": "I agree that young students should not be allowed to use AI programs for their homework.\n\nThat's because AI programs can sometimes provide incorrect information, so students may get confused.\n\nFrom my experience, when I was a university student, I used AI programs such as ChatGPT for my assignments. However, they sometimes gave me inaccurate information, and I didn't notice it. Moreover, I relied on AI too much. As a result, I didn't get good grades.", "ko": "저는 어린 학생들이 숙제를 할 때 AI 프로그램을 사용하는 것이 허용되지 않아야 한다고 생각합니다. 왜냐하면 AI 프로그램은 때때로 잘못된 정보를 제공할 수 있어서 학생들이 혼란을 겪을 수 있기 때문입니다. 제 경험을 말씀드리면, 저는 대학생 때 과제를 하면서 ChatGPT와 같은 AI 프로그램을 사용했습니다. 하지만 때때로 부정확한 정보를 제공했는데도 저는 그것을 알아차리지 못했습니다. 또한 저는 AI에 너무 의존했습니다. 그 결과, 좋은 성적을 받지 못했습니다.", "keys": "provide incorrect information / get confused / assignments / relied on / get good grades"},
            {"type": "Answer 2", "en": "I agree that young students should not be allowed to use AI programs for their homework.\n\nThat's because students are likely to use AI programs too much. So, it is not helpful to develop their thinking skills.\n\nWhen I was a high school student, I used AI programs to do my math homework. They were very convenient and useful because I didn't have to think to solve math problems. As a result, I was not able to answer the questions on my own and always got poor grades in math.", "ko": "저는 어린 학생들이 숙제를 위해 AI 프로그램을 사용하는 것이 허용되어서는 안 된다고 생각합니다. 왜냐하면 학생들은 AI 프로그램을 지나치게 많이 사용할 가능성이 있습니다. 그래서 그것은 학생들의 사고 능력을 기르는 데 도움이 되지 않기 때문입니다. 제가 고등학생이었을 때, 저는 수학 숙제를 하기 위해 AI 프로그램을 사용했습니다. 그것들은 매우 편리하고 유용했는데, 수학 문제를 풀기 위해 직접 생각할 필요가 없었기 때문입니다. 그 결과, 저는 스스로 문제에 답하지 못했고, 수학에서 항상 낮은 점수를 받았습니다.", "keys": "are likely to / do my math homework / solve math problems / on my own / got poor grades in math"}
        ]
    },
    {
        "no": 2, "title": "회사 웹사이트 방문의 유용성",
        "q_en": "Do you agree or disagree with the following statement?\nIt is very useful to visit a company's website to get information about a product before you purchase it.",
        "q_ko": "제품을 구매하기 전에 회사의 웹사이트를 방문해서 정보를 얻는 것은 매우 유용합니다.",
        "answers": [
            {"type": "Answer 1 (동의)", "en": "I agree that it is very useful to visit a company's website to get information about a product before I purchase it.\n\nThat's because we can get accurate information about products.\n\nLast week, I went to a convenience store to buy some chocolate. I usually check nutrition information before buying chocolate, but the information on the package was too small to read. So, I visited the company's website to check the detailed nutrition information. As a result, I was able to find accurate information.", "ko": "저는 제품을 구매하기 전에 회사 웹사이트를 방문해 정보를 얻는 것이 매우 유용하다고 생각합니다. 왜냐하면 우리는 제품에 대한 정확한 정보를 얻을 수 있기 때문입니다. 지난주에 저는 초콜릿을 사기 위해 편의점에 갔습니다. 저는 보통 초콜릿을 사기 전에 영양 정보를 확인하는데, 포장에 있는 정보가 너무 작아서 읽기 어려웠습니다. 그래서 자세한 영양 정보를 확인하기 위해 회사 웹사이트를 방문했습니다. 그 결과, 정확한 정보를 찾을 수 있었습니다.", "keys": "get accurate information / to buy some chocolate / before buying chocolate / too small to read / detailed"},
            {"type": "Answer 2 (반대)", "en": "I disagree that it is very useful to visit a company's website to get information about a product before I purchase it.\n\nThat's because it is difficult to check the disadvantages of a product.\n\nIn my case, I tried to buy a tablet computer online. However, I could find only the advantages of the product on the company's website. So, I visited other websites for customer reviews and I found some disadvantages of it. As a result, I did not purchase the tablet PC and saved money.", "ko": "저는 제품을 구매하기 전에 회사 웹사이트를 방문해 정보를 얻는 것이 매우 유용하다는 주장에 동의하지 않습니다. 왜냐하면 제품의 단점을 찾기 어렵기 때문입니다. 제 경우에는 태블릿을 온라인으로 구매하려고 했습니다. 하지만 회사 웹사이트에서는 제품의 장점만 찾을 수 있었습니다. 그래서 저는 고객 후기를 보기 위해 다른 웹사이트를 방문했고, 그 제품의 단점을 발견했습니다. 그 결과, 저는 태블릿을 구매하지 않았고 돈을 절약할 수 있었습니다.", "keys": "the disadvantages of a product / online / on the company's website / customer reviews / saved money"}
        ]
    },
    {
        "no": 3, "title": "노트북 교체 주기",
        "q_en": "Some people prefer to replace their laptops frequently, while others prefer to use the same laptop for a long period of time. Which do you prefer and why?",
        "q_ko": "어떤 사람들은 자주 노트북을 교체하는 것을 선호하고, 다른 사람들은 오랜 기간 동안 같은 노트북을 사용하는 것을 선호합니다. 당신은 어느 쪽을 선호하십니까? 그 이유는 무엇입니까?",
        "answers": [
            {"type": "Answer 1 (오래 사용)", "en": "I prefer to use the same laptop for a long period of time.\n\nThat's because I think replacing my laptop frequently is a waste of money.\n\nWhen I was a high school student, I replaced my laptop once every two years because I wanted the latest model. However, I realized one day that the performance was not very different, and I wasted too much money. So, nowadays, I try to use my laptop over three years.", "ko": "저는 같은 노트북을 오랫동안 사용하는 것을 선호합니다. 그 이유는 노트북을 자주 바꾸는 것이 돈 낭비라고 생각하기 때문입니다. 제가 고등학생이었을 때, 최신 모델을 갖고 싶어서 2년에 한 번씩 노트북을 교체했습니다. 하지만 어느 날 성능이 크게 다르지 않다는 것을 깨달았고, 돈을 너무 많이 낭비했다는 생각이 들었습니다. 그래서 요즘은 노트북을 3년 이상 사용하려고 노력합니다.", "keys": "a waste of money / When I was a high school student / once every two years / the latest / one day / performance / wasted too much money / over"},
            {"type": "Answer 2 (자주 교체)", "en": "I prefer to replace my laptop frequently.\n\nMost of all, old laptops are likely to break down. So, we have to worry about our computer breaking down while working.\n\nWhen I was a university student, I was doing my assignment on a five-year-old laptop. However, one day, the laptop didn't work properly. As a result, I lost all my data and couldn't submit the assignment by the deadline. And I couldn't get it repaired at the service center.", "ko": "저는 노트북을 자주 교체하는 것을 선호합니다. 무엇보다도, 오래된 노트북은 고장이 날 가능성이 높습니다. 그래서 우리는 일을 하는 도중에 컴퓨터가 고장 날까 봐 걱정해야 합니다. 제가 대학생이었을 때, 저는 5년 된 노트북으로 과제를 하고 있었습니다. 그런데 어느 날 노트북이 제대로 작동하지 않았습니다. 그 결과, 모든 데이터를 잃어버렸고 마감 기한까지 과제를 제출하지 못했습니다. 게다가 서비스 센터에서도 수리를 받을 수 없었습니다.", "keys": "are likely to / break down / a five-year-old laptop / properly / lost all my data / submit the assignment by the deadline / get it repaired"}
        ]
    },
    {
        "no": 4, "title": "전기차 추천 여부",
        "q_en": "Imagine that a friend who lives in your city is planning to buy a car. Would you recommend an electric vehicle to them? Why or why not?",
        "q_ko": "당신이 사는 도시에 거주하는 한 친구가 자동차를 살 계획이라고 가정해 봅시다. 당신은 그 친구에게 전기차를 추천하시겠습니까? 그 이유는 무엇입니까?",
        "answers": [
            {"type": "Answer 1 (반대)", "en": "I would not recommend an electric vehicle to them.\n\nMost of all, we do not have enough EV charging stations in Korea at the moment. If the battery runs low and we cannot find a charging station nearby, we will be in big trouble. So, it is not safe to drive an electric vehicle yet.\n\nA few months ago, there was a big fire at an apartment complex caused by an electric vehicle. The residents are still suffering from the damage. Therefore, I think this is not a good time to buy an electric vehicle.", "ko": "저는 그 친구에게 전기차를 추천하지 않을 것입니다. 무엇보다도, 현재 한국에는 전기차 충전소가 충분하지 않습니다. 배터리가 부족해졌는데 근처에서 충전소를 찾지 못하면 큰 곤란을 겪을 수 있습니다. 그래서 아직 전기차를 운전하기에는 안전하지 않다고 생각합니다. 예를 들어, 몇 달 전 한 아파트 단지에서 전기차로 인해 큰 화재가 발생한 적이 있습니다. 주민들은 아직도 그 피해로 고통을 겪고 있습니다. 따라서 저는 지금이 전기차를 구매하기에 좋은 시기가 아니라고 생각합니다.", "keys": "EV charging stations / runs low / be in big trouble / at an apartment complex / residents / suffering from"},
            {"type": "Answer 2 (찬성)", "en": "I would recommend an electric vehicle to them.\n\nMost of all, we can buy an electric vehicle at a reasonable price. Specifically, we can receive various kinds of financial support from the government.\n\nIn the case of my best friend Ju-mi, she bought an electric car called EV3 about two years ago. She received subsidies from the government and bought the car at a discounted price. Also, she could receive tax benefits. As a result, she could reduce the living expenses and was very satisfied with her choice.", "ko": "저는 그 친구에게 전기차를 추천할 것입니다. 무엇보다도, 우리는 전기차를 합리적인 가격에 구매할 수 있습니다. 특히 정부로부터 다양한 종류의 재정 지원을 받을 수 있습니다. 예를 들어, 제 가장 친한 친구 주미는 약 2년 전에 EV3라는 전기차를 구매했습니다. 그녀는 정부 보조금을 받아 할인된 가격에 차를 구매했습니다. 또한 세금 혜택도 받을 수 있었습니다. 그 결과 생활비를 줄일 수 있었고, 자신의 선택에 매우 만족했습니다.", "keys": "at a reasonable price / various kinds of financial support / subsidies / at a discounted price / receive tax benefits / reduce the living expenses / satisfied"}
        ]
    },
    {
        "no": 5, "title": "부모의 지원 증가",
        "q_en": "Do you agree or disagree with the following statement?\nNowadays, young adults receive more assistance from their parents than in the past.",
        "q_ko": "오늘날의 젊은 성인들은 과거에 비해 부모로부터 더 많은 지원을 받는다.",
        "answers": [
            {"type": "Answer 1", "en": "I agree that nowadays, young adults receive more assistance from their parents than in the past.\n\nMost of all, most families have no more than two children nowadays, so parents can concentrate on their children enough.\n\nIn the past, there were more than four children in a family. So, the parents were not able to pay attention to every child. However, nowadays, there are two children or just one child in most families. So, the parents can support their children's study and so on.", "ko": "저는 요즘 젊은 성인들이 과거보다 부모로부터 더 많은 도움을 받는다고 생각합니다. 무엇보다도, 요즘 대부분의 가정은 두 명 이하의 자녀를 두고 있기 때문에 부모가 자녀에게 충분히 집중할 수 있습니다. 과거에는 많은 가정이 네 명 이상의 자녀를 두었습니다. 그래서 부모들은 모든 아이에게 충분히 관심을 기울이기 어려웠습니다. 하지만 요즘에는 대부분의 가정에서 두 명 또는 한 명의 자녀만 있습니다. 그래서 부모들은 자녀의 공부를 더 많이 지원하고 여러 가지 방법으로 도울 수 있습니다.", "keys": "no more than two children / concentrate on / In the past / pay attention to"},
            {"type": "Answer 2 (만점 답변)", "en": "I agree that nowadays, young adults receive more assistance from their parents than in the past.\n\nMost of all, the number of people who get a job early has been decreasing. So, many of them still live with their parents.\n\nIn the case of my mother, she got a job when she was 23 years old, so she lived alone without her parents' assistance. In contrast, I am 26 years old, but I am still studying to get a job. As a result, I still live with my parents and receive support from them, such as living expenses and tuition.", "ko": "저는 요즘 젊은 성인들이 과거보다 부모로부터 더 많은 도움을 받는다고 생각합니다. 무엇보다도, 일찍 취업하는 사람들의 수가 줄어들고 있습니다. 그래서 많은 사람들이 여전히 부모님과 함께 살고 있습니다. 예를 들어, 제 어머니는 23살에 취직을 하셔서 부모님의 도움 없이 혼자 살았습니다. 반면 저는 26살이지만 아직 취업을 준비하며 공부하고 있습니다. 그 결과 저는 아직 부모님과 함께 살면서 생활비와 등록금 같은 지원을 받고 있습니다.", "keys": "the number of people who get a job early has been decreasing / without her parents' assistance / In contrast / receive support from them / living expenses and tuition"}
        ]
    },
    {
        "no": 6, "title": "대면 미팅의 장점",
        "q_en": "What are the advantages of meeting customers in person rather than holding a video conference?",
        "q_ko": "화상 회의를 개최하는 것보다 고객을 직접 만나서 응대(대면)하는 것의 장점은 무엇입니까?",
        "answers": [
            {"type": "Answer 1", "en": "There are some advantages of meeting customers in person rather than holding a video conference.\n\nMost of all, I can get a response quickly. So, I can understand customers' opinions and make better decisions.\n\nWhen I was a junior at work, our company launched a new laptop called \"gram.\" My goal at work was gathering customer feedback. So, I invited well-known tech influencers and asked for their opinions about the laptop. As a result, I was able to receive various responses about the product quickly.", "ko": "화상 회의를 하는 것보다 고객을 직접 만나는 것에는 몇 가지 장점이 있습니다. 무엇보다도, 빠르게 고객의 반응을 파악할 수 있습니다. 그래서 고객의 의견을 이해하고 더 나은 결정을 내릴 수 있습니다. 예를 들어, 제가 회사에서 주니어 직원이었을 때 우리 회사는 \"그램\"이라는 새로운 노트북을 출시했습니다. 제 업무 목표는 고객의 피드백을 수집하는 것이었습니다. 그래서 저는 유명한 테크 인플루언서들을 초대해 노트북에 대한 의견을 물었습니다. 그 결과, 제품에 대한 다양한 반응을 빠르게 받을 수 있었습니다.", "keys": "get a response quickly / make better decisions / launched a new laptop / asked for their opinions"},
            {"type": "Answer 2", "en": "There are some advantages of meeting customers in person rather than holding a video conference.\n\nMost of all, it is easier to communicate with people who have difficulty using a video conference.\n\nFor example, about six months ago, I worked at a local government office. At that time, a video conference was scheduled with customers, but some of them could not use the video conference application. As a result, they had to come to the office.", "ko": "화상 회의를 하는 것보다 고객을 직접 만나는 것에는 몇 가지 장점이 있습니다. 무엇보다도, 화상 회의를 사용하는 데 어려움이 있는 사람들과 의사소통하기가 더 쉽습니다. 예를 들어, 약 6개월 전 저는 지방 정부 기관에서 일했습니다. 그 당시 고객들과 화상 회의가 예정되어 있었지만, 그들 중 일부는 화상 회의 애플리케이션을 사용할 수 없었습니다. 그 결과 일부 고객은 사무실로 직접 와야 했습니다.", "keys": "have difficulty using a video conference / government office / was scheduled / had to"}
        ]
    },
    {
        "no": 7, "title": "체육 수업 확대",
        "q_en": "Do you think high schools in your area should offer more physical education classes where students can learn sports or get more exercise? Why or why not?",
        "q_ko": "당신이 사는 지역의 고등학교들이 학생들이 스포츠를 배우거나 운동을 더 많이 할 수 있는 체육 수업을 더 많이 제공해야 한다고 생각하십니까? 그 이유는 무엇입니까?",
        "answers": [
            {"type": "Answer 1", "en": "I think high schools in my area should offer more physical education classes.\n\nThat's because students can learn various exercises, so they can find a new hobby while doing them.\n\nWhen I was a high school student, I learned how to play tennis, soccer, golf and so on in physical education class. Among them, my favorite sport was tennis because it is a very active sport. As a result, I have played tennis almost every day since then.", "ko": "저는 우리 지역의 고등학교들이 체육 수업을 더 많이 제공해야 한다고 생각합니다. 왜냐하면 학생들은 다양한 운동을 배울 수 있기 때문에 그 과정에서 새로운 취미를 찾을 수 있습니다. 제가 고등학생이었을 때 체육 수업 시간에 테니스, 축구, 골프 등을 배웠습니다. 그 중에서 제가 가장 좋아했던 운동은 테니스였는데 매우 활동적인 스포츠이기 때문입니다. 그 결과 저는 그 이후로 거의 매일 테니스를 치고 있습니다.", "keys": "while doing them / learned how to play tennis / among them / active / have played tennis / since then"},
            {"type": "Answer 2", "en": "I think high schools in my area should offer more physical education classes.\n\nThat's because it is helpful for students to increase their stamina. So, they can focus on studying for a longer time.\n\nWhen I was a high school student, I was sick often. Others were worried about me because I had poor stamina. However, I could increase my physical strength gradually by playing various sports during physical education classes. As a result, I was able to focus on studying for a longer time and improve my grades.", "ko": "저는 우리 지역의 고등학교들이 체육 수업을 더 많이 제공해야 한다고 생각합니다. 왜냐하면 체육 수업은 학생들의 체력을 기르는 데 도움이 되기 때문입니다. 그래서 학생들은 더 오랫동안 공부에 집중할 수 있습니다. 제가 고등학생이었을 때 저는 자주 아팠습니다. 저의 체력이 좋지 않았기 때문에 다른 사람들은 저를 걱정했습니다. 하지만 체육 수업 시간에 다양한 운동을 하면서 점차 근력을 기를 수 있었습니다. 그 결과 저는 더 오랫동안 공부에 집중할 수 있었고 성적도 향상되었습니다.", "keys": "increase their stamina / for a longer time / I was sick often / were worried about / I had poor stamina / gradually / improve my grades"}
        ]
    },
    {
        "no": 8, "title": "디지털 문서 vs 종이 문서",
        "q_en": "Do you think companies should stop using printed documents and use digital ones instead? Why or why not?",
        "q_ko": "기업들이 종이 문서 사용을 중단하고 그 대신 디지털 문서를 사용해야 한다고 생각하십니까? 그 이유는 무엇입니까?",
        "answers": [
            {"type": "Answer 1", "en": "I think companies should stop using printed documents and use digital ones instead.\n\nThat's because it can help protect the environment.\n\nLast year in my office, many departments wasted a lot of paper. So, our company decided to use digital tools such as tablet PCs and Google Docs. As a result, we were able to save a lot of paper and make our office more eco-friendly.", "ko": "저는 회사들이 인쇄된 문서를 사용하는 것을 중단하고 대신 디지털 문서를 사용해야 한다고 생각합니다. 왜냐하면 이것은 환경을 보호하는 데 도움이 되기 때문입니다. 예를 들어, 작년에 제가 일하던 사무실에서는 많은 부서가 종이를 많이 낭비했습니다. 그래서 우리 회사는 태블릿 PC와 구글 독스 같은 디지털 도구를 사용하기로 결정했습니다. 그 결과 우리는 많은 종이를 절약할 수 있었고 사무실을 더 친환경적으로 만들 수 있었습니다.", "keys": "protect the environment / wasted a lot of paper / digital tools / save a lot of paper / eco-friendly"},
            {"type": "Answer 2", "en": "I think companies should stop using printed documents and use digital ones instead.\n\nThat's because it is easier to manage documents at work, so we can work more efficiently.\n\nAbout six months ago, I worked at a local government office. At that time, I was often asked to find some paper documents for customers. There were a lot of documents, so it was hard to find the right one. As a result, I wasted a lot of time looking for the documents.", "ko": "저는 회사들이 인쇄된 문서를 사용하는 것을 중단하고 대신 디지털 문서를 사용해야 한다고 생각합니다. 왜냐하면 문서를 관리하기가 더 쉬워지기 때문에 우리는 더 효율적으로 일할 수 있습니다. 예를 들어, 약 6개월 전 저는 지방 정부 기관에서 일했습니다. 그 당시 저는 고객들을 위해 종이 문서를 찾아달라는 요청을 자주 받았습니다. 문서가 너무 많아서 원하는 문서를 찾기가 어려웠습니다. 그 결과 저는 문서를 찾는 데 많은 시간을 낭비했습니다.", "keys": "easier to manage / was often asked to / hard to find the right one / looking for the documents"}
        ]
    },
    {
        "no": 9, "title": "비경쟁적 활동만 제공",
        "q_en": "Do you agree or disagree with the following statement?\nSchools should offer only noncompetitive activities for children.",
        "q_ko": "학교는 아이들에게 비경쟁적인 활동만 제공해야 한다.",
        "answers": [
            {"type": "Answer 1", "en": "I disagree that schools should offer only noncompetitive activities for children.\n\nThat's because competition is important for students to learn how to find strategies to win.\n\nWhen I was a middle school student, I was able to learn how to get a better score from many tests. Also, I could learn which subject I was good at. As a result, competition was helpful for me to discover my strengths.", "ko": "저는 학교가 아이들에게 경쟁이 없는 활동만 제공해야 한다는 의견에 동의하지 않습니다. 왜냐하면 경쟁은 학생들이 이기기 위한 전략을 찾는 방법을 배우는 데 중요하기 때문입니다. 제가 중학생이었을 때, 저는 많은 시험을 통해 더 좋은 점수를 얻는 방법을 배울 수 있었습니다. 또한, 제가 어떤 과목을 잘 하는지도 알 수 있었습니다. 결과적으로, 경쟁은 제가 저의 강점을 발견하는 데 도움이 되었습니다.", "keys": "how to find strategies to win / from many tests / which subject I was good at / helpful for me / discover my strengths"},
            {"type": "Answer 2", "en": "I disagree that schools should offer only noncompetitive activities for children.\n\nThat's because competition can help children prepare for the future.\n\nIn Korea, students need to compete to enter prestigious universities. After that, they also need to compete to get better jobs. So, it is important for students to experience competition early. This way, they can learn how to manage stress effectively and not give up.", "ko": "저는 학교가 아이들에게 경쟁이 없는 활동만 제공해야 한다는 주장에 동의하지 않습니다. 왜냐하면 경쟁은 아이들이 미래를 준비하는 데 도움이 될 수 있기 때문입니다. 예를 들어, 한국에서는 학생들이 명문 대학에 입학하기 위해 경쟁해야 합니다. 그 이후에는 더 좋은 직업을 얻기 위해서도 경쟁해야 합니다. 그래서 어릴 때부터 경쟁을 경험하는 것이 학생들에게 중요합니다. 이렇게 하면 스트레스를 관리하는 방법을 배우고 쉽게 포기하지 않게 됩니다.", "keys": "help children prepare for the future / enter prestigious universities / get better jobs / for students / early / manage stress effectively"}
        ]
    },
    {
        "no": 10, "title": "큰 목표 vs 작은 목표",
        "q_en": "Do you agree or disagree with the following statement?\nWhen planning a career, setting one big goal is more effective than having multiple small goals.",
        "q_ko": "진로를 계획할 때, 하나의 큰 목표를 세우는 것이 여러 개의 작은 목표를 세우는 것보다 더 효과적이다.",
        "answers": [
            {"type": "Answer 1 (동의)", "en": "I agree that when planning a career, setting one big goal is more effective than having multiple small goals.\n\nThat's because if we have multiple small goals, we could be stressed more often while trying to achieve them.\n\nIn the case of my best friend, she had multiple small goals after she entered a company. She even studied at a computer academy on weekends to get a certificate. As a result, she was under a lot of stress and often considered quitting her job.", "ko": "저는 진로를 계획할 때 하나의 큰 목표를 세우는 것이 여러 개의 작은 목표를 세우는 것보다 더 효과적이라는 주장에 동의합니다. 왜냐하면 여러 개의 작은 목표가 있으면 그것을 이루려는 과정에서 더 자주 스트레스를 받을 수 있기 때문입니다. 예를 들어, 제 가장 친한 친구는 회사에 들어간 후 여러 개의 작은 목표를 가지고 있었습니다. 그녀는 자격증을 따기 위해 주말에도 컴퓨터 학원에서 공부했습니다. 그 결과 그녀는 많은 스트레스를 받았고 직장을 그만둘지에 대해 자주 고민했습니다.", "keys": "be stressed / achieve them / In the case of my best friend / on weekends / get a certificate / a lot of stress / quitting her job"},
            {"type": "Answer 2 (반대)", "en": "I disagree that when planning a career, setting one big goal is more effective than having multiple small goals.\n\nThat's because it is easier to achieve small goals, and this helps us gain confidence.\n\nWhen I was looking for a job, I wanted to work at a global IT company, but I didn't get the job because I lacked experience. As a result, I lost my self-esteem and motivation. However, I regained my confidence by focusing on small steps, such as improving my resume and interview skills.", "ko": "저는 진로를 계획할 때 하나의 큰 목표를 세우는 것이 여러 개의 작은 목표를 세우는 것보다 더 효과적이라는 주장에 동의하지 않습니다. 왜냐하면, 작은 목표는 달성하기 더 쉽고 우리에게 자신감을 얻는 데 도움을 주기 때문입니다. 제가 취업을 준비하고 있었을 때, 글로벌 IT 회사에서 일하고 싶었습니다. 하지만 경험이 부족해서 그 회사에 취직하지 못했습니다. 그 결과 저는 자존감과 동기를 잃었습니다. 그러나 이력서와 면접 능력을 향상시키는 것과 같은 작은 단계에 집중하면서 다시 자신감을 되찾을 수 있었습니다.", "keys": "helps us gain confidence / When I was looking for a job / lacked experience / self-esteem and motivation / regained / focusing on small steps"}
        ]
    },
    {
        "no": 11, "title": "CEO의 의사결정 방식",
        "q_en": "Do you agree or disagree with the following statement?\nA company's CEO should discuss important decisions with as many employees as possible before making them.",
        "q_ko": "회사의 CEO는 중요한 결정을 하기 전에 가능한 많은 직원들과 그에 대해 논의해야 한다.",
        "answers": [
            {"type": "Answer 1 (반대)", "en": "I disagree with the following statement.\n\nThat's because it can prevent them from making quick decisions. So, they might miss important opportunities.\n\nWhen I was a new employee, our company had a good business opportunity with an American company. However, it was a little risky. So, our CEO had a lot of meetings with employees every day because he couldn't make a decision quickly. As a result, the American company decided to work with another company.", "ko": "저는 다음 주장에 동의하지 않습니다. 왜냐하면 그것은 빠른 결정을 내리는 것을 방해할 수 있기 때문입니다. 그래서 중요한 기회를 놓칠 수도 있습니다. 제가 신입사원이었을 때 우리 회사는 미국 회사와 좋은 사업 기회가 있었습니다. 하지만 그 일에는 약간의 위험이 있었습니다. 그래서 우리 CEO는 결정을 빨리 내리지 못해 매일 직원들과 많은 회의를 했습니다. 그 결과, 그 미국 회사는 다른 회사와 일하기로 결정했습니다.", "keys": "prevent / making quick decisions / miss important opportunities / risky / make a decision quickly / decided to work with"},
            {"type": "Answer 2 (찬성)", "en": "I agree with the following statement.\n\nThat's because it can give CEOs a lot of different perspectives. So, they can make effective decisions.\n\nAbout six months ago, I worked at a math academy, and my CEO was planning to change the textbooks for all classes. He discussed its pros and cons with many employees, including college interns. As a result, he was able to get many creative ideas and choose the most suitable textbook for students.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 이는 CEO들에게 각기 다른 관점을 제공할 수 있기 때문입니다. 그래서 그들은 더 효과적인 결정을 내리게 됩니다. 약 6개월 전에 저는 수학 학원에서 일했습니다. 그때 원장은 모든 수업의 교재를 바꾸려고 계획하고 있었습니다. 그는 대학생 인턴을 포함한 많은 직원들과 교재의 장단점에 대해 논의했습니다. 그 결과 그는 많은 창의적인 아이디어를 얻을 수 있었고 학생들에게 가장 적합한 교재를 선택할 수 있었습니다.", "keys": "different perspectives / make effective decisions / change the textbooks / pros and cons / including college interns / creative ideas / the most suitable textbook"}
        ]
    },
    {
        "no": 12, "title": "환경 교육 포함",
        "q_en": "Do you agree or disagree with the following statement?\nSchools should include environmental education in the curriculum for young children.",
        "q_ko": "학교는 어린 아이들을 위한 교육 과정에 환경 교육을 포함시켜야 한다.",
        "answers": [
            {"type": "Answer 1", "en": "I agree with the following statement.\n\nThat's because young children can learn the importance of protecting the environment through environmental education.\n\nWhen I was an elementary school student, I watched an educational documentary at school. At that time, I saw many animals suffering from plastic waste. As a result, I have reduced the use of plastic products.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 어린 아이들은 환경 교육을 통해 환경을 보호하는 것의 중요성을 배울 수 있기 때문입니다. 예를 들어, 제가 초등학생이었을 때 학교에서 교육용 다큐멘터리를 본 적이 있습니다. 그때 저는 플라스틱 쓰레기로 인해 많은 동물들이 고통받는 모습을 보았습니다. 그 결과 저는 플라스틱 제품 사용을 줄이게 되었습니다.", "keys": "through environmental education / educational documentary / suffering from / have reduced"},
            {"type": "Answer 2", "en": "I agree with the following statement.\n\nThat's because the environment is a serious problem in Korea. So, Koreans consider the environment important.\n\nWhen I was an elementary school student, our school included an environmental education class in the curriculum once a week. We watched videos about recycling and made recycling campaign videos ourselves. Also, we practiced recycling during the class. As a result, students became more interested in environmental problems.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 환경은 한국에서 심각한 문제이기 때문입니다. 그래서 한국 사람들은 환경을 중요하게 생각합니다. 예를 들어, 제가 초등학생이었을 때 우리 학교에서는 일주일에 한 번 환경 교육 수업이 있었습니다. 우리는 재활용에 관한 영상을 보고 재활용 캠페인 영상을 직접 만들었습니다. 또한 우리는 수업 시간에 재활용하는 방법을 연습했습니다. 그 결과 학생들은 환경 문제에 더 많은 관심을 가지게 되었습니다.", "keys": "a serious problem / consider / in the curriculum / watched videos about recycling / ourselves / practiced / became more interested in"}
        ]
    },
    {
        "no": 13, "title": "아침 vs 오후 업무",
        "q_en": "Do you agree or disagree with the following statement?\nIt is more effective to complete important work in the morning than in the afternoon.",
        "q_ko": "오후보다는 아침에 중요한 일을 끝내는 것이 더 효율적이다.",
        "answers": [
            {"type": "Answer 1", "en": "I agree with the following statement.\n\nThat's because we can get feedback on the work from co-workers.\n\nWhen I worked at a marketing company, I usually did essential tasks in the morning. So, my co-workers could find mistakes in my work in the afternoon. As a result, I was able to correct them in time.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 우리는 동료들로부터 우리의 일에 대한 피드백을 받을 수 있기 때문입니다. 예를 들어, 제가 직장인이었을 때 저는 보통 아침에 가장 필수적인 업무를 했습니다. 그래서 동료들이 오후에 제 업무에서 실수를 발견할 수 있었습니다. 그 결과 저는 그것들을 제때 수정할 수 있었습니다.", "keys": "get feedback on / from co-workers / essential / find mistakes in / correct them in time"},
            {"type": "Answer 2", "en": "I agree with the following statement.\n\nThat's because many people can concentrate on work more efficiently in the morning.\n\nFor example, when I was a student, I often studied late at night. However, I was very tired and could not concentrate well. So, I made a lot of mistakes in my assignments. After that, I started studying in the morning. As a result, I was able to focus better and finish my work more efficiently.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 많은 사람들이 아침에 더 효율적으로 일에 집중할 수 있기 때문입니다. 예를 들어, 제가 학생이었을 때 저는 종종 밤늦게 공부했습니다. 하지만 매우 피곤해서 집중을 잘 할 수 없었습니다. 그래서 과제에서 많은 실수를 했습니다. 그 이후로 저는 아침에 공부하기 시작했습니다. 그 결과 더 잘 집중할 수 있었고 일을 더 효율적으로 끝낼 수 있었습니다.", "keys": "efficiently / late at night / could not concentrate well / made a lot of mistakes / focus better"}
        ]
    },
    {
        "no": 14, "title": "대학 입학 전 1년 근무",
        "q_en": "Do you agree or disagree with the following statement?\nStudents who complete their secondary education should consider working for a year before entering university.",
        "q_ko": "중·고등학교 교육을 마친 학생들은 대학교에 입학하기 전에 1년간 일해보는 것을 고려해야 한다.",
        "answers": [
            {"type": "Answer 1", "en": "I agree with the following statement.\n\nThat's because it is really helpful to choose a career path in the future.\n\nFor example, when I graduated from high school, I just chose my major and university based on my grades. So, I couldn't adapt well for the first two years, and I regretted my decision. As a result, I changed my major to shipbuilding in my third year.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 미래의 진로 방향을 선택하는 것에 매우 도움이 되기 때문입니다. 예를 들어, 제가 고등학교를 졸업했을 때 저는 성적을 기준으로 전공과 대학을 선택했습니다. 그래서 처음 2년 동안 잘 적응하지 못했고 그 결정을 후회했습니다. 그래서 3학년 때 전공을 조선공학으로 바꾸었습니다.", "keys": "choose a career path / based on my grades / couldn't adapt well / regretted my decision / in my third year"},
            {"type": "Answer 2", "en": "I agree with the following statement.\n\nThat's because it is helpful for them to choose their career path. So, they can save time planning for their future.\n\nWhen I was 20 years old, I didn't know my interests. So, I majored in Korean without a clear reason. So, I spent about two years trying to find my aptitude. As a result, I got a job later than others.", "ko": "저는 다음 주장에 동의합니다. 왜냐하면 진로 방향을 선택하는 것에 도움이 되기 때문입니다. 그래서 미래를 계획하는 데 시간을 절약할 수 있습니다. 제가 20살이었을 때 저는 제 관심사가 무엇인지 몰랐습니다. 그래서 뚜렷한 이유 없이 한국어를 전공하게 되었습니다. 그 결과 제 적성을 찾기 위해 약 2년의 시간을 보냈습니다. 결국 저는 다른 사람들보다 늦게 취업하게 되었습니다.", "keys": "save time planning for / didn't know my interests / without a clear reason / find my aptitude / than others"}
        ]
    },
    {
        "no": 15, "title": "직업의 미래 변화",
        "q_en": "Name one job you are familiar with. Do you think employees in that field will work in a similar way in 10 years? Why or why not?",
        "q_ko": "당신이 잘 아는 직업 하나에 대해 말해보세요. 그 분야의 종사자들이 10년 후에도 비슷한 방식으로 일할 것이라고 생각합니까? 그 이유는 무엇입니까?",
        "answers": [
            {"type": "Answer 1 (마케팅)", "en": "I'm familiar with marketing jobs, and I think employees in that field will work in a different way in 10 years.\n\nThat's because AI programs have developed quickly. So, they can change marketing trends in 10 years.\n\nIn the past, people had to do market research and analysis by themselves. However, nowadays AI programs can do most of that work. As a result, employees can save time and focus more on developing creative marketing ideas.", "ko": "저는 마케팅 직무에 대해 잘 알고 있으며, 그 분야의 직원들은 10년 후에 다른 방식으로 일하게 될 것이라고 생각합니다. 왜냐하면 AI 프로그램이 빠르게 발전해왔기 때문입니다. 그래서 10년 안에 마케팅 트렌드를 바꿀 수 있습니다. 예전에는 사람들이 시장 조사와 분석을 직접 해야 했습니다. 그러나 요즘에는 AI 프로그램이 그 대부분의 일을 할 수 있습니다. 그 결과 직원들은 시간을 절약할 수 있고, 창의적인 마케팅 아이디어를 개발하는 데 더 집중할 수 있습니다.", "keys": "have developed quickly / in 10 years / In the past / market research and analysis / most of that work / developing creative marketing ideas"},
            {"type": "Answer 2 (의사 - 만점 답변)", "en": "I don't think doctors will work in a similar way in 10 years.\n\nThat's because we can see a doctor remotely. So, we don't have to travel far to see a doctor.\n\nWhen I was young, I lived in a small town called Ju-gyo. Because there were few medical clinics in my town, I had to travel to another city to see a doctor. But nowadays, I can get medical advice through a smartphone app. As a result, I can get high-quality medical treatment anytime, anywhere.", "ko": "저는 의사들이 10년 후에도 지금과 같은 방식으로 일할 것이라고 생각하지 않습니다. 왜냐하면 우리는 원격으로 진료를 받을 수 있기 때문입니다. 그래서 의사를 만나기 위해 멀리 이동할 필요가 없습니다. 제가 어렸을 때 저는 주교라는 작은 마을에 살았습니다. 우리 마을에는 병원이 거의 없었기 때문에 의사를 만나기 위해 다른 도시로 가야 했습니다. 하지만 요즘에는 스마트폰 앱을 통해 의사의 진료를 받을 수 있습니다. 그 결과 언제 어디서나 양질의 의료 서비스를 받을 수 있습니다.", "keys": "see a doctor remotely / travel far to / called / medical clinics / through a smartphone app / get high-quality medical treatment"}
        ]
    }
]

# ==========================================
# 2. Streamlit UI 구성
# ==========================================

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
        st.info("💡 암기 꿀팁: 공통 템플릿(That's because ~ So ~)과 경험 도입부(When I was ~)를 적극 활용하세요!")
        for qa in part5_qa_data:
            with st.expander(f"📝 NO.{qa['no']} - {qa['title']}"):
                st.markdown(f"**Q. {qa['q_en']}**")
                st.caption(f"해석: {qa['q_ko']}")
                st.divider()
                
                for ans in qa['answers']:
                    st.markdown(f"### ✅ {ans['type']}")
                    st.success(ans['en'])
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
        
        st.markdown("### 📊 AI 점수 산출 로직")
        st.latex(r"Total Score = \left( \frac{P1 + P2 + P3 + P4 + P5}{Total Max} \right) \times 200")
        
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
