import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'how to mark the sentence : The loss function of our model mainly consists of two parts: cross-entropy loss; for labeled V-Itrajectory data, we use supervised loss ls, and for unlabeled V-I trajectory data, we use consistency loss lu. Cross-entropy loss is a commonly used loss function in supervised learning, especially in classification tasks.',
  },
])
print(response['message']['content'])