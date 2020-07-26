import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'

cookie = {'Cookie': 'uuid_n_v=v1; uuid=7EF4B5C0CF1911EAAACFDFD33042EC97425A2CA30C9547CB98447AEDE43CFD48; _csrf=0409f6ff13e107d2616ba92875ce3c94883833d6ddd2b65ad7984f83eebd3124; _lxsdk_cuid=1738a39ada0f-0a07f7a6431399-4353761-144000-1738a39ada1c8; _lxsdk=7EF4B5C0CF1911EAAACFDFD33042EC97425A2CA30C9547CB98447AEDE43CFD48; mojo-uuid=3c062c605d677105a169adeba286cdd4; mojo-session-id={"id":"f46ba62122b6541720331a8a412ca8b1","time":1595754781337}; mojo-trace-id=2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595751957,1595752200,1595754781,1595754784; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595754784; __mta=144954891.1595751904631.1595754781679.1595754784102.10; _lxsdk_s=1738a6599e1-2b8-6c2-cb5%7C%7C4'}

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header, cookies=cookie)

bs_info = bs(response.text, 'html.parser')	

movie_list = bs_info.find_all('div', attrs={'class': 'movie-hover-info'})

mytarget = []

#获取前10个电影
for i in range(10):
   
    #获取电影名称
    movie_name = movie_list[i].find('span',attrs={'class': 'name'}).text
    #print(movie_name)

    #获取电影类型
    movie_first_div = movie_list[i].find('div')
    movie_second_div = movie_first_div.find_next('div')
    movie_second_div_text = movie_first_div.find_next('div').text
    movie_type = str(movie_second_div_text).strip()
    #print(movie_type)

    #获取电影上映时间
    movie_third_div = movie_second_div.find_next('div')
    movie_fourth_div = movie_first_div.find_next('div')
    movie_fourth_div_text = movie_third_div.find_next('div').text
    movie_start_time = str(movie_fourth_div_text).strip()
    #print(movie_start_time)

    movie_data_list=[movie_name,movie_type,movie_start_time]
    mytarget.append(movie_data_list)

#保存数据到文件
maoyan_top10_file = pd.DataFrame(data = mytarget)
maoyan_top10_file.to_csv(r'D:\pytest\Python-002\week01\homework_1\maoyantop10.csv', encoding='utf-8', index=False, header=False)



