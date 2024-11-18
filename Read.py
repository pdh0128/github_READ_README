from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools.search import get_readme_url
load_dotenv()

prompt = """
어떤 사람의 깃허브 리드미 코드를 줄게 {readme}, 그에 대한 설명을 해줘.
1. 짧은 요약
2. 기술스택
"""

summary = PromptTemplate(input_variables=["readme"], template=prompt)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chain = summary | llm
code = get_readme_url(input())
res = chain.invoke(input={"readme" :code})
print(res)