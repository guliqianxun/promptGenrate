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
        question = f"问题概述：请针对下述方案/想法请可能严厉的提出你的意见{question}"
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
审稿人，同行专家
"""
question = """
"""
reference = """
所有已知知识
"""
direction = """
1.拆分想法/方案的内在逻辑，判断逻辑推理是否合理，完善
2.对比同类问题其他解决方案，是否在同背景下存在最佳实践
3.提出可能的问题，对方案进行批判性思考，提出改进意见
"""
constrain = """
1. 用词客观清晰，逻辑严谨，不偏离主题
2. 请提供详细的解释和理由，提供参考文献或者其他支持信息
"""
language = 'ch'

prompt = generate_prompt(role, question, reference, direction, constrain, language)
#save the prompt to a file
with open('reviewer.txt', 'w',encoding='utf-8') as f:
    f.write(prompt)

print(prompt)