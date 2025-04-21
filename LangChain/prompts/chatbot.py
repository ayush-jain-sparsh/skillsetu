import pickle as pkl
def get_mentor():
    text = ""
    with open('LangChain/prompts/pickle/langchain.pkl', 'rb') as f:
        text = pkl.load(f)
    return text