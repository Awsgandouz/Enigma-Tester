import os 
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.reddit.com/r/programming/'
response=requests.get(url,headers=headers)


soup=BeautifulSoup(response.content,'lxml')

#print(soup.select('.Post')[0].get_text())
result = open("webscraped.txt",'w')
for item in soup.select('.Post'):
    separator = "---------------------------------- \n"
    num = item.select("._1rZYMD_4xY3gRcSS3p8ODO")[0].get_text()
    title = item.select("._eYtD2XCVieq6emjKBH3m")[0].get_text()
    result.writelines([separator, num, '\n', title, '\n'])

result.close()
    