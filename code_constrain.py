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
请协助我对比两种数据流图设计方案的优缺点
@startuml
!theme sketchy-outline
rectangle "传感器" as Sensor {
	usecase "传感器数据" as ParseSensorData
}

rectangle "存储模块" {
    usecase "存储传感器信息" as StoreSensorData
    usecase "存入光谱信息" as StoreSpectrumData
    usecase "存入水质信息" as StoreWaterQualityData
}

rectangle "解析模块" as AnalysisModel{
    usecase "解析传感器数据" as ParsedSensorData
    usecase "转发解析后光谱" as ParsedSpectrumData
    usecase "解析/反演后水质" as AnalysisedWaterQulityData
} 

database "数据库" as DB

ParseSensorData -down-> StoreSensorData : "传感器数据存储请求"
StoreSensorData -down-> DB : "存储传感器数据"

ParseSensorData -down-> ParsedSensorData : "传感器数据解析请求"
ParsedSensorData --> ParsedSpectrumData
ParsedSensorData --> AnalysisedWaterQulityData : "原始水质数据"

ParsedSpectrumData --> AnalysisedWaterQulityData : "水质数据"

ParsedSpectrumData -down-> StoreSpectrumData : "光谱数据存储请求"
StoreSpectrumData -down-> DB : "存储光谱数据"

AnalysisedWaterQulityData -down-> StoreWaterQualityData : "水质数据存储请求"
StoreWaterQualityData -down-> DB : "存储水质数据"

@enduml

第二种
@startuml
!theme sketchy-outline
rectangle "传感器" as Sensor {
    usecase "传感器数据" as ParseSensorData
}

rectangle "数据处理平台" as AnalysisPlatform{
    usecase "传感器数据缓存" as CacheSensorData
    usecase "解析后光谱" as ParsedSpectrumData
    usecase "解析/反演后水质" as AnalysisedWaterQulityData
} 

database "数据库" as DB

ParseSensorData -down-> CacheSensorData : "数据转发"
CacheSensorData -down-> ParsedSpectrumData : "解析光谱数据"
CacheSensorData -down-> DB : "存储传感器数据"


CacheSensorData -down-> AnalysisedWaterQulityData : "解析光谱数据"
ParsedSpectrumData --> AnalysisedWaterQulityData : "反衍光谱数据"

ParsedSpectrumData -down-> DB : "存储光谱数据"
AnalysisedWaterQulityData -down-> DB : "存储水质数据"

@enduml
"""
reference = """
软件架构设计原则
"""
direction = """
方案对比，评分估计，尽量刻薄
"""
constrain = """
"1. 答案必须符合工程实践需求，提供清晰、逻辑性强且有充分支持的答案。"
"2. 避免使用人称代词，确保答案客观且专注。"

"""
# "3. 回答格式应模仿对于需求文档/设计文档的格式，使用plantuml(基本语法，表格，python代码示例结合说明问题。
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
# as a introduction of purpose methods, please help me rephrase the following paragraph
# Initially, we present the methodology for extracting V-I trajectory signatures from an individual
# appliance’s combined terminal voltage and total current data. Following that, we provide a comprehensive
# explanation of the proposed model architecture
# """
# reference = """
# All known knowledge
# """
# direction = """
# Non-intrusive load monitoring, Semi-supervised learning, flexible thresholds, V-I trajectory, appliance identification
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