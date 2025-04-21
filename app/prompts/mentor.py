import pickle as pkl
def get_mentor():
    mentor_prompt = ""
    with open("app/prompts/pickle/mentor.pkl", "rb") as f:
        mentor_prompt = pkl.load(f)
    return mentor_prompt