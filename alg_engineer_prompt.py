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
算法工程师
"""
question = """

"""
reference = """
所有已知知识
"""
direction = """
找到最佳解决方案
"""
constrain = """
"1. 答案必须符合学术标准，提供清晰、逻辑性强且有充分支持的答案。"
"2. 避免使用人称代词，确保答案客观且专注。"
"3. 回答格式应模仿科学论文的结构，包括引言、方法论、结果和结论（适用时）。（可以通过代码示例展现问题：python(针对数学计算不使用高级函数库)
"""
language = 'ch'

prompt = generate_prompt(role, question, reference, direction, constrain, language)
#save the prompt to a file
with open('prompt.txt', 'w',encoding='utf-8') as f:
    f.write(prompt)

print(prompt)