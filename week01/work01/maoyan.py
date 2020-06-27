import requests
from bs4 import BeautifulSoup
from pandas import Series,DataFrame

myurl = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = '__mta=20772231.1593228884903.1593274213288.1593275388851.17; uuid_n_v=v1; uuid=22CD0BC0B82711EAB11C23537EB4C64B91CA02A08C2F473099979BC798B983AC; _csrf=3b41953afdec6550bebd74460ee1d6caa818f68ab419066ccbe42c2366581c7c; mojo-uuid=394811f1852aa598af73ce8573afc1b1; _lxsdk_cuid=172f3d77ad0c8-0591040d17b9bd-31627403-1aeaa0-172f3d77ad0c8; _lxsdk=22CD0BC0B82711EAB11C23537EB4C64B91CA02A08C2F473099979BC798B983AC; mojo-session-id={"id":"4f355f7d5bb70da60815cd3ae74ca771","time":1593273094622}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593228885,1593275442; mojo-trace-id=31; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593275444; __mta=20772231.1593228884903.1593275388851.1593275448906.18; _lxsdk_s=172f67a1639-c21-f7c-084%7C%7C53'
header = {'User-Agent':user_agent,'Cookie':cookie}

response = requests.get(myurl,headers=header)
html_info = BeautifulSoup(response.text,'html.parser')
n = 0
file_names=[]
file_types=[]
file_dates=[]
for tags in html_info.find_all('div',attrs={'class':'movie-hover-info'}):
    if n < 10:
        atags =  tags.find_all('div',attrs={'class':'movie-hover-title'})
        file_name = atags[0].find_all('span')[0].text
        file_type = atags[1].get_text().replace(" ", "").replace("\n", "").split(':')[1]
        file_date = atags[3].get_text().replace(" ", "").replace("\n", "").split(':')[1]
        file_names.append(file_name)
        file_types.append(file_type)
        file_dates.append(file_date)
    n = n+1

all_list = {'电影名称':file_names,'电影类型':file_types,'上映时间':file_dates}
print(all_list)
maoyan_movies = DataFrame(all_list,columns=['电影名称','电影类型','上映时间'])
maoyan_movies.to_csv('./maoyan-work1.csv',encoding='utf-8',index=False,header=False)