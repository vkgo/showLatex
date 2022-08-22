from matplotlib import mathtext
import os
from sympy import preview
from pnglatex import pnglatex


import matplotlib.pyplot as plt
import io
from PIL import Image, ImageChops
white = (255, 255, 255, 255)
def latex_to_img(tex):
    buf = io.BytesIO()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.05, 0.5, f'${tex}$', size=40)
    plt.savefig(buf, format='png')
    plt.close()
    im = Image.open(buf)
    bg = Image.new(im.mode, im.size, white)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return im.crop(bbox)



output_folder = './data/test_png/'
input_file = './data/test_caption.txt'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        latex_code = line[line.find('\t'): ]
        file_name = line[:line.find('\t')]
        # latex_code = latex_code.replace(" ","")
        latex_code = latex_code.replace("\t", "")
        latex_code = latex_code.replace("\n", "")
        latex_code = '$' + latex_code + '$'
        # print(file_name,latex_code)
        file_name = file_name + '.png'
        output_file = os.path.join(output_folder, file_name)

        # 以下是4种方法
        # mathtext.math_to_image(latex_code, output_file, dpi=200) # 方法1： 优点：不需要tex环境  缺点：对空格的兼容性差
        preview(expr=latex_code, viewer='file', filename=output_file) # 方法2： 优点：转换的大小刚好合适  缺点：需要tex环境 & 转换速度很慢
        # pnglatex(latex_code, output_file) # 方法3： 需要tex环境 运行不了
        # latex_to_img(latex_code).save(output_file) # 方法4： 优点：转换速度很快 缺点：需要tex环境 & size固定
print("end")
