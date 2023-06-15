from PIL import Image, ImageTk
import cv2
import numpy
import random
import tkinter as tk
import tkinter.filedialog
filename = 'seal.jpg'


def basic():
    global img_real
    global filename
    filename = tk.filedialog.askopenfilename()
    img_real = ImageTk.PhotoImage(Image.open(filename))
    image_real.config(image=img_real)

# 二值化


def bitnary():
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img_result = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('bitnary', img_result)
    cv2.waitKey(0)

# 灰階


def gray():
    img_result = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('gray', img_result)
    cv2.waitKey(0)


# 中值濾波
def medianFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.medianBlur(img, 5)  # 增加内核大小為5
    img_result = cv2.medianBlur(img_result, 5)  # 再次應用中值滤波器
    cv2.imshow("medianFilter", img_result)
    cv2.waitKey(0)


# 平均濾波
def averageFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.blur(img, (5, 5))
    cv2.imshow("averageFilter", img_result)
    cv2.waitKey(0)

# 高斯濾波


def gaussianFilter():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.GaussianBlur(img, (5, 5), 1)
    cv2.imshow("gaussianFilter", img_result)
    cv2.waitKey(0)

# 椒鹽雜訊


def saltAndPepper():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = numpy.zeros(img.shape, numpy.uint8)
    thres = 1 - 0.05
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            randomnum = random.random()
            if randomnum < 0.05:
                img_result[i][j] = 0
            elif randomnum > thres:
                img_result[i][j] = 255
            else:
                img_result[i][j] = img[i][j]
    cv2.imshow("saltAndPepper", img_result)
    cv2.waitKey(0)

# 侵蝕，將迭代次數設定為2並使用5x5的核


def erosion():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    kernel = numpy.ones((3, 3), numpy.uint8)
    img_result = cv2.erode(img, kernel, iterations=2)
    cv2.imshow("erosion", img_result)
    cv2.waitKey(0)


# 膨脹
def dilate():
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    kernel = numpy.ones((5, 5), numpy.uint8)
    img_result = cv2.dilate(image, kernel, iterations=5)
    cv2.imshow('dilate', img_result)
    cv2.waitKey(0)

# 銳化


def sharpen():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_blur = cv2.GaussianBlur(img, (0, 0), 100)
    img_result = cv2.addWeighted(img, 1.5, img_blur, -0.5, 0)
    cv2.imshow("Sharpen", img_result)
    cv2.waitKey(0)

# 邊緣偵測


def edgeDetect():
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    img_result = cv2.Canny(img, 30, 70)
    cv2.imshow("canny", img_result)
    cv2.waitKey(0)


def define_layout(obj, cols=1, rows=1):

    def method(trg, col, row):

        for c in range(cols):
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj) == list:
        [method(trg, cols, rows) for trg in obj]
    else:
        trg = obj
        method(trg, cols, rows)


window = tk.Tk()
window.title('Window')
window.geometry("1600x900")
window.state("zoomed")
window.config(bg="#003060")

align_mode = 'nswe'
pad = 5

div_file = tk.Frame(window,  width=1600, height=100)
div_real = tk.Frame(window,  width=1280, height=720)
div_button = tk.Frame(window,  width=320, height=720)
div_exitbutton = tk.Frame(window, width=320, height=720)
window.update()
win_size = min(window.winfo_width(), window.winfo_height())
print(win_size)

div_file.grid(column=0, row=0, padx=pad, pady=pad, columnspan=2)
div_real.grid(column=0, row=1, padx=pad, pady=pad,
              rowspan=2, sticky=align_mode)
div_button.grid(column=1, row=1, padx=pad, pady=pad,
                rowspan=2, sticky=align_mode)
div_exitbutton.grid(column=1, row=0, padx=pad, pady=pad, columnspan=2)

define_layout(window, cols=3, rows=3)
define_layout([div_exitbutton, div_file, div_real, div_button])

button = tk.Button(div_file, text='請選擇圖片檔', font=("標楷體", 20),
                   bg='#272727', fg='#84C1FF', command=basic)
button.grid(column=0, row=0, sticky=align_mode)
button = tk.Button(div_exitbutton, text='離開程式', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=window.quit)
button.grid(column=0, row=0, sticky=align_mode)

img_origin = ImageTk.PhotoImage(Image.open(filename).resize((1280, 720)))
image_real = tk.Label(div_real, image=img_origin, bg='#003060')
image_real.grid(column=0, row=0, sticky=align_mode)

bt_bitnary = tk.Button(div_button, text='二值化', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=bitnary)
bt_gray = tk.Button(div_button, text='灰階化', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=gray)
bt_medianFilter = tk.Button(div_button, text='中值濾波', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=medianFilter)
bt_averageFilter = tk.Button(div_button, text='平均濾波', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=averageFilter)
bt_gaussianFilter = tk.Button(div_button, text='高斯濾波', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=gaussianFilter)
bt_saltAndPepper = tk.Button(div_button, text='椒鹽雜訊', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=saltAndPepper)
bt_erosion = tk.Button(div_button, text='侵蝕', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=erosion)
bt_dilate = tk.Button(div_button, text='膨脹', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=dilate)
bt_sharpen = tk.Button(div_button, text='銳化', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=sharpen)
bt_edgeDetect = tk.Button(div_button, text='邊緣偵測', font=(
    "標楷體", 20), bg='#272727', fg='#84C1FF', command=edgeDetect)

bt_erosion.grid(column=0, row=0, sticky=align_mode)
bt_dilate.grid(column=0, row=1, sticky=align_mode)
bt_sharpen.grid(column=0, row=2, sticky=align_mode)
bt_edgeDetect.grid(column=0, row=3, sticky=align_mode)
bt_saltAndPepper.grid(column=0, row=4, sticky=align_mode)
bt_gray.grid(column=1, row=0, sticky=align_mode)
bt_bitnary.grid(column=1, row=1, sticky=align_mode)
bt_averageFilter.grid(column=1, row=2, sticky=align_mode)
bt_medianFilter.grid(column=1, row=3, sticky=align_mode)
bt_gaussianFilter.grid(column=1, row=4, sticky=align_mode)

define_layout(window, cols=2, rows=3)
define_layout(div_file)
define_layout(div_exitbutton)
define_layout(div_real)
define_layout(div_button, cols=2, rows=5)

window.mainloop()
