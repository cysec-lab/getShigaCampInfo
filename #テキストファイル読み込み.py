#テキストファイル読み込み

f = open('myfile.txt', 'r')
#f = open('myfile.txt', 'r', encoding='UTF-8')  #文字エンコーディングを指定
data = f.read()
print(data)
f.close()
