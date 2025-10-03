from chatbot import review_chain


question = """Has anyone complained about communication with the hospital staff?"""

result = review_chain.invoke({"question": question})

print(result)