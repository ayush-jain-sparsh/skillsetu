
def get_roadmap():
    roadmap_prompt = """create roadmap of skill set to get a job in json format with thier main skill title and then 
                its subtopic and the resources link to complete these sub topics without using star or # for bold 
                letters or something like that and the roadmap to be prepare for given duration, 
                i.e. on the daily/weekly/monthly basis.
                
                Its json structure should be as-
                {'Day' - day number(integer)
                'Topic' - topic to be complete for given day
                'Subtopic' - subtopic inside the topic(list)
                'Reference' - reference links to cover these subtopic(list of list)}

                as for reference you can as much response as posssible and it should be with respect to subtopic in list.

                the output should be strictly follow the given json format no additional things
                
                now here if duration is based on daily basis then use Day as a key otherwise for weekly or monthly basis use Week or Month as a
                key respectively."""
    return roadmap_prompt