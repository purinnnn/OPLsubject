from aip import AipBodyAnalysis

# 我的API Key、Secret Key和App ID
APP_ID = '57271204'
API_KEY = 'xasOTS0LVzrzllMPLU9GB0r2'
SECRET_KEY = 'MazWnnnqtOWsqeD398hMPdFPscbmiMPB'

# 创建AipBodyAnalysis客户端
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

# 调用人体特征检测接口
def detect_body_features(image_path):
    # 读取图片
    with open(image_path, 'rb') as f:
        image = f.read()

    # 调用接口
    result = client.bodyAttr(image)

    # 解析返回结果
    if 'person_info' in result:
        person_info = result['person_info']
        for info in person_info:
            body_features = info['attributes']
            print("人体特征:")
            print(f"年龄: {body_features['age']}")
            print(f"性别: {body_features['gender']['name']}")
            print(f"衣服颜色: {body_features['upper_color']['name']}")
            print(f"裤子颜色: {body_features['lower_color']['name']}")
            print("------------------------")
    else:
        print("未检测到人体")

# 测试
image_path = 'E:/opl/OPLsubject/human.jpg'
detect_body_features(image_path)