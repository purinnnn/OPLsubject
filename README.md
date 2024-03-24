​RoboCuo@home|OPL@Yao Yuze

# 一、必做题

## 1、学习使用Git

| 我的GitHub仓库链接 | https://github.com/purinnnn/OPLsubject/tree/master |
|:------------:| -------------------------------------------------- |

| 常用命令                                       | 命令行                                                                     |
|:------------------------------------------:|:-----------------------------------------------------------------------:|
| 配置Git                                      | git config --global user.name "Your Name"                               |
| 配置Git                                      | git config --global user.email "email@example.com"                      |
| 查看配置信息                                     | git config -l                                                           |
| 创建目录                                       | mkdir your_directory_name                                               |
| 查找目录                                       | cd your_directory_name                                                  |
| 显示当前目录                                     | pwd                                                                     |
| 将当前目录变成Git可管理的仓库                           | git init                                                                |
| 将文件添加到缓存                                   | git add your_file_name                                                  |
| 将文件提交到库                                    | git commit -m "your_commit_instruction"                                 |
| 查看相关文件状态                                   | git status                                                              |
| 查看文件修改内容                                   | git diff                                                                |
| 查看工作区和版本库里面最新版本的区别                         | git diff HEAD -- your_file_name                                         |
| 显示从最近到最远的详细提交日志                            | git log                                                                 |
| 单行显示从最近到最远的提交日志                            | git log --pretty=oneline                                                |
| 查看文件内容                                     | cat your_file_name                                                      |
| 回退到上一个版本                                   | git reset --hard HEAD^                                                  |
| 回退到过去第100个版本（数字可改）                         | git reset --hard HEAD~100                                               |
| 指定回到未来的某个版本                                | git reset --hard commit_id                                              |
| 查看命令历史记录                                   | git reflog                                                              |
| 丢弃工作区的修改                                   | git checkout -- your_file_name                                          |
| 把暂存区的修改撤销掉                                 | git reset HEAD your_file_name                                           |
| 删除工作区文件                                    | rm your_file_name                                                       |
| 从版本库中删除文件                                  | git rm your_file_name 并且 git commit                                     |
| 把工作区误删的文件恢复到版本库的最新版本                       | git checkout -- your_file_name                                          |
| 把一个已有的本地仓库与GitHub仓库关联                      | git remote add origin git@github.com:your_name/your_repository_name.git |
| 把本地仓库的内容推送到GitHub仓库<br/>（关联本地和远程的master分支） | git push -u origin master                                               |
| 把本地仓库的内容推送到GitHub仓库                        | git push origin master                                                  |
| 查看远程库信息                                    | git remote -v                                                           |
| 删除远程库<br/>（解除本地和远程的绑定关系）                   | git remote rm remote_repository_name<br/>e.g. git remote rm origin      |
| 从远程克隆一个本地库                                 | git clone git@github.com:your_name/your_repository_name.git             |

