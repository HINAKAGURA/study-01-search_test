
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# CSVファイル読み込み
path = "member.csv"
with open(path,mode="r") as f:
    for mem in f:
        source.append(mem.replace("\n",""))


### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    if word in source:

        print("{}が見つかりました".format(word))
    else:
        print("{}はリストにありません。追加します".format(word))
        source.append(word)
        
    #登場人物リスト（更新版）を出力
    path_new="new_member.csv"
    with open(path_new,mode="w") as f:
        for mem in source:
            f.write(mem + "\n")


if __name__ == "__main__":
    search()