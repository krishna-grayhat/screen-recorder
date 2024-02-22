# import cv2
# import pyautogui
# from win32api import GetSystemMetrics
# import numpy as np
# import time
#
# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
# wh = (width,height)
#
# f = cv2.VideoWriter_fourcc(*"XVID")
#
# output = cv2.VideoWriter("test.MP4",f,30.0,wh)
#
# now_time = time.time()
# dur = 10
# end_time = now_time + dur
#
# while True:
#     image = pyautogui.screenshot()
#     frame_1 = np.array(image)
#     frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
#
#     output.write(frame)
#
#     c_time = time.time()
#     if c_time > end_time:
#         break
#
# output.release()
#
# print("-----End >>>>>>>")



# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Edge()
# get google.co.in
driver.get("https://google.co.in")