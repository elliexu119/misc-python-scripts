# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 07:51:10 2020

@author: ellix
"""


from twitterscraper import query_tweets
from datetime import date, timedelta
import pandas as pd
from textblob import TextBlob
import en_core_web_sm
import matplotlib.pyplot as plt

search = 'oil'
minretweet = 1
bundle = 2
subject = 'oil' #one word max
upuntilthisdayago = 30 
occurance = 0

def mostcommonwords(startDate, endDate):
    global minretweet
    global occurance
        
    common = []
    a = "think over best going retweet you’re go only right see need most why someone go make time don't down very find great against any" 
    a = a + " the to of is a in at for that this i have & it has us and on in as … an - also be with by you he she my if but are am his her"
    a = a + " our just like does me your you're so their was where what we been who they from about people all when no do or not some i’m would"
    a = a + " will him were even how being know it’s one said more get back can got that’s up says it's still don’t had because never another now after out new"
    a = a + " want these into every too let may both days 8 please real them made making thread did doing , total complete everyone can't first media good"
    a = a + " he’s she’s 1 last tried tonight today tomorrow yesterday can’t than then way friends put say you, u i'm until while take should really there"
    a = a + " call give during could 2 cnn support white fbi use day night always better which own different many seen use million follow"
    a = a + " small other state gonna didn’t top state house those tell states tag tests inside come ever used keep black come briefing let’s nobody name before asked"
    a = a + " look go: he's " + '"it\'s line comes like, things'
    
    for b in a.split(): 
        if (b in common) is False: 
            common.append(b)
    
    words = []
    tid = [] 
    for tweet in query_tweets("min_retweets:" + str(minretweet) + " lang:en", 100, begindate = date.today() - timedelta(days=endDate), enddate = date.today() - timedelta(days=startDate)):
        if (tweet.tweet_id in tid) == False: 
            tw = tweet.text
            print (tw)
            print ('retweets: ', tweet.retweets)
            print ('')
            if ('trump' in tw.lower() and 'love' in tw.lower()): 
                occurance += 1
            for line in tw.split(): 
                if (line.lower() in common) == False: 
                    for i in range (0, int(tweet.retweets/2)):
                        words.append(line.lower())
    
    from collections import Counter
    Counter= Counter (words)
    most_occur = Counter.most_common(20) 
    return (most_occur)


def sentimentAnalysis():
    global search
    global minretweet
    global bundle 
    global subject  #one word max
    global upuntilthisdayago
    nlp = en_core_web_sm.load()
    
    sentiment = []
    sentimentTime = []
    
    
    for day in range (bundle, upuntilthisdayago, bundle):
        score = []
        tid = [] 
        day2 = day - bundle
        for tweet in query_tweets("(" + search + ") min_retweets:" + str(minretweet) + " lang:en", 100, begindate = date.today() - timedelta(days=day), enddate = date.today() - timedelta(days=day2)):
            if (tweet.tweet_id in tid) == False: 
                tw = tweet.text
                #print (tw)
                doc = nlp(tw)
                sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
                li = [] 
                for i in sub_toks: 
                    li.append(i.text.lower())
                #print (li)
                if (subject in li) == True: 
                    print(li)
                    print(tw)
                    print (TextBlob(tw).sentiment)
                    print(tweet.timestamp)
                    print('retweets:', tweet.retweets)
                    
                    textblob = TextBlob(str(tw))
                    score.append(textblob.sentiment.subjectivity * textblob.sentiment.polarity * tweet.likes)
                    tid.append(tweet.tweet_id)
        
        sentiment.append(sum(score)) 
        sentimentTime.append(date.today() - timedelta(days=day))
    
    dataframe = pd.DataFrame ()
    dataframe['sentiment'] = sentiment
    dataframe['time'] = sentimentTime
    ax = dataframe.plot(title = subject, y = 'sentiment', x = 'time')
    ax.get_legend().remove()	
    plt.show()
    
print (mostcommonwords(0, 30))
#sentimentAnalysis()
