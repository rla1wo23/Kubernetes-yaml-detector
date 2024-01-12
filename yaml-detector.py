#작성자:김재현
#오픈소스
from openai import OpenAI
import streamlit as st


client = None
api_key = 'your api_key'
if api_key:
    client = OpenAI(api_key=api_key)

lang_list = ('Kubernetes yaml', 'js', 'sh', 'py')

st.header('Cloudwave yaml 문법검사기')

st.text('사용법: From Text Box에 원하는 텍스트를 넣고, Ctrl+Enter를 넣으면 아래 To 결과박스에 결과가 나옵니다.') 
st.text('만약 잘 되지 않는다거나, 기타 문의사항은 https://open.kakao.com/o/sHwnai3f 여기로 연락 부탁드려요')
st.text('EC2 t3.micro 인스턴스로 배포중인데, 너무 약한 서버라서 트래픽 조금만 쌓여도 터집니다...')


col1, col2 = st.columns(2)
result = ''
option = st.selectbox('Lang', lang_list)
q = st.text_area('From')
if client and q:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": f"You should change the indentation of the following text to suit the grammar of the language. Correct the text sent by the user into {option}"},
        {"role": "user", "content": q}
      ]
    )

    print(response.choices[0].message.content)
    result = response.choices[0].message.content

st.text_area('To', value=result)