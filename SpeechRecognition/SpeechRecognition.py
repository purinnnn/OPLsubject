import pyaudio  # 导入PyAudio库
import wave  # 导入wave库，用于操作音频文件
import whisper

class Robot:
    def __init__(self):
        self.audio = pyaudio.PyAudio()  # 创建PyAudio实例
        self.stream = None  # 初始化音频流变量

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
        wf.close()  # 关闭音频文件
        print(f"Recorded audio saved as {filename}")
        
# 创建机器人对象
robot = Robot()

# 开始录音
robot.record_audio()

# 语音识别
model = whisper.load_model("base")
result = model.transcribe("abm.mp3")    # 选择识别已有音频文件或之前录制的音频文件（recorded_audio.wav）
print(result["text"])

# 将结果保存到txt文件
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(result['text'])

print("结果已保存到result.txt文件")

# 销毁对象
del robot