import streamlit as st
import random

# 운세 리스트
fortune_list = [
    "오늘은 행운의 날이에요!",
    "힘든 하루가 예상되니 조심하세요.",
    "새로운 기회가 찾아올 거예요!",
    "건강을 잘 챙기세요.",
    "오늘은 편안한 하루가 될 거예요."
]

# 앱 제목
st.title("오늘의 운세 확인")

# 날짜 입력 받기
user_date = st.date_input("오늘의 날짜를 선택하세요:")

# 운세 추천 버튼
if st.button("오늘의 운세 보기"):
    st.write(f"{user_date}의 운세는:")
    st.success(random.choice(fortune_list))
    
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    
    # 음식 리스트
food_list = ['피자', '햄버거', '스시', '파스타', '라면', '샌드위치', '초밥', '떡볶이', '치킨', '부대찌개']

# 제목과 설명
st.title("랜덤 음식 추천기")
st.write("오늘 뭐 먹을지 고민되나요? 버튼을 눌러 랜덤 음식을 추천받아보세요!")

# 버튼이 눌리면 랜덤 음식 추천
if st.button("음식 추천 받기"):
    recommended_food = random.choice(food_list)
    st.success(f"오늘의 추천 음식: {recommended_food}")

# 음식 목록을 보여주는 기능 추가
if st.checkbox("음식 목록 보기"):
    st.write(food_list)