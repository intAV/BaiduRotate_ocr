from urllib.parse import unquote
import requests
import execjs
import time
import json
import re
import urllib3
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class BaiduRotate:

    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, '
                      '*/*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://wappass.baidu.com/static/captcha/tuxing.html?ak=2ef521ec36290baed33d66de9b16f625&backurl=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E5%25A9%259A%25E5%25A7%25BB%26ie%3Dutf-8%26pn%3D3900&timestamp=1676562481&signature=db40e5143d0645f18009524380a49b8e',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

    def get_image_request_data(self):
        """
        :return: 获取需要获取图片的参数
        """
        url = "https://wappass.baidu.com/viewlog"
        params = {
            "callback": "jQuery110205449684422426735_" + str(int(time.time() * 1000)),
            "ak": "2ef521ec36290baed33d66de9b16f625",
            "_": str(int(time.time() * 1000))
        }
        response = self.session.get(url, headers=self.headers, params=params)
        res_data = re.findall(r'.*?(\{.*?})\)', response.text)[0]
        res_data = json.loads(res_data)
        item = {
            "tk": res_data['data']['tk'],
            "as": res_data['data']['as'],
            "ds": res_data['data']['ds']
        }
        #print(item)
        return item

    #获取图片url地址
    def get_img(self, item):
        url = "https://wappass.baidu.com/viewlog/getstyle"
        params = {
            "callback": "jQuery110205449684422426735_" + str(time.time() * 1000),
            "ak": '2ef521ec36290baed33d66de9b16f625',
            "tk": item["tk"],
            "isios": "0",
            "type": "spin",
            "_": str(time.time() * 1000)
        }
        response = self.session.get(url, headers=self.headers, params=params)
        ret_data = re.findall(r'.*?(\{.*?})\)', response.text)[0]
        ret_data = json.loads(ret_data)
        item_img = {
            "img_url": unquote(ret_data['data']['ext']['img']),
            "backstr": ret_data['data']['backstr'],
            "tk": item["tk"],
            "as": item["as"]
        }
        response = self.session.get(item_img['img_url'], verify=False)
        with open('img.png', 'wb')as f:
            f.write(response.content)
        return item_img

    # 图片旋转度数--关键
    def fun_get_angle(self,img_url):
        # print(img_url)
        res = requests.get(url=img_url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        data = {
            "img": base64.b64encode(res.content).decode("utf-8"),
            "project_name": "旋转(百度贴吧)",
            "show": "True",
        }
        try:
            text = requests.post(url="http://121.4.108.95:8000/%E6%B5%8B%E8%AF%95/", data=data, headers=headers,
                                 timeout=5)
        except:
            print("远程识别验证码失败! url:http://121.4.108.95:8000/")
            return 0
        detail = json.loads(text.text).get('detail')
        print("旋转度数:", detail)
        return detail


    def verify_data(self, item):
        url = "https://wappass.baidu.com/viewlog"
        print("angle：", item['angle'])
        print("as：", item['as'])
        with open('get_encrypt.js', 'r', encoding='utf-8') as f:
            js_text = f.read()
        #print(js_text)
        fs = execjs.compile(js_text).call('encrypt_', str(item['angle']), str(item['as']), str(item['backstr']))
        #print("fs：", fs)
        params = {
            "callback": "jQuery110204100787474351779_" + str(time.time() * 1000),
            "ak": "2ef521ec36290baed33d66de9b16f625",
            "as": item['as'],
            "fs": fs[0],
            "tk": item['tk'],
            "cv": "submit",
            "_": str(time.time() * 1000)
        }
        response = self.session.get(url, headers=self.headers, params=params)
        print(response.headers.get("cookies"))
        ret_data = re.findall(r'.*?(\{.*?})\)', response.text)[0]
        ret_data = json.loads(ret_data)
        print("验证结果：", ret_data)
        return ret_data






if __name__ == '__main__':
    item = BaiduRotate().get_image_request_data()
    item_img = BaiduRotate().get_img(item)
    angle = BaiduRotate().fun_get_angle(item_img.get('img_url'))
    item_img['angle'] = angle
    #print(item_img)
    ret_data = BaiduRotate().verify_data(item_img)
    #print(ret_data)
    if 1 == ret_data['data']['op']:
        print("验证通过...")
    else:
        print("验证未通过...")
