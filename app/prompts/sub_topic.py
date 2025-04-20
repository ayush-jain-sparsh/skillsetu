def get_subtopic():
    subtopic_prompt = """Provide me the subtopic of the topic in detail related to the task i provide and for each subtopic 
                provide me the links of the sites where i can study and learn these subtopic, without using star or # for bold 
                letters or something like that.
                
                Its json structure should be as-
                {'index' - index number(integer){
                'Subtopic' - subtopic inside the topic
                'Reference' - reference links to cover these subtopic(list)}}

                as for reference you can as much response as posssible and it should be with respect to subtopic in list.

                the output should be strictly follow the given json format no additional things"""
    return subtopic_prompt