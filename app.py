# 실습 02
# 테스트!
import os
import secrets
from openai import OpenAI
import streamlit as st
import requests
import pandas as pd

    #http://data4library.kr/api/loanItemSrch?authKey=ce0c893b3fcd2b1080903988f1fdd1367c7f811cdcad7d0a3a2ab99666816111&startDt=2020-01-01&endDt=2024-12-11&gender=1&frome_age=0&to_age=100&pageSize=2&dtl_region=00&format=json

st.set_page_config(layout="wide")

con0, con1, con2 = st.columns([0.1,0.8,0.1])
col1, center ,col2 = st.columns([0.45,0.1,0.45])

api_gpt = st.secrets["API_KEY"]
os.environ["OPENAI_API_KEY"] = api_gpt
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)




def fetch_library_data(startDt, endDt, gender, from_age, to_age, pageSize, dtl_kdc):
    base_url = "http://data4library.kr/api/loanItemSrch"
    params = {
        "authKey": api_key,
        "startDt": startDt,
        "endDt": endDt,
        "gender": gender,
        "from_age": from_age,
        "to_age": to_age,
        "pageSize": pageSize,
        "dtl_kdc": dtl_kdc,
        "format": "json",
        "pageNo": "1"
    }

    response = requests.get(base_url, params=params)
    
    # 디버깅용 URL 및 응답 출력
    #st.write(f"API 호출 URL: {response.url}")
    #st.write(f"API 응답: {response.json()}")

    if response.status_code == 200:
        return response.json()  # JSON 응답 반환
    else:
        st.error(f"API 호출 실패: {response.status_code}")
        return None



with con1:
    st.markdown(
        """
        <div style="background-color: #ffe500; padding: 20px; border-radius: 10px; width: 80vh;">
            <h3>📚도서 추천 웹사이트📚</h3>
            이곳에서는 GPT4 API와 공공 도서관 데이터를 활용하여 독서 경험을 더욱 풍성하게 만들어드립니다. 독서를 좋아하는 모든 사람들에게 추천 도서를 제공하고, 재미있는 퀴즈로 책의 내용을 더 깊이 이해할 수 있는 기회를 제공합니다.
        </div>
        """,
        unsafe_allow_html=True
    )
# 앱 제목

    st.divider()

# 재료 입력 받기
#food = st.text_input("aa .")

api_key = st.secrets["Lib_API_KEY"]
# API 키 출력 (테스트용)
 
#http://data4library.kr/api/loanItemSrch?authKey=ce0c893b3fcd2b1080903988f1fdd1367c7f811cdcad7d0a3a2ab99666816111&startDt=2022-01-01&endDt=2022-03-31& 
#gender=1&age=20&region=11;31&addCode=0&kdc=6&pageNo=1&pageSize=10

