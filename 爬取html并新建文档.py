import urllib.error
from urllib.request import *
import time

def create_text(content):
    file_path = "新文件" + text_name + ".txt"
    with open(file_path,"w",encoding='utf-8') as file:
        file.write(content)

#程序开始执行
if __name__ == '__main__':
    url = "https://"+input("请输入您想爬取的网站url：")
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    a = []
    try:
        #获取html超文本数据
        request = Request(url=url, headers=headers)
        respond = urlopen(request)
        content = respond.read().decode('utf-8')
    except urllib.error.HTTPError:
        print("出现http类错误")
        a.append(1)
    except urllib.error.URLError:
        print("出现url类错误")
        a.append(2)
    finally:
        if len(a) != 0:
            print("出现错误，所以程序停止运行")
            time.sleep(2)
        else:
            input_time = 1
            while input_time <=10:
                whether = input("html代码已爬取完毕，请问是否创建文档：（输入是或否）：")
                if whether == "是":
                    text_name = input("给你的文件起个名字吧！：")
                    create_text(content)
                    print("您的文档已创建完毕")
                    time.sleep(2)
                    break
                elif whether == "否":
                    print("再见")
                    time.sleep(2)
                    break
                else:
                    print("您的代码有误，请再输一遍")
                    input_time += 1
                    if input_time == 11:
                        print("尝试次数超过10次，程序终止运行")
                        time.sleep(2)
                        break
                    else:
                        continue
