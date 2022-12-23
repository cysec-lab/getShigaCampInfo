#dom: 入力, ver: 出力 配列に入れ直す → [[domain, version], [domain, version]]
import main
import csv
import json

def get_vlun_by_list(version):
    p = open('wordpresses.json','r')
    json_dict = json.load(p)
    #print('json_dict:{}'.format(type(json_dict)))
    try:
        vuln_data=json_dict[version]['vulnerabilities']
        print(version+"では登録された脆弱性情報が発見されました")
        #print(vuln_data)
        return vuln_data
    except:
        print('指定されたversionの脆弱性情報はありません')
        return None



    #json_str = '''
#{
    #"test":"json",
    #"test2":"json2"
#}
#'''

    #json_dict = json.loads(json_str)
    #print('json_dict:{}'.format(type(json_dict)))

    #vlun_list=バージョンを与えた時の脆弱性一覧

    vlun_list = json_dict
    return vlun_list

def get_domain_by_url(url):
    from urllib.parse import urlparse
    parse = urlparse(url)
    domain = parse.netloc
    return domain

def read_version_by_file():
    with open('output.csv','r') as f:
        d_reader = csv.reader(f)
        for row in d_reader:
            ret_json=get_vlun_by_list(row[1])
            print(get_domain_by_url(row[0])+":"+str(ret_json))

if __name__ == '__main__':
    read_version_by_file()
    while True:
        s = input('\n調べたいversionの値を入力してください: ')
        s = s.strip() #空白文字のみの入力は無視する
        if s != '':
            print('\nversion {s} を調べます')
            break
    get_vlun_by_list(s) 

#if s == 