> 参考学习链接：
> 
> （1）Git教程 - 廖雪峰的官方网站 [Git教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600)
> 
> （2）使用git config --global设置用户名和邮件 [使用git config --global设置用户名和邮件_git config --global user.name-CSDN博客](https://blog.csdn.net/sjt19910311/article/details/83685616)

## 2、学习使用conda

<img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-24-04-39-39-image.png" title="" alt="" data-align="center">

| 常用命令            | 命令行                                      |
|:---------------:|:----------------------------------------:|
| 查看已安装的包         | conda list                               |
| 查看已有虚拟环境        | conda env list                           |
| 检查更新当前conda     | conda update conda                       |
| 创建虚拟环境          | conda create -n your_env_name python=x.x |
| 切换虚拟环境          | activate your_env_name                   |
| 查看当前环境的python版本 | python -V                                |
| 对虚拟环境中安装额外的包    | conda install -n your_env_name [package] |
| 删除虚拟环境          | conda remove -n your_env_name --all      |

> 参考学习链接：
> 
> （1）Anaconda安装-超详细版(2023) https://blog.csdn.net/weixin_43412762/article/details/129599741
> 
> （2）怎么彻底干净的卸载anaconda3？ https://www.zhihu.com/question/393199176
> 
> （3）Anaconda-用conda创建python虚拟环境 https://zhuanlan.zhihu.com/p/94744929

## 3、学习使用python基本语法

| 任务文件     | 说明                                                                  | 安装库             |
|:--------:|:-------------------------------------------------------------------:|:---------------:|
| robot.py | a.创建robot类<br/>b.实现类功能：调用摄像头，捕捉摄像头图像<br/>c.实现类功能：开启麦克风录音，将音频文件保存到本地 | cv2<br/>pyaudio |

### 使用说明：

1. 建立虚拟环境（python=3.7.12），安装cv2库和pyaudio库

2. 使用vscode打开robot.py

3. 选定刚才建立的虚拟环境作为python解释器
   
   <img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-25-03-16-38-屏幕截图%202024-03-24%20220152.png" title="" alt="" data-align="center">

4. 在代码中右键选择“运行Python”-“在终端中运行Python文件”

5. 捕捉到摄像头图像，接着按任意键继续

6. 终端窗口输出“Recording started...”，开始使用麦克风录制音频

7. 录制好的音频文件“recorded_audio.wav”被保存到“robot.py”同目录下
   
   

> 参考学习链接：
> 
> （1）Python 如何使用Python从相机（或网络摄像头）捕捉视频和音频 https://deepinout.com/python/python-qa/700_python_how_to_capture_a_video_and_audio_in_python_from_a_camera_or_webcam.html
> （2）安装PyAudio过程出现错误：Failed building wheel for PyAudio https://zhuanlan.zhihu.com/p/78361283
> 
> （3）Python robot.Robot类代码示例 https://vimsky.com/examples/detail/python-ex-models.robot-Robot---class.html

## 4、熟悉ubuntu系统，一些基本的终端指令

| 常用命令                   | 命令行              |
|:----------------------:|:----------------:|
| sudo apt install <软件名> | 安装软件             |
| sudo apt list          | 查看所有已安装的软件列表     |
| sudo apt remove <软件名>  | 删除某个软件包          |
| sudo apt upgrade       | 升级包到最新版本         |
| ls                     | 查看当前文件夹下的内容      |
| pwd                    | 查看当前所在文件夹        |
| cd <目录名>               | 切换文件夹            |
| touch <目录名>            | 如果文件不存在，新建文件     |
| mkdir <目录名>            | 创建目录             |
| rm <文件名>               | 删除指定的文件          |
| clear                  | 清屏               |
| cd                     | 切换到当前用户的主目录      |
| cd ~                   | 切换到当前用户的主目录      |
| cd .                   | 保持在当前目录不变        |
| cd ..                  | 切换到上级目录          |
| cd -                   | 在最近两次工作目录之间来回切换  |
| ifconfig               | 查看网卡配置信息         |
| ping ip地址              | 检测到目标ip地址的连接是否正常 |
| vim <文件名>              | 启动vim编辑器         |
| 按下 `i` 键               | 进入插入模式           |
| 按下 `Esc` 键             | 退出插入模式           |
| 输入 `:w`                | 保存文件             |
| 输入 `:q` 命令             | 退出vim编辑器         |

> 参考学习链接：
> 
> （1）Ubuntu常用命令 总结整理 https://zhuanlan.zhihu.com/p/392986700
> 
> （2）Linux Ubuntu 入门基本命令整理 [Linux Ubuntu 入门基本命令整理_linux ubuntu入门基本命令整理-CSDN博客](https://blog.csdn.net/qq_45277212/article/details/120834748)

# 二、选做题

## 1、通用功能：完成语音识别功能

【说明】调⽤电脑的⻨克⻛，通过调⽤openai whisper语⾳识别模型，完成语⾳转⽂字

| 任务文件                 | 说明                                       | 安装库                 |
|:--------------------:|:----------------------------------------:|:-------------------:|
| SpeechRecognition.py | 调⽤openai whisper语⾳识别模型实现语⾳转⽂字（录制音频或导入音频） | pyaudio<br/>whisper |
| recorded_audio.wav   | 执行程序录制的音频                                |                     |
| abm.mp3              | 提前准备的奥巴马演讲音频                             |                     |
| result.txt           | 语音转文字结果的文本文件                             |                     |
| abmOriginalText.txt  | 提前准备的奥巴马演讲音频的正确文字稿                       |                     |

### 使用说明：

1. 建立虚拟环境（python=3.9.18），安装pyaudio库和whisper

2. 使用vscode打开SpeechRecognition.py

3. 选定刚才建立的虚拟环境作为python解释器

4. 代码第51行`result = model.transcribe("abm.mp3")`可以选择识别已有音频文件（`“abm.mp3”`）或麦克风录制的音频文件（`“recorded_audio.wav”`）

5. 在代码中右键选择“运行Python”-“在终端中运行Python文件”

6. 终端窗口输出“Recording started...”，开始使用麦克风录制音频

7. 录制好的音频文件“recorded_audio.wav”被保存到“SpeechRecognition.py”同目录下

8. 终端窗口输出语音识别的text文本结果

9. 语音识别得到的text文本结果“result.txt”被保存到“SpeechRecognition.py”同目录下

<img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-24-23-56-29-image.png" title="" alt="" data-align="center">

<img title="" src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-24-23-57-02-image.png" alt="" data-align="center">

> 参考学习链接：
> 
> （1）openai whisper https://github.com/openai/whisper
> （2）语音识别whisper的介绍、安装、错误记录 https://blog.csdn.net/zdm_0301/article/details/133854913
> （3）OpenAI语音识别模型Whisper原理介绍以及代码演示 https://www.bilibili.com/video/BV1SA4m137ta/?vd_source=131c932e072eb6d1f0ace7296dc15b66

## 2、what’s that推荐方向:使用yolov5完成给定数据集的目标检测训练

### 使用说明：

#### 环境配置

1. 安装pycharm，建立虚拟环境（python=3.9.18）

2. 在工作目录打开Git Bash，输入命令`git clone https://github.com/ultralytics/yolov5  # clone`，下载yolov5代码

3. 进入yolov5文件夹目录，安装第三方库，`pip install -r requirements.txt`

#### 数据标注

1. 在刚刚建立的虚拟环境中，安装数据标注软件，`pip install labelimg`

2. 在命令行中输入labelimg即可打开，`labelimg`

3. 打开需要进行标注的文件夹：点击Open Dir -> 选择需要标注的文件夹 -> ok

4. 选择yolo标注格式
   
   <img title="" src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-24-23-49-04-image.png" alt="" data-align="center">

5. 打标签：点击Create RectBo -> 拖拽鼠标框选目标 -> 给上标签 -> 点击ok

6. 保存：点击save，保存txt至`E:\opl\OPLsubject\yolov5\datasets\subject\labels\train`

7. 文件目录结构如下：
   
   ![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-03-18-37-image.png)

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-03-18-26-屏幕截图%202024-03-24%20231559.png)

#### yolov5模型训练

1. 使用pycharm打开yolov5项目

2. 选择虚拟环境：File -> Settings -> Project:yolov5 -> Python Interpreter -> add -> Conda Enviroment -> Existing Enviroment -> 选择虚拟环境路径 -> ok

3. 测试代码是否能够正常运行：运行train.py，代码会自动下载演示数据集以及预训练模型，并且开始训练，若运行正常，则说明环境安装正确

4. 训练自己的数据（添加数据配置文件）：在yolov5/data文件夹下新建subject.yaml
   
   ![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-03-18-58-屏幕截图%202024-03-24%20232731.png)
   
   其中：
   
   path：数据集的根目录
   train：训练集与path的相对路径
   val：验证集与path的相对路径
   nc：类别数量，因为这个数据集只有一个类别（fire），nc即为1
   names：类别名字

5. [下载预训练模型]([跳转中...](https://link.zhihu.com/?target=https%3A//github.com/ultralytics/yolov5/releases))，选择yolov5s.pt下载，并将其保存至`E:\opl\OPLsubject\yolov5\runs\train\exp\weights`
   
   ![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-24-23-50-12-image.png)

6. 开始训练：进入train.py -> Edit Configurations：在Script parameters，输入对应参数命令`--weights runs/train/exp/weights/yolov5s.pt --data data/subject.yaml --workers 1 --batch-size 8`，开始训练模型

7. 模型训练的可视化结果以及训练好的模型保存在runs文件夹下
   
   ![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-03-19-17-屏幕截图%202024-03-24%20233827.png)

#### 模型测试

1. 模型训练完成后，将runs/expx/weights下的模型（best.pt）复制在yolov5文件夹下

2. 开始测试，`python detect.py --weights best.pt --source ../datasets/subject/images/test`

3. 测试结果保存在runs/detect/exp下
   
   ![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-03-19-31-屏幕截图%202024-03-24%20234338.png)
   
   <img title="" src="file:///E:/opl/OPLsubject/yolov5/runs/detect/exp/11.jpg" alt="" data-align="center" width="331"><img title="" src="file:///E:/opl/OPLsubject/yolov5/runs/detect/exp/12.jpg" alt="" width="328" data-align="center">

> 参考学习链接：
> 
> （1）2023最新pytorch安装（超详细版） https://blog.csdn.net/weixin_44752340/article/details/130542629
> （2）pycharm安装教程配置环境 https://wenku.csdn.net/answer/2g4r2cku2t
> （3）yolov5 https://github.com/ultralytics/yolov5?tab=readme-ov-file

## 3、GPSR推荐方向：编写一个prompt，通过调用任意大语言模型，实现对一条指令的任务拆解

【说明】输⼊⼀个指令，输出⼀个有顺序的元动作列表，如MetaAction为⼀个机器⼈的元动作类（基础动作）：

i. 输⼊：Meet Charlie at the sofa, follow him, and go to the living room

ii. 模型返回结果：MetaAction("move",sofa”,None),MetaAction("findperson",Charlie,None),MetaAction( ("go",”living room”,None)]

| 任务文件                | 说明                                             |
|:-------------------:|:----------------------------------------------:|
| GetAccessToken.py   | 百度文心大语言模型：使用 API Key，Secret Key 获取access_token |
| MetaActionPrompt.py | 调用百度文心大语言模型实现对机器人动作指令任务的拆解                     |

### 使用说明：

1. 建立虚拟环境（python=3.7.12）

2. 登录[百度智能云千帆大模型平台]([百度智能云控制台 (baidu.com)](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application))创建应用，获取“API Key”和“Secret Key”

3. 使用vscode打开GetAccessToken.py，替换自己的“API Key”和“Secret Key”，执行程序获取自己的“access_token”

4. 使用vscode打开MetaActionPrompt.py，替换自己的“access_token”

5. MetaActionPrompt.py代码第53到70行为自行撰写的prompt，其中第69行`{Meet Alice at the park, accompany her to the café, and then walk to the library.}`为希望模型拆解的新任务，其他行内容是为大语言模型提供的要求与参考

6. 在代码中右键选择“运行Python”-“在终端中运行Python文件”

7. 终端窗口以json格式输出任务拆解结果
   
   <img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-24-23-59-46-image.png" title="" alt="" data-align="center">

> 参考学习链接：
> 
> （1）面向开发者的Prompt Engineering https://prompt-engineering.xiniushu.com/
> （2）动手学大模型应用开发 https://datawhalechina.github.io/llm-universe/#/
> （3）百度智能云 https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application

## 4、reception推荐方向：调用百度人体特征检测接口：实现人体的特征识别

| 任务文件                         | 说明                                              | 安装库       |
|:----------------------------:|:-----------------------------------------------:|:---------:|
| HumanSignatureRecognition.py | 调用百度人体检测与属性识别接口，<br/>实现“年龄、性别、衣服颜色、裤子颜色”的人体特征识别 | baidu-aip |
| human.jpg                    | 用于测试程序效果的关于人的图片                                 |           |

### 使用说明：

1. 建立虚拟环境（python=3.7.12），安装baidu-aip

2. 使用vscode打开HumanSignatureRecognition.py，替换自己的"API Key"、"Secret Key"和"App ID"

3. 选定刚才建立的虚拟环境作为python解释器

4. 代码第35行`image_path = 'E:/opl/OPLsubject/human.jpg'`设置希望测试图片的绝对路径

5. 在代码中右键选择“运行Python”-“在终端中运行Python文件”

6. 终端窗口输出人体特征识别结果

<img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-25-00-00-54-image.png" title="" alt="" data-align="center">

> 参考学习链接：
> 
> 百度智能云平台 https://console.bce.baidu.com/ai/?fromai=1#/ai/body/overview/index

## 5、waht’s that推荐方向：调用百度手势识别检测接口：实现石头，剪刀，布手势识别

| 任务文件                      | 说明                         | 安装库       |
|:-------------------------:|:--------------------------:|:---------:|
| HandGestureRecognition.py | 调用百度手势识别接口，实现“石头、剪刀、布”手势识别 | baidu-aip |
| gesture01.jpg             | 测试图片：剪刀手势                  |           |
| gesture02.jpg             | 测试图片：石头手势                  |           |
| gesture03.jpg             | 测试图片：布手势                   |           |

### 使用说明：

1. 建立虚拟环境（python=3.7.12），安装baidu-aip

2. 使用vscode打开HandGestureRecognition.py，替换自己的"API Key"、"Secret Key"和"App ID"

3. 选定刚才建立的虚拟环境作为python解释器

4. 代码第12行`with open('E:/opl/OPLsubject/gesture01.jpg', 'rb') as f:`设置希望测试图片的绝对路径

5. 在代码中右键选择“运行Python”-“在终端中运行Python文件”

6. 终端窗口输出手势识别结果

<img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-25-00-01-42-image.png" title="" alt="" data-align="center">

> 参考学习链接：
> 
> 百度智能云平台 https://console.bce.baidu.com/ai/?fromai=1#/ai/body/overview/index

## 6、Tidy up 推荐方向：将给定的欧拉坐标转换为四元数坐标python函数实现，了解像素-相机-世界坐标系之间的转换，以图文形式说明

| 任务文件                 | 说明                   |
|:--------------------:|:--------------------:|
| EulerToQuaternion.py | 创建四元数类，将传入的欧拉角转换为四元数 |

<img src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-25-00-02-41-image.png" title="" alt="" data-align="center">

### 像素-相机-世界坐标系之间的转换

#### 1、理解四个坐标之间的几何关系

<img title="" src="file:///C:/Users/姚俞泽/AppData/Roaming/marktext/images/2024-03-25-03-20-38-坐标关系.png" alt="" width="776" data-align="center">

- Ow−XwYwZw:世界坐标系，描述相机位置，单位:m
- Oc−XcYcZc:相机坐标系，光心为原点，单位：m
- Oxy: 图像坐标系，光心为图像中点，单位：mm
- uv: 像素坐标系，原点为图像左上角，单位：pixel
- P: 世界坐标系中的一点，即为生活中真实的一点；
- p: 点P在图像中的成像点，在图像坐标系中的坐标为(x,y),在像素坐标系中的坐标为(u,v);
- f: 相机焦距，等于o与Oc的距离，f=||o−Oc||。

#### 2、世界坐标系和相机坐标系之间的转换

<img title="" src="https://mazhengg.github.io/2019/03/29/%E4%B8%96%E7%95%8C%E3%80%81%E7%9B%B8%E6%9C%BA%E3%80%81%E5%9B%BE%E5%83%8F%E5%92%8C%E5%83%8F%E7%B4%A0%E5%9D%90%E6%A0%87%E4%B9%8B%E9%97%B4%E7%9A%84%E8%BD%AC%E6%8D%A2/%E4%B8%96%E7%95%8C%E5%88%B0%E7%9B%B8%E6%9C%BA.png" alt="" width="693" data-align="center">

从世界坐标系变换到相机坐标系属于刚体变换：即物体不会发生形变，只需要进行旋转和平移。  
R:表示旋转矩阵；  
T:表示平移矩阵。

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-13-28-image.png)

以齐次坐标表示：

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-13-43-image.png)

#### 3、相机坐标系到图像坐标系之间的转换

<img title="" src="https://mazhengg.github.io/2019/03/29/%E4%B8%96%E7%95%8C%E3%80%81%E7%9B%B8%E6%9C%BA%E3%80%81%E5%9B%BE%E5%83%8F%E5%92%8C%E5%83%8F%E7%B4%A0%E5%9D%90%E6%A0%87%E4%B9%8B%E9%97%B4%E7%9A%84%E8%BD%AC%E6%8D%A2/%E7%9B%B8%E6%9C%BA%E5%88%B0%E5%9B%BE%E5%83%8F.png" alt="" width="537" data-align="center">

从相机坐标系到图像坐标系是从3D转换到2D，属于透视投影关系，以下是推导过程：

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-14-47-image.png)

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-14-55-image.png)

