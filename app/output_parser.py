from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Dict

class Summary(BaseModel):
    summary: str = Field(description="그 사람의 깃허브 리드미에 대한 짧은 요약")
    engine: str = Field(description="기술스택")

    def to_dict(self) -> Dict[str, str]:
        return {"summary": self.summary, "engine": self.engine}

summary_parser = PydanticOutputParser(pydantic_object=Summary)

class read_Summary(BaseModel):
    summary: str = Field(description="그 사람의 깃허브 리드미를 읽고 프로젝트에 대한 짧은 요약")

    def to_dict(self) -> Dict[str, str]:
        return {"summary": self.summary}

read_summary_parser = PydanticOutputParser(pydantic_object=read_Summary)