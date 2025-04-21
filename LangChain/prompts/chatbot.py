import pickle as pkl
def get_chat():
    text = ""
    with open('LangChain/prompts/pickle/langchain.pkl', 'rb') as f:
        text = pkl.load(f)
    return text
