import tweepy
import csv
import json

Api_key = "YcCsRItAYm1tldfKkqQAhiQDJ"
Api_Key_Secret = "WGLUztelCcrSEZ9uZrjbs2V1tSEqbw9njwpMcB3Ps8TD8qjWRd"

access_token = ""
access_token_secret = ""


bearer_token = "AAAAAAAAAAAAAAAAAAAAAN8uVwEAAAAAYlItIumLjjY%2BVm5saopuf1joxV4%3DdYGUA87Bq8cuTvTpzTazukR9zsHtjXiudQp5pCXUCKCpirfOdy"

def addTweet(dicc,id,text):
    if(id not in dicc):
            dicc[id]=text

# Ver el formato del objeto STATUS en:
# https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2

def get_tweets():
    dicc = {}
    auth = tweepy.OAuthHandler(Api_key, Api_Key_Secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) #wait on rate limit hara que el programa no se pare
    for tweet in tweepy.Cursor(api.search, q="LassoGuillermo lo mejor para Ecuador",tweet_mode="extended").items(250):
        try:
            jsonRetweet = tweet.retweeted_status
            id = jsonRetweet.id
            full_text = jsonRetweet.full_text
            addTweet(dicc,id,full_text)

        except:
            id = tweet.id
            full_text = tweet.full_text

            addTweet(dicc,id,full_text)

    return dicc


def saveData():
    dicc = get_tweets()
    out_file_name = 'dataSetPositivos.csv'

    csv_headers = ["idTweet","fullText","Polaridad"]
    with open(out_file_name, mode='a',encoding= "utf-8") as f:
        writer = csv.writer(f)
        #writer.writerow(csv_headers)  # escribe la primera fila nuests crear el archivo de texto ros csv headers

        for tweet in dicc:
            row = [tweet,dicc[tweet]]
            writer.writerow(row)

saveData()

                    
