#coding=utf-8
import os
import sys

import qrcode
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from mydj.forms import NameForm, RemarkForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def message(request):
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RemarkForm()

    return render(request, 'name.html', {'form': form})
if __name__=="__main__":
    from PIL import Image, ImageDraw,ImageFont

    qr_img = qrcode.make("http://60.205.57.100:8543/android_files/qwqw.png")
    qr_img.save("qt.png")
    # qr_img=Image.open("qt.png")
    # qr_img=qr_img.resize((256,256),Image.ANTIALIAS)
    # os.remove('qt.png')
    # log_img=Image.open("wd.jpg")
    # base_img = Image.new("RGBA", (640, 480), (255, 255, 255))
    # base_img.paste(qr_img, (330, 30))
    # base_img.paste(log_img,(30,40))
    # # get an image
    # base = base_img.convert('RGBA')
    # # make a blank image for the text, initialized to transparent text color
    # txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    #
    # # get a font
    # fnt = ImageFont.truetype('FZYTK.TTF', 25)
    # # get a drawing context
    # d = ImageDraw.Draw(txt)
    #
    # # draw text, half opacity
    # d.text((20, 260), u"111：123124", font=fnt, fill=(0, 0, 0, 255))
    # d.text((20, 300), u"11：18", font=fnt, fill=(0, 0, 0, 255))
    # # draw text, full opacity
    # d.text((20, 340),u"111:100", font=fnt, fill=(0, 0, 0, 255))
    # d.text((400, 300), u"11111111", font=fnt, fill=(0, 0, 0, 255))
    # #d.line((320,0,320,640),fill=(0,0,0,255),width=1)
    #
    # for i in range(0,640,5):
    #     d.point((320,0+i,320,640), fill=(0,0,0,255))
    # out = Image.alpha_composite(base, txt)
    # out.show()
    # out.convert('1',palette=Image.ADAPTIVE,colors=1).save("qr.bmp")
