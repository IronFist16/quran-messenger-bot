# bot.logic.py

import alfanous

def answer(query):
    limit = 3
    response = alfanous.do(flags={"action":"search", "query":query, "unit": "aya", "fuzzy":True, "highlight": "none", "limit": limit})
    print query.encode('utf-8')
    print response["error"]
    reply=""
    if (not response["error"]["code"]):
        for i in xrange(1,  min(limit+1, response["search"]["interval"]["total"]+1)):
             reply += "{" + response["search"]["ayas"][i]["identifier"]["sura_arabic_name"] + " "+ str(response["search"]["ayas"][i]["identifier"]["aya_id"]) + "}"
             reply += "\n"+ response["search"]["ayas"][i]["aya"]["text"]
             reply += "\n\n"
    return reply

LOGIC_RESPONSES = {
    "thank": [
         "Of course!",
        "Anytime!",
        "You're welcome",
         "You are so welcome!"
    ],
    "thanks": [
        "Of course!",
        "Anytime!",
        "You're welcome",
         "You are so welcome!"
    ],
    'help': [
        "A good place to get help is by going to our forums on http://joincfe.com/ask/",
        "You can always ask questions in our videos or on http://joincfe.com/ask/"
    ],
    'code': [
        "Have you considered looking at our code on http://joincfe.com/github/? That might help you",
        "We don't review code at this time, but you can consider looking at our open-source repo http://joincfe.com/github/"
    ],
}