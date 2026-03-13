
import re
from typing import Dict
import long_responses as long
import wikipedia



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    



def check_all_messages(message):
    highest_prob_list: Dict[str, int] = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # ...existing code for responses...
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hii'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks',], single_response=True)
    response('Thank you, but I don\'t feel the same', ['i', 'love', 'you'], required_words=['love', 'you'])
    response('Namaste!', ['namaste', 'namaskar'], single_response=True)
    response('Oh! That\'s great', ['i', 'am' , 'fine'], required_words=['i','fine'])
    response('Yeah sure. I will try', ['can','you','help','me'], required_words=['help','me'])
    response('There are 2 types : formal and informal', ['how','many','types','education','india'], required_words=['how','types','india'])
    response('Jai Shree Ram!!',['jai','shree','shri','ram'], single_response=True)
    response('I was created on 7th August 2023', ['when','were','was','you','created','born'], required_words=['when'])
    response('Thank You!!',['nice','good','best','amazing','gorgeous','beautiful'], single_response=True)
    response('Oh! not much but i can try to answer you',['how','much','educated','you','are'], required_words=['how'])
    response('Please tell me what to explain.',['explain','elaborate'], single_response=True)
    response('Yes! It makes a person self dependent',['education','self','dependent'],required_words=['self','dependent'])
    response('Knowledge is a form of awareness or familiarity. It is often understood as awareness of facts or as practical skills, and may also mean familiarity with objects or situations.',['what','knowledge','define'],required_words=['knowledge'])
    response("Dharmendra Pradhan",['who','is','education','minister','india','name'],required_words=['education','minister','india'])
    response("Your degree is just a piece of paper, your education is seen in your behavior, attitude and character.",['quote','education'],required_words=['quote'])
    response('Telangana',['indian','state','government','set','it','camp','for','differently','abled','people'],required_words=['state','government','it','camp','differently','abled'])
    response('Nothing just passing the time.',['what','are','you','doing'],required_words=['what','doing'])
    response('I was created by Nagorao and Kanishk',['who','created','made','developed','you','invented'],required_words=['who','you'])
    response('You should watch Dr. Stone. It is a great anime which teaches you and entertain you at the same time.',['which','what','cartoon','anime','should','watch','see','recommend'],required_words=['anime'])
    response('It\'s on 10th August 2023',['what','date','submission'],required_words=['date'])
    response('Software Engineer \n Network Architect/Engineer \n Game Designer', ['career','options','career','option','cs','computer','science'],required_words=['career'])
    response('Mr. Narendra Modi',['prime','minister','india'],required_words=['prime','minister','india'])
    response('Mrs. Draupati Murmu',['president','india'], required_words=['president','india']) 
    response('You should watch Dr. Stone. It is a great anime which teaches you and entertain you at the same time.',['anime'],required_words=['anime'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_QUES_A, ['what','is','understand','term','education','mean'], required_words=['what','education'])
    response(long.R_QUES_B, ['education', 'system', 'india'], required_words=['system','india'])
    response(long.R_QUES_C, ['education', 'policy', 'india'], required_words=['policy','india'])
    response(long.R_QUES_D, ['western', 'education', 'policy'], required_words=['western','policy'])
    response(long.R_QUES_E, ['difference','comparison','between','western','indian','policy'], required_words=['education','policy','western','indian'])
    response(long.R_QUES_F, ['literacy','rate','from','last','years','india'], required_words=['literacy','rate','india','last'])
    response(long.R_QUES_G, ['current','literacy','rate','india'], required_words=['literacy','rate','india'])
    response(long.R_QUES_H, ['types','education','india'],required_words=['types'])
    response(long.R_QUES_I, ['benefits','benefits','advantages','advantage','merit','merits','need'], single_response=True)
    response(long.R_QUES_J, ['some','tips','study','effectively','suggest'], required_words=['tips'])
    response(long.R_QUES_K, ['how','education','brings','change','everyone','everybody','everybody\'s','life'], required_words=['change','life'])
    response(long.R_QUES_L, ['how','education','helps','life','long'], required_words=['helps'])
    response(long.R_QUES_M, ['education','for','children','with','special','needs','cwsn'],required_words=['special','needs'])
    response(long.R_QUES_N, ['types','type','education','online','offline','better','difference','vs'],required_words=['online','offline'])
    response(long.R_QUES_O, ['online','classes','education','virtual','class'], required_words=['online'])
    response(long.R_QUES_P, ['offline','classes','class','education'], required_words=['offline'])
    response(long.R_QUES_Q, ['why','education','important','essential','rural','parts','india'], required_words=['rural','why','important'])
    response(long.R_QUES_Q, ['why','education','important','essential','rural','parts','india'], required_words=['rural','why','essential'])
    response(long.R_QUES_R, ['which','more','important','moral','academic','education','vs'],required_words=['moral','academics'])
    response(long.R_QUES_S, ['what','moral','education'], required_words=['what','moral'])
    response(long.R_QUES_T, ['what','academic','academics','education'], required_words=['what','academic'])
    response(long.R_QUES_U, ['how','education','makes','person'], required_words=['how','makes','person'])
    response(long.R_QUES_V, ['how','education','self','reliant','reliance','dependent'],required_words=['self'])
    response(long.R_QUES_W, ['difference','between','education','knowledge','differentiate'],required_words=['knowledge','education'])
    response(long.R_QUES_X, ['sii','portal'],required_words=['sii','portal'])
    response(long.R_QUES_Y, ['yuva','sangam','registration','portal'], required_words=['yuva','sangam','registration','portal'])
    response(long.R_QUES_Z, ['what','benefits','advantages','online','classes'],required_words=['what','online','classes'])
    response(long.R_QUES_AA, ['can','you','recommend','some','eductional','education','teaching','website','learning','app'], required_words=['recommend'])

    if not highest_prob_list:
        best_match = ""
        best_score: int = 0
    else:
        best_match = max(highest_prob_list, key=lambda k: highest_prob_list[k])
        best_score = highest_prob_list[best_match]

    # If no good match, try Wikipedia
    if best_score < 1:
        try:
            # Join the message to form a query
            query = ' '.join(message)
            summary = wikipedia.summary(query, sentences=2)
            return summary
        except Exception as e:
            # If Wikipedia fails, provide a Google search link
            google_url = f"https://www.google.com/search?q={'%20'.join(message)}"
            return f"Sorry, I couldn't find an answer to your question on Wikipedia. You can try searching on Google: {google_url}"
    return best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
if __name__ == '__main__':
    while True:
        print('Bot: ' + get_response(input('You: ')))
