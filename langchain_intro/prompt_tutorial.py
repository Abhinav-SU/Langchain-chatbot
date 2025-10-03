#Importing ChatPromptTemplate from langchain.prompts 
from langchain.prompts import ChatPromptTemplate


#Basic review template string with context and question
review_template_str = """Your job is to use patient reviews to answer 
question about their expeience at a hospital.
Use the following context to answer questions. Be as detailed
as possible, but dont make up information that's not from the context.
If you dont know an answer, say you dont know.


{context}

{question}
"""

#Creating a review template from review template string using the ChatPromptTemplate
review_template = ChatPromptTemplate.from_template(review_template_str)

#Providing the context and the question from user
context= "I had a great stay!"
question ="Did anyone have a positive experience?"

#Printing the result of the review tempate after formatting it
print(review_template.format(context=context,question=question))