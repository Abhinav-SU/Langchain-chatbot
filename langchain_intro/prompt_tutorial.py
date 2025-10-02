from langchain.prompts import ChatPromptTemplate

review_template_str = """Your job is to use patient reviews to answer 
question about their expeience at a hospital.
Use the following context to answer questions. Be as detailed
as possible, but dont make up information that's not from the context.
If you dont know an answer, say you dont know.


{context}

{question}
"""

review_template = ChatPromptTemplate.from_template(review_template_str)


context= "I had a great stay!"
question ="Did anyone have a positive experience?"

print(review_template.format(context=context,question=question))