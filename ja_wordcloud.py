import MeCab
import matplotlib.pyplot as plt
import csv
from wordcloud import WordCloud

def analyze_tweet_text(datafile):
    #読込むファイル名を設定
    fname = r"'"+ datafile+ "'"
    fname = fname.replace("'","")

    with open(fname, 'r',encoding="utf-8") as f:
       reader = f.readline()
       #UnicodeEncodeErrorを避けるため
       s = reader.encode('cp932', "ignore")
       reader_after = s.decode('cp932')

       while reader_after:
             #print(reader_after)
             ap = reader_after.strip()
             #読込むファイル名を設定
             ap_fname = r"'"+ ap + "_tweet.txt" + "'"
             ap_fname = ap_fname.replace("'","")

             out_wordcloud(ap_fname,ap)

             reader = f.readline()
             #UnicodeEncodeErrorを避けるため
             s = reader.encode('cp932', "ignore")
             reader_after = s.decode('cp932')
             #print(reader_after)


def out_wordcloud(tweet_file,ap_name):
    #読込むファイル名を設定
    t_fname = r"'"+ tweet_file + "'"
    t_fname = t_fname.replace("'","")

    #Mecabを使用して、形態素解析
    mecab = MeCab.Tagger("-Ochasen")

    #"名詞", "動詞", "形容詞", "副詞"を格納するリスト
    words=[]

    #ファイルを読込み
    with open(t_fname, 'r',encoding="utf-8") as f1:

        reader = f1.readline()

        while reader:
            #Mecabで形態素解析を行う
            node = mecab.parseToNode(reader)

            while node:
                word_type = node.feature.split(",")[0]

                #取得する単語は、"名詞", "動詞", "形容詞", "副詞"
                #if word_type in ["名詞", "動詞", "形容詞", "副詞"]:
                if word_type in ["名詞"]:

                    words.append(node.surface)

                node = node.next

            reader = f1.readline()

    #wordcloudで出力するフォントを指定
    font_path = r"C:\Users\NORIKO\Desktop\SNS情報分析\PROC\IPAfont00303\ipag.ttf"

    txt = " ".join(words)

    if not txt:
       return

    stop_words = [ 'https','*','-','#','@']

    #解析した単語、ストップワードを設定、背景の色は黒にしてます
    wordcloud = WordCloud(background_color="black",font_path=font_path, stopwords=set(stop_words),
        width=800,height=600).generate(txt)

    imgfile = ap_name+".png"
    wordcloud.to_file(imgfile)
    #plt.imshow(wordcloud)
    #plt.axis("off")
    #plt.show()
    return


if __name__ == '__main__':
    #Peach帰港空港名ファイル名入力
    print ('====== Enter Peach Airport file =====')
    datafile = input('>  ')

    analyze_tweet_text(datafile)
