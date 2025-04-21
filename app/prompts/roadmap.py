import pickle as pkl
def get_roadmap():
    roadmap_prompt = ""
    with open("app/prompts/pickle/roadmap.pkl", "rb") as f:
        roadmap_prompt = pkl.load(f)
    return roadmap_prompt