import tkinter as tk
import serial
from tkinter import messagebox

root = tk.Tk()  # 创建窗口
root.title('演示窗口')
root.geometry("300x100+630+80")  # (宽度x高度)+(x轴+y轴)

btn1 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn1["text"] = "点击"  # 给按钮一个名称
btn1.pack()  # 按钮布局
"""btn2 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn2["text"] = "点击"  # 给按钮一个名称
btn2.pack()  # 按钮布局
btn3 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn3["text"] = "点击"  # 给按钮一个名称
btn3.pack()  # 按钮布局
btn4 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn4["text"] = "点击"  # 给按钮一个名称
btn4.pack()  # 按钮布局
btn5 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn5["text"] = "点击"  # 给按钮一个名称
btn5.pack()  # 按钮布局
btn6 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn6["text"] = "点击"  # 给按钮一个名称
btn6.pack()  # 按钮布局
btn7 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn7["text"] = "点击"  # 给按钮一个名称
btn7.pack()  # 按钮布局
btn8 = tk.Button(root)  # 创建按钮，并且将按钮放到窗口里面
btn8["text"] = "点击"  # 给按钮一个名称
btn8.pack()  # 按钮布局"""

def LED1CONRDL(e):
    '''创建弹窗'''
    """ser=serial.Serial('COM4',9600)
    ser.write(b'Hello,world!')
    #date=ser.readline()
    print("write")"""
    #ser.close()"""#关闭穿孔链接
    messagebox.showinfo("LED1", "发送成功")


btn1.bind("<Button-1>", LED1CONRDL)  # 将按钮和方法进行绑定，也就是创建了一个事件
root.mainloop()  # 让窗口一直显示，循环
