def generate_prompt(role='', question='', reference='', direction='', constrain='', language='ch'):
    """
    Generate a research assistant prompt in either English or Chinese.

    Parameters:
    - question (str): The main question to address.
    - reference (str): Background information or reference material.
    - direction (str): Specific instructions on how to approach answering the question.
    - language (str): Language of the prompt ('English' or 'Chinese').

    Returns:
    - str: A formatted prompt.
    """
    if role == '':
        role = 'algorithm engineer'
    if question == '':
        question = 'How can we improve the efficiency of the algorithm?'
    if reference == '':
        reference = 'all known knowledge'
    if direction == '':
        direction = 'find the best solution'
    if constrain == '':
        constrain = 'no constrain'

    if language == 'ch':
        role = f"角色：{role}"
        question = f"问题概述：{question}"
        reference = f"参考资料摘要：{reference}"
        direction = f"回答方向：{direction}"
        constrain = f"约束条件：{constrain}"    
    else:
        role = f"Role: {role}"
        question = f"Question Overview: {question}"
        reference = f"Reference Summary: {reference}"
        direction = f"Answer Direction: {direction}"
        constrain = f"Constrain: {constrain}"

    prompt = f"{role}\n\n{question}\n\n{reference}\n\n{direction}\n\n{constrain}"
    return prompt

role = """
软件工程师
"""
question = """
什么是图论中的最短路径问题，请举例说明
"""
reference = """
所有已知知识
"""
direction = """
找到最佳解决方案
"""
constrain = """
"1. 答案必须符合工程实践需求，提供清晰、逻辑性强且有充分支持的答案。"
"2. 避免使用人称代词，确保答案客观且专注。"
"3. 回答格式应模仿对于需求文档/设计文档的格式，使用plantuml，表格，python代码示例结合说明问题。
"""
language = 'ch'

prompt = generate_prompt(role, question, reference, direction, constrain, language)
#save the prompt to a file
with open('prompt.txt', 'w',encoding='utf-8') as f:
    f.write(prompt)

print(prompt)

# role = """
# Algorithm Engineer
# """
# question = """
# How can we improve the efficiency of the algorithm?
# """
# reference = """
# All known knowledge
# """
# direction = """
# Find the best solution
# """
# constrain = """
# "1. The response must adhere to academic standards, providing clear, logical, and well-supported answers."
# "2. Avoid the use of personal pronouns, ensuring the answer remains objective and focused."
# "3. Format the response to mimic the structure of a scientific paper, including an introduction, methodology, results, and conclusion where applicable.")
# """
# language = 'en'

# prompt = generate_prompt(role, question, reference, direction, constrain, language)
# #save the prompt to a file
# with open('prompt.txt', 'w',encoding='utf-8') as f:
#     f.write(prompt)
# print(prompt)