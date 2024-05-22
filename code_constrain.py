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
软件架构工程师
"""
question = """
请协助整理软件架构独立构件风格的特点、优缺点及应用场景。
"""
reference = """
独立构件风格
触发事件
主函数
调用返回风格
主函数
事件管理机制
通知执行
返回执行结果
子函数
调用子函数
子函数
构件之间不直接交互
松耦合
构件之间直接交互
紧耦合
返回执行结果

优点
松耦合。
2、良好的重用性/可修改性/可扩展性。
缺点
1、构件放弃了对系统计算的控制。一个构件触发一个事件时，不能确定其他构件是否会响应它。而且即使它知道事件注册了哪些构件的过程，它也不能保证这些过程被调用的顺序。
数据交换的问题。
3、既然过程的语义必须依赖于被触发事件的上下文约束，关于正确性的推理就存在问题。
特点
系统由若干子系统构成且成为一个整体;系统有统一的目标;子系统有主从之分;每一子系统有自己的事件收集和处理机制
"""
direction = """
给出技术要点的关键说明
"""
constrain = """
"1. 答案必须符合工程实践需求，提供清晰、逻辑性强且有充分支持的答案。"
"2. 避免使用人称代词，确保答案客观且专注。"
"3. 回答格式应模仿对于需求文档/设计文档的格式，使用plantuml(基本语法，表格，python代码示例结合说明问题。
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