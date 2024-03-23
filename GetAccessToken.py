import requests
import json

def get_access_token(api_key, secret_key):
    """
    使用 API Key，Secret Key 获取access_token
    """
    # 指定网址
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    # 设置 POST 访问
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # 通过 POST 访问获取账户对应的 access_token
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

if __name__ == "__main__":
    api_key = "YHgm9nUsyc0cb1s7ffUw2Qzc"  # 替换为自己的API Key
    secret_key = "4UO2nGlb0fQx5WENIg5UEXyP6UrN3bi2"  # 替换为自己的Secret Key
    access_token = get_access_token(api_key, secret_key)
    print(access_token)