一、参考资料
1、学习使用git
Git教程 - 廖雪峰的官方网站 https://www.liaoxuefeng.com/wiki/896043488029600
使用git config --global设置用户名和邮件 https://blog.csdn.net/sjt19910311/article/details/83685616

2、学习使用conda
Anaconda-用conda创建python虚拟环境 https://zhuanlan.zhihu.com/p/94744929

3、熟悉ubuntu系统，⼀些基本的终端指令
Ubuntu常用命令 总结整理 https://zhuanlan.zhihu.com/p/392986700
Linux Ubuntu 入门基本命令整理 https://blog.csdn.net/qq_45277212/article/details/120834748

4、安装Anaconda
Anaconda安装-超详细版(2023) https://blog.csdn.net/weixin_43412762/article/details/129599741
怎么彻底干净的卸载anaconda3？ https://www.zhihu.com/question/393199176

5、Robot类代码
Python robot.Robot类代码示例 https://vimsky.com/examples/detail/python-ex-models.robot-Robot---class.html

6、Python捕捉视频和音频
Python 如何使用Python从相机（或网络摄像头）捕捉视频和音频 https://deepinout.com/python/python-qa/700_python_how_to_capture_a_video_and_audio_in_python_from_a_camera_or_webcam.html
安装PyAudio过程出现错误：Failed building wheel for PyAudio https://zhuanlan.zhihu.com/p/78361283

7、实现语音识别功能（openai whisper模型）
openai whisper https://github.com/openai/whisper
语音识别whisper的介绍、安装、错误记录 https://blog.csdn.net/zdm_0301/article/details/133854913
OpenAI语音识别模型Whisper原理介绍以及代码演示 https://www.bilibili.com/video/BV1SA4m137ta/?vd_source=131c932e072eb6d1f0ace7296dc15b66

8、what’s that⽅向:使⽤yolov5完成给定数据集的⽬标检测训练
2023最新pytorch安装（超详细版） https://blog.csdn.net/weixin_44752340/article/details/130542629
pycharm安装教程配置环境 https://wenku.csdn.net/answer/2g4r2cku2t
yolov5 https://github.com/ultralytics/yolov5?tab=readme-ov-file

9、调用百度AI人体检测接口（⼈体特征、手势识别）
百度智能云平台 https://console.bce.baidu.com/ai/?fromai=1#/ai/body/overview/index

10、欧拉坐标与四元数坐标
如何通俗地解释欧拉角？之后为何要引入四元数？ https://www.zhihu.com/question/47736315/answers/updated
四元数（Quaternion）和旋转 +欧拉角 https://www.cnblogs.com/jins-note/p/9512719.html
四元数与欧拉角（Yaw、Pitch、Roll）的转换（含python代码参考） https://blog.csdn.net/xiaoma_bk/article/details/79082629

二、问题与解决
1、python安装后，输入cmd，输入python，显示的版本还是以前的版本，这个如何更新到新的版本？
https://www.zhihu.com/question/493547164#:~:text=1.%E9%A6%96%E5%85%88%E8%BF%99%E6%98%AF%E5%92%8C%E4%B8%AA%E4%BA%BA%E7%BB%88%E7%AB%AF%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E8%AE%BE%E7%BD%AE%E7%9B%B8%E5%85%B3%E7%9A%84%E4%B8%80%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E5%BD%93%E4%BD%A0%E5%AE%89%E8%A3%85%E4%BA%86%E6%96%B0%E7%89%88%E6%9C%AC%E6%B2%A1%E6%9C%89%E8%A6%86%E7%9B%96%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E4%B8%AD%E6%9C%89%E5%85%B3python%E7%9A%84%E8%AE%BE%E7%BD%AE%E6%98%AF%EF%BC%8C%E5%8D%B3%E4%BD%BF%E6%96%B0%E7%89%88%E6%9C%AC%E5%AE%89%E8%A3%85%E5%AE%8C%EF%BC%8Ccmd%E4%B8%AD%E8%BF%90%E8%A1%8Cpython%E4%BB%8D%E6%98%AF%E6%89%A7%E8%A1%8C%E4%BA%86%E6%97%A7%E7%89%88%E6%9C%AC%E3%80%82%202.%E5%A6%82%E4%BD%95%E8%AE%BE%E7%BD%AEpython%E7%9A%84%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E4%BA%86%EF%BC%9F%20%E4%BB%A5win7%E4%B8%BA%E4%BE%8B%EF%BC%8C%E8%AE%A1%E7%AE%97%E6%9C%BA--%E5%8F%B3%E5%87%BB--%E5%B1%9E%E6%80%A7--%E9%AB%98%E7%BA%A7%E7%B3%BB%E7%BB%9F%E8%AE%BE%E7%BD%AE--%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%20%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E8%AE%BE%E7%BD%AE%203.%E8%AE%BE%E7%BD%AE%E6%9C%89%E4%B8%A4%E7%A7%8D%E6%96%B9%E5%BC%8F%EF%BC%8C%E4%B8%80%E6%98%AF%E7%9B%B4%E6%8E%A5%E5%B0%86python%E6%96%B0%E7%89%88%E6%9C%AC%E7%9A%84,%E5%AE%89%E8%A3%85%E7%9B%AE%E5%BD%95%20%E2%80%9CXXpython%E2%80%9D%E5%8A%A0%E5%85%A5%E5%88%B0path%E4%B8%AD%EF%BC%8C%E4%BA%8C%E6%98%AF%E5%8F%AF%E4%BB%A5%E6%96%B0%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%8F%ABpythonhome%3D%E2%80%9Cxxxpython%E2%80%9D%E7%9A%84%E5%8F%98%E9%87%8F%EF%BC%8C%E7%84%B6%E5%90%8E%E5%86%8Dpath%E4%B8%AD%E6%B7%BB%E5%8A%A0%20%25pythonhome%25%2C%E6%8E%A8%E8%8D%90%E7%AC%AC%E4%BA%8C%E7%A7%8D%E8%AE%BE%E7%BD%AE%E6%96%B9%E5%BC%8F%E3%80%82%204.%E8%AE%BE%E7%BD%AE%E5%AE%8C%E5%90%8E%E4%B8%8D%E7%94%A8%E9%87%8D%E5%90%AF%E7%94%B5%E8%84%91%EF%BC%8C%E4%BD%86%E6%98%AF%E4%B8%80%E5%AE%9A%E8%A6%81%E9%87%8D%E6%96%B0%E6%89%93%E5%BC%80cmd%20%E7%AA%97%E5%8F%A3%E3%80%82
2、ERROR: No .egg-info directory found in C:\xxx\xx\xxx
https://blog.csdn.net/u013066244/article/details/130039052
3、No module named ‘_distutils_hack‘
https://blog.csdn.net/weixin_38739735/article/details/127633988
4、运行yolov5训练时遇到Exception: Dataset not found ❌
https://blog.csdn.net/weixin_45004544/article/details/134687048