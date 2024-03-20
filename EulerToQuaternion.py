import math

# 四元数类
class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

# 将传入的欧拉角转换为四元数    
def to_quaternion(yaw, pitch, roll):
    # Abbreviations for the various angular functions
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
 
    q = Quaternion(0, 0, 0, 0)
    q.w = cy * cp * cr + sy * sp * sr
    q.x = cy * cp * sr - sy * sp * cr
    q.y = sy * cp * sr + cy * sp * cr
    q.z = sy * cp * cr - cy * sp * sr
 
    return q

# 示例
yaw = 0.1  # 欧拉角 yaw
pitch = 0.2  # 欧拉角 pitch
roll = 0.3  # 欧拉角 roll

quat = to_quaternion(yaw, pitch, roll)
print("四元数坐标：w = {}, x = {}, y = {}, z = {}".format(quat.w, quat.x, quat.y, quat.z))