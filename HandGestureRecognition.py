from aip import AipBodyAnalysis

# 我的API密钥和密钥
APP_ID = '57273192'
API_KEY = 'eCkA0se11WyCyiOtRGgh4qqs'
SECRET_KEY = '7tKewKv17E3p4KaRSpcYroeqZjLf8n83'

# 创建AipBodyAnalysis对象
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

# 打开并读取要进行识别的图片
with open('E:/opl/OPLsubject/gesture01.jpg', 'rb') as f:
    image = f.read()

# 调用手势识别接口
result = client.gesture(image)
# 解析识别结果
if 'result' in result:
    for gesture in result['result']:
        if gesture['classname'] == 'Fist':
            print('石头手势')
        elif gesture['classname'] == 'Two':
            print('剪刀手势')
        elif gesture['classname'] == 'Five':
            print('布手势')
else:
    print('识别失败')