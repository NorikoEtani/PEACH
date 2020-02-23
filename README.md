# PEACH
作成日：2020年2月23日

作成者：江谷典子

電子メール：kerotan@kcn.ne.jp


【準備】

社団法人情報処理学会のデジタルプラクティス報告「オープンソースによるTwitter検索およびデータ可視化の方法」を読んで必要なライブラリやモジュールをインストールし，プログラムを御利用ください．

情報処理学会情報学広場URL　https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=202959&item_no=1&page_id=13&block_id=8

【目的】

SNS Twitter情報分析を行い、Peach号が離陸・着陸する空港周囲の話題(トレンド）を可視化するためにPythonを使ったツールを前述を参考にして再構築を行った。その使い方について説明を行い、「観光」「コロナウイルス」を事例とした分析結果を記載した資料を提示する。

【開発環境】

　筆者の開発環境は下記の通りである．
 
・Windowsのエディション：Windows 10 Home

・システムの種類：64ビットオペレーティングシステム

・Java version 9

・Python 3.5.2 /Anaconda 4.1.1 (64-bit)

・日本語形態素解析MeCab 0.996

【提供するプログラム】

・PEACH.txt		Peach号の利用空港名リスト

・geo_peach.txt		Peach号の利用空港緯度経度リスト 

・peach_airport.html	Peach号の利用空港地図

・ja_geodata.py　	Peach号の利用空港名リストから帰港空港の緯度経度を取得し（geo_peach.txt出力）地図マーカー（peach_airport.html）を表示

・search_tweet.py	各利用空港周辺TwitterのデータをTwitter APIを利用して取得（空港名_tweet.txt出力）

・ja_rank_tweet.py　	日本語形態素解析から名詞の単語を抽出し単語の出現頻度リストを作成

・ja_wordcloud.py　	日本語形態素解析から名詞の単語を抽出しWord Cloudで単語の出現頻度を可視化

・IPAfont00303\ipag.ttf　Word Cloudで表示するフォント

【提供する資料】

・MANUAL		Twitter情報分析　空港周辺のトレンド分析

・SAMPLE1_Tourism	Sunarnabhumi Airport（タイ）周囲の検索キーワード「観光」の場合、WordCloudおよび名詞出現頻度リスト例

・SAMPLE2_Coronavirus	Sunarnabhumi Airport（タイ）周囲の検索キーワード「コロナウィルス」の場合、WordCloudおよび名詞出現頻度リスト例

以上
