import re
import requests
import time
import sys

sess = requests.Session()
# sess.verify = False
sess.headers = {
    "User-Agent": "miniProgram",
    "X-Requested-With": "XMLHttpRequest"
}

def login(name, stuid, id):
    login_url = "http://jstxcj.91job.org.cn/passport/verify?v=release"
    login_html = sess.get(login_url).text
    login_data = {
        "_front_csrf": re.search(r'name="_front_csrf" value="(.+?)"', login_html).group(1),
        "name": name,
        "no": stuid,
        "id_number": id
    }
    login_res = sess.post(login_url, login_data)
    login_json = login_res.json()
    if login_json["type"] != "success":
        raise Exception(login_json["message"])
    enter_url = "http://jstxcj.91job.org.cn" + login_json["url"]
    enter_html = sess.get(enter_url).text
    enter_data = {
        "_front_csrf": re.search(r'name="_front_csrf" value="(.+?)"', enter_html).group(1),
        "StudentLoginForm[phone]": re.search(r'value="(.+?)"  name="StudentLoginForm\[phone\]"', enter_html).group(1)
    }
    enter_res = sess.post(enter_url, enter_data)
    token_url = "http://jstxcj.91job.org.cn/site/pact"
    token_html = sess.get(token_url).text
    sess.headers["token"] = re.search(r"'/pages/selector/selector\?token=' \+ '(.+?)'", token_html).group(1)

def upload(filename):
    cur_time = int(time.time() * 1000)
    upload_url = "https://jstxcj.91job.org.cn/wechat/camera/upload"
    sess.headers["Content-Type"] = f"multipart/form-data; boundary={cur_time}"
    upload_data = f"--{cur_time}".encode("utf-8") \
                + '\r\nContent-Disposition: form-data; name="file"; filename="tmp.jpg"\r\nContent-Type: image/jpeg\r\n\r\n'.encode("utf-8") \
                + open(filename, "rb").read() \
                + f"\r\n\r\n--{cur_time}--\r\n\r\n".encode("utf-8")
    upload_res = sess.post(upload_url, upload_data)
    upload_json = upload_res.json()
    if upload_json["type"] != "success":
        raise Exception(upload_json["message"])
    print("camera/upload: \u56fe\u7247\u4e0a\u4f20\u6210\u529f")
    chklv_url = "https://jstxcj.91job.org.cn/wechat/camera/check-living"
    sess.headers["Content-Type"] = "application/x-www-form-urlencoded"
    chklv_res = sess.get(chklv_url)
    chklv_json = chklv_res.json()
    if chklv_json["type"] != "success":
        raise Exception(chklv_json["message"])
    print("camera/check-living: \u6d3b\u4f53\u68c0\u6d4b\u901a\u8fc7")
    crop_url = "https://jstxcj.91job.org.cn/wechat/camera/crop"
    crop_res = sess.get(crop_url)
    crop_json = crop_res.json()
    if crop_json["type"] != "success":
        raise Exception(crop_json["message"])
    print("camera/crop: " + (crop_json["message"] or "\u56fe\u7247\u88c1\u5207\u6210\u529f"))
    check_url = "https://jstxcj.91job.org.cn/wechat/camera/check"
    check_res = sess.get(check_url)
    check_json = check_res.json()
    if check_json["type"] != "success":
        raise Exception(check_json["message"])
    print("camera/check: \u4eba\u50cf\u68c0\u6d4b\u6210\u529f")
    draft_url = "https://jstxcj.91job.org.cn/wechat/draft/create"
    draft_res = sess.get(draft_url)
    draft_json = draft_res.json()
    if draft_json["type"] != "success":
        raise Exception(draft_json["message"])
    print("draft/create: \u5df2\u52a0\u5165\u8349\u7a3f\u7bb1")

def main(name, stuid, id, imgname):
    login(name, stuid, id)
    upload(imgname)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(*sys.argv[1:])
    else:
        raise Exception("\u53c2\u6570\u9519\u8bef")