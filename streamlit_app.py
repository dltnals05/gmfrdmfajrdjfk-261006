import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit 요소 체험실", page_icon="🧪", layout="wide")

st.title("Streamlit 요소 체험실")
st.write("화면의 요소를 직접 눌러 보세요. 입력을 바꾸면 페이지가 다시 실행되고 결과에도 바로 반영됩니다.")
st.caption("Python 코드 몇 줄로 데이터 앱을 만드는 Streamlit의 기본 요소를 살펴봅니다.")

st.info("왼쪽 위 메뉴에서 화면을 넓히거나, 각 탭의 위젯을 바꾸며 동작을 확인해 보세요.")

intro_tab, input_tab, data_tab = st.tabs(["1. 텍스트와 버튼", "2. 입력과 상태", "3. 데이터와 차트"])

with intro_tab:
    st.header("텍스트로 설명하고, 버튼으로 동작시키기")
    st.write("`st.write()`는 문자열, 숫자, 데이터 등 다양한 내용을 화면에 표시합니다.")

    st.subheader("텍스트 표현")
    st.markdown("마크다운으로 **굵은 글씨**, *기울임*, 목록과 링크를 표시할 수 있어요.")
    st.code('st.title("제목")\nst.write("화면에 내용을 표시합니다")', language="python")
    st.caption("`st.caption()`은 본문보다 작은 보충 설명에 사용합니다.")

    st.subheader("버튼과 입력창")
    visitor_name = st.text_input("이름을 입력해 보세요", placeholder="예: 민지")
    if st.button("인사 받기", type="primary"):
        if visitor_name.strip():
            st.success(f"반가워요, {visitor_name.strip()}님! 버튼 클릭으로 동작을 실행했어요.")
        else:
            st.warning("먼저 이름을 입력해 주세요.")
    st.caption("`st.text_input()`은 한 줄 입력, `st.button()`은 클릭 이벤트를 처리합니다.")

    with st.expander("펼쳐서 더 알아보기: 폼"):
        st.write("폼은 여러 입력을 모아 제출 버튼을 눌렀을 때 한 번에 처리합니다.")
        with st.form("feedback_form"):
            feedback = st.text_area("체험 소감", placeholder="좋았던 점이나 궁금한 점을 적어 보세요.")
            rating = st.select_slider("난이도", options=["쉬움", "보통", "어려움"])
            submitted = st.form_submit_button("소감 제출")
        if submitted:
            st.success(f"소감이 제출됐어요. 선택한 난이도: {rating}")
            if feedback:
                st.write(feedback)

with input_tab:
    st.header("위젯으로 값을 입력받기")
    st.write("위젯의 반환값을 변수에 담으면, 그 값을 계산이나 화면 표시 등에 사용할 수 있습니다.")

    left, right = st.columns(2)
    with left:
        topic = st.selectbox("관심 주제를 선택하세요", ["데이터", "웹 앱", "시각화"])
        display_mode = st.radio("표시 방식", ["간단히", "자세히"], horizontal=True)
        favorite_topics = st.multiselect("관심 주제를 더 골라 보세요", ["Python", "Streamlit", "pandas", "차트"])
        quantity = st.number_input("항목 수", min_value=1, max_value=20, value=5)
    with right:
        score = st.slider("만족도를 조절하세요", min_value=0, max_value=100, value=68)
        show_details = st.checkbox("상세 설명 보기", value=True)
        dark_example = st.toggle("예시 알림 켜기", value=False)
        selected_date = st.date_input("날짜 선택")

    st.caption("`selectbox`, `radio`, `multiselect`, `number_input`, `slider`, `checkbox`, `toggle`, `date_input`은 입력 방식이 서로 다른 위젯입니다.")
    st.subheader("입력 결과")
    st.write(f"선택한 주제는 **{topic}**, 표시 방식은 **{display_mode}**, 항목 수는 **{quantity}개**입니다.")
    st.progress(score, text=f"만족도 {score}%")
    if show_details:
        st.write(f"관심 주제: {', '.join(favorite_topics) if favorite_topics else '아직 선택하지 않았어요'} · 날짜: {selected_date}")
    if dark_example:
        st.warning("토글이 켜져 있어요. 조건에 따라 다른 메시지를 보여줄 수 있습니다.")

    st.subheader("폼으로 입력 모아 제출하기")
    st.write("폼 안의 값은 제출할 때까지 모아 두었다가 한 번에 처리할 수 있습니다.")
    with st.form("quick_poll"):
        poll_topic = st.selectbox("가장 흥미로운 요소", ["입력 위젯", "표", "차트"], key="poll_topic")
        poll_comment = st.text_input("한 줄 의견", key="poll_comment")
        poll_submitted = st.form_submit_button("응답 제출")
    if poll_submitted:
        st.success(f"'{poll_topic}'을(를) 골랐어요." + (f" 의견: {poll_comment}" if poll_comment else ""))

with data_tab:
    st.header("표와 차트로 데이터를 살펴보기")
    st.write("표는 값을 자세히 확인할 때, 차트는 값의 차이나 변화를 빠르게 볼 때 유용합니다.")

    row_count = st.slider("표와 차트에 표시할 월 수", min_value=3, max_value=12, value=8)
    chart_type = st.radio("차트 종류", ["선 차트", "막대 차트"], horizontal=True)

    months = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
    data = pd.DataFrame(
        {
            "월": months[:row_count],
            "방문자": [120, 145, 132, 180, 205, 198, 240, 225, 270, 290, 275, 320][:row_count],
            "가입자": [24, 32, 28, 41, 53, 49, 64, 60, 72, 81, 78, 92][:row_count],
        }
    )

    st.subheader("데이터 표")
    st.dataframe(data, use_container_width=True, hide_index=True)
    st.caption("`st.dataframe()`은 정렬하고 탐색할 수 있는 표를 표시합니다.")

    st.subheader(chart_type)
    chart_data = data.set_index("월")
    if chart_type == "선 차트":
        st.line_chart(chart_data, use_container_width=True)
    else:
        st.bar_chart(chart_data, use_container_width=True)
    st.caption("`st.line_chart()`와 `st.bar_chart()`는 표의 숫자를 빠르게 시각화합니다.")

    st.subheader("숫자를 한눈에: 메트릭")
    metric_columns = st.columns(3)
    metric_columns[0].metric("표시한 달", f"{row_count}개월")
    metric_columns[1].metric("방문자 합계", f"{data['방문자'].sum():,}명")
    metric_columns[2].metric("가입자 합계", f"{data['가입자'].sum():,}명", delta="예시 데이터")

st.divider()
st.caption("이 페이지는 Streamlit의 기본 위젯과 시각화 기능을 보여 주는 인터랙티브 예시입니다.")