# 작성자:김재현
# 오픈소스
import streamlit as st
from yamlfix import fix_code

TEXT = {
    "HEADER": "Cloudwave YAML 문법검사기",
    "NOTICE": """\
사용법: From Text Box에 원하는 텍스트를 넣고, Ctrl+Enter를 넣으면 아래 To 결과박스에 결과가 나옵니다.
만약 잘 되지 않는다거나, 기타 문의사항은 https://open.kakao.com/o/sHwnai3f 여기로 연락 부탁드려요.
EC2 t3.micro 인스턴스로 배포중인데, 너무 약한 서버라서 트래픽 조금만 쌓여도 터집니다...\
    """,
}

st.header(TEXT["HEADER"])
st.text(TEXT["NOTICE"])


result = ""
q = st.text_area("From")
btn = st.button("제출")

if q or btn:
    result = fix_code(q)
    print(f"Result: {result}")

st.text_area("To", value=result)
