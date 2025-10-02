from langchain.schema.messages import HumanMessage, SystemMessage
from chatbot import chat_model

messages = [
    SystemMessage(
        content="""You are an assistant knowledeable about
          healthcare. Only answer healthcare related questions."""
    ),
    #HumanMessage(content="What is medicaid managed care?"),
    HumanMessage(content="How do i change tire?"),
]

print(chat_model.invoke(messages))