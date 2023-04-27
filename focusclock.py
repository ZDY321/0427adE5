import time
import datetime

duration = datetime.timedelta(minutes=25) # 设置专注时长为25分钟
interval = datetime.timedelta(seconds=1) # 每隔1秒钟更新一次时钟

start_time = datetime.datetime.now() # 当前时间为计时器的起点
end_time = start_time + duration # 定义结束时间

while datetime.datetime.now() < end_time: # 当当前时间小于结束时间时继续计时
    remaining_time = end_time - datetime.datetime.now() # 剩余时间计算
    remaining_str = str(remaining_time)[2:7] # 将剩余时间截取为分钟和秒数形式
    print("Remaining Time: {}".format(remaining_str), end='\r')
    time.sleep(interval.total_seconds()) # 休眠1秒

print("Time's up!") # 在专注时长结束时提示用户
