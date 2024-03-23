import requests
import json

def get_wenxin(prompt):
    # 调用接口
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={24.f843d98c186e57f60493cce002ad4e0a.2592000.1713804147.282335-57884869}"
    # 配置 POST 参数
    payload = json.dumps({
        "messages": [
            {
                "role": "user",# user prompt
                "content": "{}".format(prompt)# 输入的 prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # 发起请求
    response = requests.request("POST", url, headers=headers, data=payload)
    # 返回的是一个 Json 字符串
    js = json.loads(response.text)
    print(js["result"])

# 一个封装 Wenxin 接口的函数，参数为 Prompt，返回对应结果
def get_completion_weixin(prompt, temperature = 0.1, access_token = ""):
    '''
    prompt: 对应的提示词
    temperature：温度系数
    access_token：已获取到的秘钥
    '''
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token={access_token}"
    # 配置 POST 参数
    payload = json.dumps({
        "messages": [
            {
                "role": "user",# user prompt
                "content": "{}".format(prompt)# 输入的 prompt
            }
        ],
        "temperature" : temperature
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # 发起请求
    response = requests.request("POST", url, headers=headers, data=payload)
    # 返回的是一个 Json 字符串
    js = json.loads(response.text)
    # print(js)
    return js["result"]

prompt = '''
请参考下方示例，对{}中的指令内容进行任务拆解，只输出一个 JSON 对象，其中包含以下键：action_type，target，requirement。
注意事项：
1，要以动作为单位来拆分任务，例如"meet Jack at park"，需要拆分为"go park"和"meet Jack"2个动作。
2，要根据句子的顺序来拆分动作。
3，要检查动作的逻辑顺序是否正确，如果符合句子顺序但不符合逻辑顺序，需要调整顺序，例如"meet someone at somewhere"，正确的动作逻辑顺序应该是第一步"go somewhere"，第二部"meet someone"。
4，要检查action_type和target是否匹配合理，例如若action_type为"go"，则"target"应为地名，若action_type为"meet"，则"target"应为人名。
5，要删除重复的动作。

请使用以下格式：
输出 JSON：[MetaAction("action_type","target","requirement")]

示例，输⼊⼀个指令，输出⼀个有顺序的元动作列表，如MetaAction为⼀个机器⼈的元动作类（基础动作）：
输⼊：Meet Charlie at the sofa, follow him, and go to the living room
输出：[MetaAction("move","sofa",None),MetaAction("findperson","Charlie",None),MetaAction(("go","living room",None)]

{Meet Alice at the park, accompany her to the café, and then walk to the library.}
'''
access_token = "24.f843d98c186e57f60493cce002ad4e0a.2592000.1713804147.282335-57884869"
print(get_completion_weixin(prompt, access_token=access_token))