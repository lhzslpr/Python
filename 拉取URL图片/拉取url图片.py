# coding: utf8
import requests
import time
def download_img(img_url, api_token,index):
    print ('+'+img_url+'+')
    header = {"Authorization": "Bearer " + api_token} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get(img_url, headers=header, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        savePath = 'D:\\test\\img' + str(index) + '.png'
        open(savePath, 'wb').write(r.content) # 将内容写入图片
        print("done")
    del r

if __name__ == '__main__':
    file = open("headurl.txt")
    i = 1
    while 1:
        line = file.readline()
        api_token = ""
        download_img( line.strip(), api_token, i )
        i = i + 1
        time.sleep(1)
        if not line:
            break
        pass # do something