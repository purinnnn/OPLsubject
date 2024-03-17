import cv2  # 导入OpenCV库
import pyaudio  # 导入PyAudio库
import wave  # 导入wave库，用于操作音频文件

class Robot:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)  # 初始化摄像头，参数0表示使用默认摄像头
        self.audio = pyaudio.PyAudio()  # 创建PyAudio实例
        self.stream = None  # 初始化音频流变量

    def capture_camera(self):
        ret, frame = self.video_capture.read()  # 读取摄像头图像
        print("Start to capture camera")
        if ret:
            cv2.imshow('Camera', frame)  # 在窗口中显示图像
            cv2.waitKey(0)  # 暂停等待按下任意键继续
        else:
            print("Failed to capture camera")

    def record_audio(self):
        duration = 5  # 录音持续时间（秒）
        fs = 44100  # 采样率（每秒采样点数）
        channels = 1  # 声道数
        format = pyaudio.paInt16  # 音频采样位数

        # 打开音频流
        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=fs,
                                      input=True,
                                      frames_per_buffer=int(fs * duration))

        print("Recording started...")
        frames = []  # 用于存储音频帧数据的列表
        for i in range(0, int(duration * fs / (fs * duration))):
            data = self.stream.read(int(fs * duration))  # 读取音频数据
            frames.append(data)  # 将音频数据添加到列表中

        # 关闭音频流
        self.stream.stop_stream()
        self.stream.close()

        # 保存录音文件
        filename = 'recorded_audio.wav'
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)  # 设置声道数
        wf.setsampwidth(self.audio.get_sample_size(format))  # 设置采样位数
        wf.setframerate(fs)  # 设置采样率
        wf.writeframes(b''.join(frames))  # 将音频帧数据写入文件
        wf.close()
        print(f"Recorded audio saved as {filename}")

    def __del__(self):
        self.video_capture.release()  # 释放摄像头资源
        cv2.destroyAllWindows()  # 关闭窗口

# 创建机器人对象
robot = Robot()

# 调用摄像头
robot.capture_camera()

# 开始录音
robot.record_audio()

# 销毁对象
del robot