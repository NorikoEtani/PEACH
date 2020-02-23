# -*- coding:utf-8 -*-  
from requests_oauthlib import OAuth1Session
import json
                                                                                                                                                  
oath_key_dict = {
    "consumer_key": "8TKebUW9PSm5yMtCrQF9dM7H0",
    "consumer_secret": "3GzoLxTgEYSMVVCnY0pSdhaZlRaBghaqoceN0AZ0XYlEiunjRk",
    "access_token": "725947432631033856-QHkFkYaSxWyXLCH0vPtJUWgKSCtxn9p",
    "access_token_secret": "WNUU9028nX60nG2zhNZnVdU4kA76MyecNiddTjZEWbarh"
}

def searchtweet(geofile,searchstr,strlang,apdist):
  #読込むファイル名を設定
  geo_fname = r"'"+ geofile + "'"
  geo_fname = geo_fname.replace("'","")

  with open(geo_fname, 'r',encoding="utf-8") as f:
       reader = f.readline()
       #UnicodeEncodeErrorを避けるため
       s = reader.encode('cp932', "ignore")
       reader_after = s.decode('cp932')
       #print(reader_after)
       while reader_after:
             d = reader_after.split(",")
             fname = d[0].strip()
             latitude = d[1].strip()
             longtude = d[2].strip()
             tweets = tweet_search(searchstr,strlang,str(latitude),str(longtude),str(apdist),oath_key_dict)
 
             out_tweets(tweets,fname)

             reader = f.readline()
             #UnicodeEncodeErrorを避けるため
             s = reader.encode('cp932', "ignore")
             reader_after = s.decode('cp932')
             #print(reader_after)
  return

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word,str_lang,latitude,longtude,ap_dist,oath_key_dict):
    #print(search_word)
    #print(str_lang)
    #print(latitude)
    #print(longtude)
    #print(ap_dist)

    if not str_lang:
       str_lang = "ja"
    if not ap_dist:
       ap_dist = "7"
    ap_dist = ap_dist+"mi"

    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word,
	"geocode": "\""+latitude+","+longtude+","+ap_dist+"\"",
	#"geocode": "42.786787000000004,141.68293158837253,7mi",
        "lang": str_lang,
        "result_type": "recent",
        "count": "100"
        }

    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print ("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

def out_tweets(get_tweets,airport_fname):
    #出力ファイル名
    fname = r"'"+ airport_fname+"_tweet.txt"+ "'"
    fname = fname.replace("'","")
    #print(fname)
    #ファイルへ出力
    with open(fname, "w",encoding="utf-8") as f1:
      for tweet in get_tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']

        f1.write('\n')
        f1.write(tweet_id)
        f1.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_text = text.encode('cp932', "ignore")
        after_text = before_text.decode('cp932')
        f1.write(after_text)
        f1.write('\n')

        f1.write(created_at)
        f1.write('\n')
        f1.write(user_id)
        f1.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_user = user_description.encode('cp932', "ignore")
        after_user = before_user.decode('cp932')
        f1.write(after_user)
        f1.write('\n')

        f1.write(screen_name)
        f1.write('\n')

        #UnicodeEncodeErrorを避けるため
        before_uname = user_name.encode('cp932', "ignore")
        after_uname = before_uname.decode('cp932')
        f1.write(after_uname)
        f1.write('\n')
    return

if __name__ == '__main__':
    #Peach帰港空港GEOデータファイル名入力
    print ('====== Enter Peach Airport Geodata file =====')
    geofile = input('>  ')

    #検索キーワードを入力
    print ('====== Enter Search String   =====')
    searchstr = input('>  ')
    #検索言語を入力
    print ('====== Enter Search Languate (ja: Japanese, en: English)   =====')
    strlang = input('>  ')
    #空港からの距離 (mile)を入力
    print ('====== Enter Disctance from Airport (unit: mile)    =====')
    apdist = input('>  ')

    searchtweet(geofile,searchstr,strlang,apdist)

