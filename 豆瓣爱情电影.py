import requests
import json
import pandas as pd

if __name__ == '__main__':
    # 用来爬取豆瓣的电影数据

    url = 'https://movie.douban.com/j/chart/top_list'

    page_all = [461,482,482,482,482,482,482,482,482,460]
    name_all = ['90-100','80-90','70-80','60-70','50-60','40-50','30-40','20-30','10-20','0-10']
    interval_all = ['100:90','90:80','80:70','70:60','60:50','50:40','40:30','30:20','20:10','10:0']
    for i in range(0,10):
        name = name_all[i]

        # page = page_all[i]
        # interval_id = interval_all[i]
        # for num in range(0,page,20):
        #     param = {
        #         'type': '13',
        #         'interval_id': interval_id,
        #         'action':'',
        #         'start': str(num),#从库中的第几部电影开始
        #         'limit': '20'#每一次从电影库中取出多少电影
        #     }
        #
        #     header = {
        #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        #     }
        #
        #     response = requests.get(url,headers=header,params=param)
        #
        #     list_data = response.json()
        #
        #     fp = open(f'./爱情{name}_.json','a',encoding='utf-8',newline='\n')
        #
        #     json.dump(list_data,fp=fp,ensure_ascii=False,indent=1)
        #
        #     print(i,"bravo",num)

        # 下面的用来转换成excel文件

        with open(f'爱情{name}_.json', "r", encoding='utf-8') as f:
            data = json.load(f)
            print(data)
        data = pd.DataFrame(data)
        data.to_excel(f'./xlsx/{i}.xlsx', sheet_name="60-70",index=1)
        #
        #











