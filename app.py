import random
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 2. 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애는 이제 그만! 버튼을 눌러 오늘의 메뉴를 골라보세요.")

# 3. 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "짜장면",
    "짬뽕",
    "초밥",
    "파스타",
    "햄버거",
    "국밥",
    "비빔밥",
    "칼국수",
    "쌀국수",
    "마라탕",
    "샐러드",
    "샌드위치",
    "부대찌개",
    "라멘",
]

st.divider()  # 구분선

# 4. 버튼 생성 및 랜덤 추천 로직
if st.button("🎲 오늘의 점심 메뉴 뽑기!", use_container_width=True):
  # random.choice()로 리스트에서 무작위 항목 1개 선택
  selected_menu = random.choice(lunch_menus)

  # 시각적 효과 및 결과 출력
  st.balloons()  # 화면에 풍선이 날아가는 효과
  st.success(f"🎉 오늘의 추천 점심 메뉴는 **[{selected_menu}]** 입니다!")
