#terminal에서 pip install streamlit, langchain, openai, langchain-openai

#import os #윈도우에서 작동되는지 확인시에는 사용, github에 올릴 때는 삭제
import streamlit as st

#openAI API키 저장
#os.environ["OPENAI_API_KEY"] = 'Your key'

from langchain.llms import OpenAI
llm = OpenAI()

from langchain_openai import ChatOpenAI

content = "코딩"
result = llm.predict(content + "에 대한 시를 써줘")
print(result)

from langchain_openai import ChatOpenAI

chatgpt = ChatOpenAI()
chatgpt = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens = 512)
answer = chatgpt.invoke("코딩에 대한 시를 써줘.")
print(answer.content)

import streamlit as st

st.set_page_config(
    page_title="DirChat",
    page_icon=":books")

st.title("_Private Data :red[QA Chat]_ :books:")

with st.sidebar:
    openai_api_key = st.text_input("Open API Key", key="chatbot_api_key", type="password")
    process = st.button("Process")
if process:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

content = st.text_input('시의 주제를 제시해주세요.')
if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chatgpt.predict(content + "에 대한 시를 써줘")
        st.write(result)