# Streamlit 앱 제목
with col1 :

    st.markdown(
        """
        <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px;">
            <h3>도서 추천 시스템 !</h3>
            This is column 1 with a light red background.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
# 1. 조회 일자 입력 startdt end dt
#2. 연령을 입력하시오 age 
#3. 성별 gender
#4. 페이지 크기 - 한 페이지당 제고되는 도서목록 개수 지정 pagesize
#5. 도서구분 class_no 분류코드 


    # 1. 조회 일자 입력 startdt end dt
    st.header("1. 조회 일자의 범위를 알려주세요")
    # 날짜와 시간 입력
    st.write("당월의 집계는 다음달에 나오니 이전 달까지 조회하시는 것을 추천드립니다.")
    startDt = st.date_input("범위의 시작 날짜를 선택하세요")
    endDt = st.date_input("범위의 끝 날짜을 선택하세요")

    # 결과 출력
    st.write("선택한 날짜와 시간:")
    st.write(f"{startDt} {endDt}")

    st.divider()


    #st.header("1. 도서관 선택")
    #library_options = ["도서관 A", "도서관 B", "도서관 C"]  # 도서관 리스트 (API로 가져올 수 있음)
    #selected_library = st.selectbox("도서관을 선택하세요:", library_options)


    #2. 연령을 입력하시오 age 
    age_start = -1
    age_end = -1
    st.header("2. 조회하고 싶은 연령의 범위를 알려주세요~")
    st.write("범위를 넓게 잡으시는 걸 추천드립니다.")
    frome_age = st.text_input("범위의 시작 나이", placeholder="예: 20")
    to_age = st.text_input("범위의 끝 나이", placeholder="예: 29")

    if age_end != -1 and age_start != -1:
        st.write(f"나이 범위: {frome_age}세 ~ {to_age}세")

    st.divider()

    #3. 성별 gender
    st.header("3. 성별 선택")
    age_group = st.radio(
        "성별을 선택하세요:",
        options=["전체", "여성", "남성"],
    )
    st.write(age_group)
    if(age_group == "남성"):
        gender = 0
    elif(age_group == "여성"):
        gender = 1
    else:
        gender = 0;1;2
    
    st.divider()

    #4. 페이지 크기 - 한 페이지당 제고되는 도서목록 개수 지정 pagesize
    st.header("4. 도서 추천 개수")

    pageSize = st.text_input("원하시는 추천받으실 도서의 개수를 알려주세요 !",placeholder="예: 5 (꼭 숫자만 입력해주세요 ㅜㅡㅜ)")
    st.divider()

    #5. 도서구분 class_no 분류코드 
    st.header("5. 한국 도서구분 분류코드!")
    st.write("00 총류 01 도서학, 서지학 02 문헌정보학 03 백과사전 04 일반 논문집 05 일반 연속간행물 06 학·협회,기관 07 신문, 언론, 저널리즘 08 일반 전집, 총서 09 향토자료")
    st.write("10 철학 11 형이상학 12 인식론, 인과론, 인간학 13 철학의 체계 14 경학 15 동양 철학, 사상 16 서양철학 17 논리학 18 심리학 19 윤리학, 도덕철학 ")
    st.write("20 종교 21 비교종교학 22 불교 23 기독교 24 도교 25 천도교 26 신도 27 바라문교, 인도교 28 회교(이슬람교) 29 기타 제종교 ")
    st.write("30 사회과학 31 통계학 32 경제학 33 사회학, 사회문제 34 정치학 35 행정학 36 법학 37 교육학 38 풍속, 민속학 39 국방, 군사학")
    st.write("40 자연과학 41 수학 42 물리학 43 화학 44 천문학 45 지학 46 광물학 47 생물과학 48 식물학 49 동물학 ")
    st.write("50 기술과학 51 의학52 농업, 농학 53 공학, 공업일반  54 건축공학 55 기계공학 56 전기공학, 전자공학 57 화학공학 58 제조업 59 가정학 및 가정생활")
    st.write("60 예술61 건축술 62 조각 63 공예, 장식미술 64 서예 65 회화, 도화 66 사진술 67 음악 68 연극 69 오락, 운동 ")
    st.write("70 언어 71 한국어 72 중국어 73 일본어 74 영어 75 독일어 76 프랑스어 77 스페인어 78 이탈리아어 79 기타 제어 80 문학 ")
    st.write("89 기타 제문학81 한국문학 82 중국문학 83 일본문학 84 영미문학85 독일문학 86 프랑스문학 87 스페인문학 88 이탈리아문학")
    st.write("90 역사 91 아시아(아세아) 92 유럽(구라파) 93 아프리카 94 북아메리카(북미) 95 남아메리카(남미) 96 오세아니아(대양주) 97 양극지방 98 지리 99 전기 ")

    dtl_kdc = st.text_input("원하시는 도서구분 분류코드를 입력해주세요 !",placeholder="예시 : 41 (수학을 희망하는 경우)")
    st.divider()



    # 추천 도서 결과 버튼
    if st.button("추천 도서 확인"):
        st.subheader("📚 추천 도서 목록")
        # 여기서 도서관정보나루 API를 호출하여 데이터를 가져오고, 결과를 표시
        st.write(f"선택한 조회 일자: {startDt} {endDt}")
        st.write(f"선택한 연령대: {frome_age}세 ~ {to_age}세")
        st.write(f"선택한 성별: {age_group}")
        st.write(f"선택한 도서구분 분류코드: {dtl_kdc}")
        st.write(f"도서 추천 개수: {pageSize}")

        st.info("추천 도서 목록은 API를 통해 곧 제공될 예정입니다.")

        #
        data = fetch_library_data(startDt,endDt,gender,frome_age,to_age,pageSize,dtl_kdc)
        if data:
            # 데이터프레임으로 변환 (예: 대출 도서 목록)
            books = data.get("response", {}).get("docs", [])
            if books:
                st.subheader("📚 추천 도서 목록")
            for book in books:
                book = book.get("doc","없음")
                # 개별 책 정보 가져오기
                book_name = book.get("bookname", "제목 없음")
                authors = book.get("authors", "저자 정보 없음")
                publisher = book.get("publisher", "출판사 정보 없음")
                publication_year = book.get("publication_year", "출판년도 정보 없음")
                loan_count = book.get("loan_count", 0)
                book_image_url = book.get("bookImageURL", None)
                book_detail_url = book.get("bookDtlUrl", "#")

                # 책 이미지 및 설명 표시
                if book_image_url:
                    st.image(book_image_url, width=150, caption=book_name)
                else:
                    st.write(f"📖 {book_name}")  # 이미지가 없는 경우 텍스트만 표시

                # 상세 정보 표시
                st.markdown(
                    f"""
                    **제목**: [{book_name}]({book_detail_url})  
                    **저자**: {authors}  
                    **출판사**: {publisher}  
                    **출판년도**: {publication_year}  
                    **대출건수**: {loan_count}  
                    """,
                    unsafe_allow_html=True,
                )
                st.divider()  # 각 책 사이에 구분선 추가
        else:
            st.warning("추천 도서 목록이 없습니다.")
    else:
        st.error("API 응답을 가져오지 못했습니다.")


with center:
    st.markdown(
        """
        <div style="background-color:rgb(0, 255, 98), 45) 37, 37); padding: 20px; border-radius: 10px; height: 250vh; position: relative;">
            <h3>📚📚📚</h3>
            
        </div>
        """,
        unsafe_allow_html=True
    )
        
        
with col2:
    st.markdown(
        """
        <div style="background-color: #ccccff; padding: 20px; border-radius: 10px;">
            <h3>도서 퀴즈 시스템</h3>
            This is column 3 with a light blue background.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    
    st.header("책의 제목과 저자를 입력해주세요 !")
    
    gpt_book_name = st.text_input("책의 이름을 알려주세요 !",placeholder="예: 빙하에서 살아남기")
    gpt_book_author = st.text_input("책의 저자를 알려주세요 !",placeholder="예: 최덕희")

    # 퀴즈 생성 함수
    # 퀴즈 생성 함수
    def generate_quiz(gpt_book_name, gpt_book_author):
        # GPT-4 모델을 사용하여 퀴즈 생성 요청
        chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": "당신은 퀴즈 생성 전문가입니다. 사용자가 제공한 책의 내용에 기반하여 퀴즈를 작성하세요.",
            },
            {
                "role": "user",
                "content": f"책 '{gpt_book_name}'의 내용과 저자 {gpt_book_author}에 대한 퀴즈를 1문항 만들어주세요. 질문과 답을 포함해주세요.",
            },
        ],
        model="gpt-4o",
        )

        # 응답 내용 추출
        result = chat_completion.choices[0].message.content
        return result

    # 버튼을 눌렀을 때 퀴즈 생성
    if st.button("퀴즈 생성"):
        if gpt_book_name and gpt_book_author:
            with st.spinner('퀴즈를 생성하는 중...'):
                quiz = generate_quiz(gpt_book_name, gpt_book_author)
                st.subheader("생성된 퀴즈:")
                st.write(quiz)  # 퀴즈 출력
        else:
            st.error("책 제목과 저자 이름을 모두 입력해주세요.")
        

# 추가 정보 섹션
st.sidebar.title("📖 도서 추천 시스템 도움말")
st.sidebar.info(
    """
    1. 조회 일자 범위, 연령 범위, 성별, 도서 추천 개수, 원하는 도서 분류코드를 안내에 맞게 입력해주세요 .
    2. "추천 도서 확인" 버튼을 눌러주세요 !
    3. 추천 받은 도서들을 확인하세요 !!
    """
)


st.sidebar.title("📖 도서 퀴즈 시스템 도움말")
st.sidebar.info(
    """
    아직 미완성!
    """
)
