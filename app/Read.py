from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools.search import get_readme_info, get_repo_content, get_reponame
from app.output_parser import summary_parser, Summary, read_summary_parser
load_dotenv()

async def read_home(name):
    prompt = """
    어떤 사람의 깃허브 리드미 코드를 줄게 {readme}, 그에 대한 설명을 해줘, 404오류가 뜨면 None을 반환해줘.
    1. 짧은 요약
    2. 기술스택
    {output_format}
    """

    summary = PromptTemplate(input_variables=["readme"], template=prompt, partial_variables={"output_format" : summary_parser.get_format_instructions()})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    chain = summary | llm | summary_parser
    code = get_readme_info(name)
    res = chain.invoke(input={"readme" :code})
    print(res)
    return res

async def read(name):
    prompt = """
        어떤 사람의 깃허브 리드미 코드를 줄게 {readme}, 그에 대한 설명을 해줘, 404오류가 뜨면 None을 반환해줘.
        1. 짧은 요약
        {output_format}
        """

    summary = PromptTemplate(input_variables=["readme"], template=prompt,
                             partial_variables={"output_format": read_summary_parser.get_format_instructions()})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    contents = []
    chain = summary | llm | read_summary_parser
    repo_names = get_reponame(name)
    for repo_name in repo_names:
        code = get_repo_content(name, repo_name)
        if code is None or not code.strip():
            res = {"summary": "README 파일이 비어있거나 존재하지 않습니다."}
        else :
            res = chain.invoke(input={"readme": code})
        print(res)
        contents.append({repo_name : res})
    print(f"최종 : {contents}")
    return contents


if __name__ == '__main__':
    read('whgkals')