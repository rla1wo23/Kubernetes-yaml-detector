# 작성자:김재현
# 오픈소스
import streamlit as st
from yamlfix import fix_code


def main():
    TEXT = {
        "HEADER": "Cloudwave YAML 문법검사기",
        "NOTICE": """\
    사용법: From Text Box에 원하는 텍스트를 넣고, Ctrl+Enter를 넣으면 아래 To 결과박스에 결과가 나옵니다.
    만약 잘 되지 않는다거나, 기타 문의사항은 https://open.kakao.com/o/sHwnai3f 여기로 연락 부탁드려요.
    EC2 t3.micro 인스턴스로 배포중인데, 너무 약한 서버라서 트래픽 조금만 쌓여도 터집니다...\
        """,
    }

    TEXT_AREA_HEIGHT = 480
    st.set_page_config(layout="wide")

    st.header(TEXT["HEADER"])
    st.text(TEXT["NOTICE"])

    col1, col2, col3 = st.columns([3, 1, 3])

    with col1:
        st.markdown("### From:")
        q = st.text_area(
            "From text area",
            height=TEXT_AREA_HEIGHT,
            placeholder="포맷팅 할 YAML 텍스트를 입력하세요.",
            label_visibility="collapsed"
        )

    with col2:
        btn = st.button("Format ➡️")

    with col3:
        result = "Waiting for input..."
        if q or btn:
            result = fix_code(q)
            print(f"Result: {result}")
        st.markdown("### To:")
        st.code(result, language="YAML")


if __name__ == "__main__":
    main()