Zc是空间点P的深度信息。此时，投影点p的单位还是mm，并不是像素pixel，需要进一步转换到像素坐标系。

#### 4、图像坐标系到像素坐标系之间的转换

像素坐标系和图像坐标系都在成像平面上，只是各自的原点和度量单位不一样。图像坐标系的原点为相机光轴与成像平面的交点，通常情况下是成像平面的中点或者叫principal point。图像坐标系的单位是mm，是物理单位，而像素坐标系的单位是pixel，我们平常描述一个像素点都是几行几列。所以这两者之间的转换关系如下：

<img title="" src="https://mazhengg.github.io/2019/03/29/%E4%B8%96%E7%95%8C%E3%80%81%E7%9B%B8%E6%9C%BA%E3%80%81%E5%9B%BE%E5%83%8F%E5%92%8C%E5%83%8F%E7%B4%A0%E5%9D%90%E6%A0%87%E4%B9%8B%E9%97%B4%E7%9A%84%E8%BD%AC%E6%8D%A2/%E5%9B%BE%E5%83%8F%E5%88%B0%E5%83%8F%E7%B4%A0.png" alt="" width="597" data-align="center">

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-15-40-image.png)

其中，dx和dy分别表示每一列和每一行分别代表多少mm，即1pixel=dxmm。

