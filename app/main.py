

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from config import ModelConfigs

configs = ModelConfigs()

model = ChatOpenAI(model=configs.Model_Name, api_key=configs.Model_Api_Key,base_url=configs.Model_Base_Url)


messages = [SystemMessage(content="You are a helpful assistant."), HumanMessage(content="Who are you?")]

result = model.invoke(messages)

print(result)