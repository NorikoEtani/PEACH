# -*- coding:utf-8 -*-
import folium
import geocoder


def get_geodata(dfile,geofile,outfile):
    # 地図の基準として兵庫県明石市を設定
    japan_location = [35, 135]

    # 基準地点と初期の倍率を指定し、地図を作成する
    map = folium.Map(location=japan_location, zoom_start=4)

    #読込むファイル名を設定
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #読込むファイル名を設定
    geo_fname = r"'"+ geofile + "'"
    geo_fname = geo_fname.replace("'","")

    #Mecabを使用して、形態素解析
    #mecab = MeCab.Tagger("-Ochasen")

    #"名詞", "動詞", "形容詞", "副詞"を格納するリスト
    words=[]
 
    #ファイルを読込みんで緯度経度出力
    with open(fname, 'r',encoding="utf-8") as f:
         reader = f.readline()

         #UnicodeEncodeErrorを避けるため
         s = reader.encode('cp932', "ignore")
         reader_after = s.decode('cp932')

         #print(reader_after)
         while reader_after:
                ret = geocoder.osm(reader_after, timeout=5.0)
                if ret.ok != False:
                   s_add = ret.address.encode('cp932', "ignore")
                   add_after = s_add.decode('cp932')
                   #print(reader_after)
                   #print(ret.latlng[0])
                   #print(ret.latlng[1])
                   latitude = ret.latlng[0]
                   longtude = ret.latlng[1]
                   name = reader_after.strip()
                   folium.Marker(location=[latitude, longtude], popup=name).add_to(map)
                   
                reader = f.readline()
                #UnicodeEncodeErrorを避けるため
                s = reader.encode('cp932', "ignore")
                reader_after = s.decode('cp932')
                #print(reader_after)

                with open(geo_fname, 'a',encoding="utf-8") as f2:
                     f2.writelines(name+","+str(latitude)+","+str(longtude)+"\n")


# 地図表示
    #出力ファイル名
    fname = r"'"+ outfile + "'"
    fname = fname.replace("'","")
    map.save(fname)
    #map.save('kyoto.html')

if __name__ == '__main__':
    #Peach帰港空港名ファイル名入力
    print ('====== Enter Peach Airport file =====')
    dfile = input('>  ')

    #Peach帰港空港GEOデータファイル名入力
    print ('====== Enter Peach Airport Geodata file =====')
    geofile = input('>  ')

    #地図htmlファイル名（出力）を入力
    print ('====== Enter Peach Airport HTML file =====')
    outfile = input('>  ')

    get_geodata(dfile,geofile,outfile)