以齐次坐标形式表示为：

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-15-57-image.png)

最后总结起来：

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-16-14-image.png)

其中，

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-00-16-32-image.png)

Zc是深度信息：所以一个空间中的坐标点，可以在图像中找到一个对应的像素点，但是，通过图像中的一个点找到它在空间中对应的点就很难。因为Zc（深度信息）未知。

> 参考学习链接：
> 
> 【欧拉坐标与四元数坐标】
> （1）如何通俗地解释欧拉角？之后为何要引入四元数？ https://www.zhihu.com/question/47736315/answers/updated
> （2）四元数（Quaternion）和旋转 +欧拉角 https://www.cnblogs.com/jins-note/p/9512719.html
> （3）四元数与欧拉角（Yaw、Pitch、Roll）的转换（含python代码参考） https://blog.csdn.net/xiaoma_bk/article/details/79082629
> 
> 【像素-相机-世界坐标系之间的转换】
> （1）图像处理——4个坐标系及相关转换图像像素坐标系 图像物理坐标系 相机坐标系 世界坐标系 https://blog.csdn.net/MengYa_Dream/article/details/120233806
> （2）世界坐标系，相机坐标系，图像坐标系，像素坐标系的转换 https://zhuanlan.zhihu.com/p/282497081
> （3）世界、相机、图像和像素坐标之间的转换 https://mazhengg.github.io/2019/03/29/%E4%B8%96%E7%95%8C%E3%80%81%E7%9B%B8%E6%9C%BA%E3%80%81%E5%9B%BE%E5%83%8F%E5%92%8C%E5%83%8F%E7%B4%A0%E5%9D%90%E6%A0%87%E4%B9%8B%E9%97%B4%E7%9A%84%E8%BD%AC%E6%8D%A2/
> （4）世界坐标系,相机坐标系和图像坐标系的转换(Python) https://blog.csdn.net/guyuealian/article/details/104184551

