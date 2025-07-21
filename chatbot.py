from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation',
    max_new_tokens=50
)

model = ChatHuggingFace(llm = llm)

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input.strip().lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print('AI: ',result.content)

print(chat_history)
