from chatbot import hospital_agent_executor

res1 = hospital_agent_executor.invoke(
    {"input": "What is current wait time at hospital A?"}  # Fixed: Input -> input, added hospital name
)
print(res1)

res2 = hospital_agent_executor.invoke(
    {"input": "What have patients said about their comfort at the hospital?"}  # Fixed: Input -> input
)
print(res2)