## 7、建图导航方向：在ubuntu基础上，安装并学习ros,学会用ROS 收发话题

### 安装并学习ROS：启动一个小海龟仿真

```
# 启动ROS Master
roscore

# 启动小海龟仿真器
rosrun turtlesim turtlesim_node

# 启动小海龟控制节点
rosrun turtlesim turtle_teleop_key
```

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-02-46-31-569ea6b407ae9b053a558d67c0e83af.jpg)

### ROS收发话题

#### 基础：通过操纵小海龟案例，具体学习日常使用topic通讯过程中常用到的几个命令

| 命令                                 | 说明                                         |
|:----------------------------------:|:------------------------------------------:|
| roscore                            | 启动ros master节点管理器（大管家）                     |
| rosrun turtlesim turtlesim_node    | 启动turtlesim节点<br/>（启动小海龟仿真）                |
| rosrun turtlesim turtle_teleop_key | 启动teleop_turtle节点<br/>（通过发布对应topic控制小海龟移动） |
| rosnode list                       | 查看所有启动的节点                                  |
| rosrun rqt_graph rqt_graph         | 查看节点连接图                                    |
| rostopic info /turtle1/cmd_vel     | 具体查看topic“/turtle1/cmd_vel”的相关信息           |
| rosmsg show geometry_msgs/Twist    | 具体查看数据类型”geometry_msgs/Twist“中包括哪些信息       |

