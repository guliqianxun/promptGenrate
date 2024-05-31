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

article: Tent: Fully Test-time Adaptation by Entropy Minimization 
my summary:
#### Important Point by Author

<mark class="customZot-Yellow">Existing adaptation settings extend training given more data and supervision. Transfer learning by ﬁne-tuning (Donahue et al., 2014; Yosinski et al., 2014) needs target labels to (re-)train with a supervised loss L(xt, yt). Without target labels, our setting denies this supervised training. Domain adaptation (DA) (Quionero-Candela et al., 2009; Saenko et al., 2010; Ganin &amp; Lempitsky, 2015; Tzeng et al., 2015) needs both the source and target data to train with a cross-domain loss L(xs, xt). Test-time training (TTT) (Sun et al., 2019b) adapts during testing but ﬁrst alters training to jointly optimize its supervised loss L(xs, ys) and self-supervised loss L(xs). Without source, our setting denies joint training across domains (DA) or losses (TTT). Existing settings have their purposes, but do not cover all practical cases when source, target, or supervision are not simultaneously available.</mark>[Page 2](zotero://open-pdf/library/items/P2LDXW9B?page=2&annotation=RICWY5L3)

> DA,TTT
 
<mark class="customZot-Yellow">TTT jointly optimizes this same loss on source data L(xs) with a supervised loss L(xs, ys), to ensure the parameters θ are shared across losses for compatibility with adaptation by L(xt).</mark>[Page 2](zotero://open-pdf/library/items/P2LDXW9B?page=2&annotation=WD8CTDUC)

> 使用有监督损失+无监督损失的形式，在测试数据集上，保留无监督损失使得模型在上线时依然拥有适应数据集变化的能力
 
<mark class="customZot-Yellow">Our test-time objective L(xt) is to minimize the entropy H(yˆ) of model predictions yˆ = fθ(xt). In particular, we measure the Shannon entropy (Shannon, 1948), H(yˆ) = − ∑ c p(yˆc) log p(yˆc) for the probability yˆc of class c. Note that optimizing a single prediction has a trivial solution: assign all probability to the most probable class. We prevent this by jointly optimizing batched predictions over parameters that are shared across the batch.</mark>[Page 3](zotero://open-pdf/library/items/P2LDXW9B?page=3&annotation=9GC6X5VF)

> 通过batch中包含不同预测类，因此难以存在将所有预测分到一个类中，熵直接为零的情况。避免损失函数不工作。
 
<mark class="customZot-Yellow">Transformation turns x¯ into the output x′ = γx¯ + β by afﬁne parameters for scale γ and shift β</mark>[Page 4](zotero://open-pdf/library/items/P2LDXW9B?page=4&annotation=RVZDT7FA)

> 通过调整输入，来匹配模型？
 
#### Important Information For me

<mark class="customZot-Red">The model to be adapted must be trained for the supervised task, probabilistic, and differentiable. No supervision is provided during testing, so the model must already be trained. Measuring the entropy of predictions requires a distribution over predictions, so the model must be probabilistic. Gradients are required for fast iterative optimization, so the model must be differentiable. Typical deep networks for supervised learning satisfy these model requirements.</mark>[Page 3](zotero://open-pdf/library/items/P2LDXW9B?page=3&annotation=82TNXU58)

> 已训练的，概率分布的，可差分的。
整体看来，该模型允许数据集出现值域上的偏移，但对于数据分布变化是无措的。
 



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