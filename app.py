import random
import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 2. 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 뽑아보세요.")

# 3. 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "국밥",
    "햄버거",
    "파스타",
    "쌀국수",
    "비빔밥",
    "부대찌개",
    "칼국수",
    "마라탕",
    "샌드위치",
]

st.divider()  # 구분선

# 4. 버튼 생성 및 랜덤 추천 로직
# use_container_width=True 옵션으로 버튼을 화면 너비에 맞게 넓게 만듭니다.
if st.button("🎲 오늘의 메뉴 추천받기", use_container_width=True):
    # 리스트에서 무작위로 1개 선택
    selected_menu = random.choice(lunch_menus)

    # 풍선 애니메이션 효과
    st.balloons()

    # 결과 출력
    st.success(f"오늘의 추천 점심 메뉴는 **'{selected_menu}'** 입니다! 🎉")