```通过命令来实现往对应的topic上pub消息控制机器人运动。键入如下命令让小乌龟持续转起来，最后-r
# 通过命令来实现往对应的topic上pub消息控制机器人运动。
# 键入如下命令让小乌龟持续转起来，最后-r 1的参数含义是，按照1hz的频率pub这条topic：
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.0" -r 1
```

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-02-46-02-b11e565d879fc966a56869af40a1d61.jpg)

#### 进阶：自主创建node实现message的发布与订阅

##### 创建node实现message的发布与订阅（C++版本）

###### publisher

编辑cpp_talker.cpp文件：

```
#include <ros/ros.h>
#include <learn_topic/person.h>

int main(int argc, char **argv){

    ros::init(argc, argv, "cpp_talker");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<learn_topic::person>("/person_topic", 1);

    ros::Rate loop_rate(1);

    learn_topic::person man;
    man.age = 0;
    man.name = "allen";
    ROS_INFO("pub: Here's a man named, how old is he? %s", man.name.data());
    while (ros::ok()){
        man.age++;
        pub.publish(man);
        loop_rate.sleep();
    }
    return 0;
}
```

###### subscriber

编辑cpp_listener.cpp文件：

```
#include <ros/ros.h>
#include "learn_topic/person.h"

void getAgeCallback(const learn_topic::personConstPtr &person){

    ROS_INFO("answer: %s's age is %d", person->name.data(), person->age);
}

int main(int argc, char **argv){

    ros::init(argc, argv, "cpp_listener");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("/person_topic",1, getAgeCallback);
    ros::spin();
    return 0;
}
```

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-02-43-36-d940ca3edb6bb4fc11b87953cd5a0da.jpg)

