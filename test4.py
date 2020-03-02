from collections import Counter
import urllib
import random
import webbrowser

import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np
from konlpy.tag import Twitter
from lxml import html
import pytagcloud  # requires Korean font support
import sys

r = lambda: random.randint(0, 255)
# 글씨의 랜덤색깔
color = lambda: (r(), r(), r())


def get_tags(text, ntags=50, multiplier=3):  # 전에 했던 명사 탐색
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return [{'color': color(), 'tag': n, 'size': (c * multiplier) / 2} \
            for n, c in count.most_common(ntags)]


def draw_cloud(tags, filename, fontname='NanumGothic', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

    def main():
        text_file = open("고혈압 피해야할 음식_conut.txt", 'r')
        text = text_file.read()
        tags = get_tags(text)

        wordcloud = WordCloud(max_font_size=200, font_path='D:\\jooho\\font\\NanumGothic.ttf',
                              background_color='#FFFFFF', width=1200, height=800).generate(tags)

        # 사이즈 등을 설정해 줍니다.

        plt.figure(figsize=(10, 8))

        plt.imshow(wordcloud)

        plt.tight_layout(pad=0)

        plt.axis('off')

        # 저장까지 해봅니다.

        plt.savefig('image_name.png', bbox_inches='tight')


        text_file.close()

    if __name__ == "__main__":
        main()