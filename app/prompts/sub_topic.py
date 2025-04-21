import pickle as pkl
def get_subtopic():
    subtopic_prompt = ""
    with open("app/prompts/pickle/subtopic.pkl", "rb") as f:
        subtopic_prompt = pkl.load(f)
    return subtopic_prompt