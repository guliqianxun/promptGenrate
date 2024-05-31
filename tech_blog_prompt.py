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
请结合我的总结和疑问，帮助整理文章Tent: Fully Test-time Adaptation by Entropy Minimization 
"""
reference = """

"""
direction = """
找到最佳解决方案
"""
constrain = """
1. 从技术源头开始拆解，逐步分析技术解决问题以及为何使用当前解决方案
2. 给出技术实践方式，对比同类问题其他解决方案以及是否在同背景下存在最佳实践
3. 用词客观清晰，逻辑严谨，不偏离主题
"""
language = 'ch'

prompt = generate_prompt(role, question, reference, direction, constrain, language)
#save the prompt to a file
with open('prompt.txt', 'w',encoding='utf-8') as f:
    f.write(prompt)

print(prompt)