##### 创建node实现message的发布与订阅（python版本）

###### publisher

编辑python_talker.py文件：

```
#!/usr/bin/env python
#coding=utf-8
import rospy
#倒入自定义的数据类型
from learn_topic.msg import person

def talker():
    pub = rospy.Publisher('person_topic', person, queue_size=10)
    rospy.init_node('pytalker', anonymous=True)
    rate = rospy.Rate(1)
    name='allen'
    rospy.loginfo('Talker: this man named %s', name)
    i = 0
    while not rospy.is_shutdown():
            pub.publish(person('allen',i))
            i = i+1
            rate.sleep()

if __name__ == '__main__':
    talker()
```

###### subscriber

编辑python_listener.py文件：

```
#!/usr/bin/env python
#coding=utf-8
import rospy
#倒入自定义的数据类型
from learn_topic.msg import person

def callback(person):
    rospy.loginfo('Listener: %s''s age is %d', person.name, person.age)

def listener():
    rospy.init_node('pylistener', anonymous=True)
    rospy.Subscriber('person_topic', person, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
```

![](C:\Users\姚俞泽\AppData\Roaming\marktext\images\2024-03-25-02-44-42-7164270c06c444972bb143634267db0.jpg)

> 参考学习链接：
> 
> ​（1）Ubuntu20.04.4安装ROS Noetic详细教程 https://zhuanlan.zhihu.com/p/515361781
> （2）ROS基础(一)：ROS通讯之话题(topic)通讯 https://blog.csdn.net/allenhsu6/article/details/112334048

# 三、其他问题与解决

> 1、python安装后，输入cmd，输入python，显示的版本还是以前的版本，这个如何更新到新的版本？
> https://www.zhihu.com/question/493547164/answer/2187893858
> 
> 2、ERROR: No .egg-info directory found in C:\xxx\xx\xxx
> https://blog.csdn.net/u013066244/article/details/130039052
> 
> 3、No module named ‘_distutils_hack‘
> https://blog.csdn.net/weixin_38739735/article/details/127633988
> 
> 4、运行yolov5训练时遇到Exception: Dataset not found ❌
> https://blog.csdn.net/weixin_45004544/article/details/134687048
> 
> 5、在 ROS 系统中，遇到 roscore 无任何反应，解决办法。
> https://blog.csdn.net/qq_50840738/article/details/126018200
