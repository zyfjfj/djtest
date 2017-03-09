# coding=utf-8
# 在字典里的都是计1分,186-是，187-否，188-不确定
# sphinx-apidoc -F -o C:\python_doc\numpy C:\Python27\Lib\site-packages\numpy
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont

# os.environ['DJANGO_SETTINGS_MODULE'] = 'scales.settings'
#from scale.models import Experimentrecord

L_scale_scores = {187: [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 195, 225, 255, 285]}

F_scale_scores = {187: [17, 20, 54, 65, 75, 83, 112, 113, 115, 164, 169, 177, 185, 196, 199, 220, 257, 258, 272, 276],
                  186: [14, 27, 31, 34, 35, 40, 42, 48, 49, 50, 53, 56, 66, 85, 121, 123, 139, 146, 151, 156, 168, 184,
                        197, 200, 202, 205, 206, 209, 210, 211, 215, 218, 227, 245, 246, 247, 252, 256, 269, 275, 286,
                        288, 291, 293]}

K_scale_scores = {186: [196],
                  187: [30, 39, 71, 89, 124, 129, 134, 138, 142, 148, 160, 170, 171, 180, 183, 217, 234, 267, 272, 296,
                        316, 322, 368, 370, 372, 373, 375, 386, 394]}
scale_scores = {"L": {187: [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 195, 225, 255, 285]},
                "F": {186: [14, 27, 31, 34, 35, 40, 42, 48, 49, 50, 53, 56, 66, 85, 121, 123, 139, 146, 151, 156, 168,
                            184,
                            197, 200, 202, 205, 206, 209, 210, 211, 215, 218, 227, 245, 246, 247, 252, 256, 269, 275,
                            286,
                            288, 291, 293],
                      187: [17, 20, 54, 65, 75, 83, 112, 113, 115, 164, 169, 177, 185, 196, 199, 220, 257, 258, 272,
                            276]},
                "K": {186: [196],
                      187: [30, 39, 71, 89, 124, 129, 134, 138, 142, 148, 160, 170, 171, 180, 183, 217, 234, 267, 272,
                            296,
                            316, 322, 368, 370, 372, 373, 375, 386, 394]},
                "1Hs": {186: [23, 29, 43, 62, 72, 108, 114, 125, 161, 189, 273],
                        187: [2, 3, 7, 9, 18, 51, 55, 63, 68, 103, 130, 153, 155, 163, 175, 188, 190, 192, 230, 243,
                              274, 281]},
                "2D": {
                    186: [5, 32, 41, 43, 52, 67, 86, 104, 130, 138, 142, 158, 159, 182, 189, 193, 236, 259, 288, 290],
                    187: [2, 8, 9, 18, 30, 36, 39, 46, 51, 57, 58, 64, 80, 88, 89, 95, 98, 107, 122, 131, 145, 152, 153,
                          154, 155, 160, 178, 191, 207, 208, 233, 241, 242, 248, 263, 270, 271, 272, 285, 296]},
                "3Hy": {
                    186: [10, 23, 32, 43, 44, 47, 76, 114, 179, 186, 189, 238, 253],
                    187: [2, 3, 6, 7, 8, 9, 12, 26, 30, 51, 55, 71, 89, 93, 103, 107, 109, 124, 128, 129, 136, 137, 141,
                          147, 153, 160, 162, 163, 170, 172, 174, 175, 180, 188, 190, 192, 201, 213, 230, 234, 243, 265,
                          267, 274, 279, 289, 292]},
                "4Pd": {
                    186: [16, 21, 24, 32, 33, 35, 38, 42, 61, 67, 84, 94, 102, 106, 110, 118, 127, 215, 216, 224, 239,
                          244, 245, 284],
                    187: [8, 20, 37, 82, 91, 96, 107, 134, 137, 141, 155, 170, 171, 173, 180, 183, 201, 231, 235, 237,
                          248, 267, 287, 289, 294, 296]},
                "5Mf-m": {
                    186: [4, 25, 69, 70, 74, 77, 78, 87, 92, 126, 132, 134, 140, 149, 179, 187, 203, 204, 217, 226, 231,
                          239, 261, 278, 282, 295, 297, 299],
                    187: [1, 19, 26, 28, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 133, 144, 176, 198, 213, 214, 219,
                          221, 223, 229, 249, 254, 260, 262, 264, 280, 283, 300]},
                "5Mf-f": {
                    186: [4, 25, 70, 74, 77, 78, 87, 92, 126, 132, 133, 134, 140, 149, 187, 203, 204, 217, 226, 239,
                          261, 278, 282, 295, 299],
                    187: [1, 19, 26, 28, 69, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 144, 176, 179, 198, 213, 214,
                          219, 221, 223, 229, 231, 249, 254, 260, 262, 264, 280, 283, 297, 300]},
                "6Pa": {
                    186: [16, 24, 27, 35, 110, 121, 123, 127, 151, 157, 158, 202, 275, 284, 291, 293, 299, 305, 314,
                          317, 326, 338, 341, 364, 365],
                    187: [93, 107, 109, 111, 117, 124, 268, 281, 294, 313, 316, 319, 327, 347, 348]},
                "8Sc": {
                    186: [15, 22, 40, 41, 47, 52, 76, 97, 104, 121, 156, 157, 159, 168, 179, 182, 194, 202, 210, 212,
                          238, 241, 251, 259, 266, 273, 282, 291, 297, 301, 303, 307, 308, 311, 312, 315, 320, 323, 324,
                          325, 328, 331, 332, 333, 334, 335, 339, 341, 345, 349, 350, 352, 354, 355, 356, 360, 363, 364,
                          366],
                    187: [17, 65, 103, 119, 177, 178, 187, 192, 196, 220, 276, 281, 302, 306, 309, 310, 318, 322, 330]},
                "7Pt": {
                    186: [10, 15, 22, 32, 41, 67, 76, 86, 94, 102, 106, 142, 159, 182, 189, 217, 238, 266, 301, 304,
                          321, 336, 337, 340, 342, 343, 344, 346, 349, 351, 352, 356, 357, 358, 359, 360, 361, 362,
                          366],
                    187: [3, 8, 36, 122, 152, 164, 178, 329, 353]},
                "9Ma": {
                    186: [11, 13, 21, 22, 59, 64, 73, 97, 100, 109, 127, 134, 143, 156, 157, 167, 181, 194, 212, 222,
                          226, 228, 232, 233, 238, 240, 250, 251, 263, 266, 268, 271, 277, 279, 298],
                    187: [101, 105, 111, 119, 120, 148, 166, 171, 180, 267, 289]},
                "0Si": {
                    186: [32, 67, 82, 111, 117, 124, 138, 147, 171, 172, 180, 201, 236, 267, 278, 292, 304, 316, 321,
                          332, 336, 342, 357, 360, 370, 373, 376, 378, 379, 385, 389, 393, 398, 399],
                    187: [25, 33, 57, 91, 99, 119, 126, 143, 193, 208, 229, 231, 254, 262, 281, 296, 309, 353, 359, 367,
                          371, 374, 377, 380, 381, 382, 383, 384, 387, 388, 390, 391, 392, 395, 396, 397]},
                "A": {
                    186: [32, 41, 67, 76, 94, 138, 147, 236, 259, 267, 278, 301, 305, 321, 337, 343, 344, 345, 356, 359,
                          368, 370, 372, 376, 414, 418, 431, 443, 461, 462, 465, 482, 499, 511, 518, 544, 549, 555],
                    187: [450]},
                "R": {
                    186: [],
                    187: [1, 6, 9, 12, 39, 51, 81, 112, 126, 131, 140, 145, 154, 156, 191, 208, 219, 221, 271, 272, 281,
                          282, 327, 375, 377, 380, 382, 383, 384, 387, 394, 429, 445, 447, 468, 472, 516, 529, 550,
                          556]},
                "MAS": {
                    186: [13, 14, 23, 31, 32, 43, 67, 86, 125, 142, 158, 186, 191, 217, 238, 241, 263, 301, 317, 321,
                          322, 335, 337, 340, 352, 361, 372, 398, 418, 424, 431, 439, 442, 499, 506, 530, 555],
                    187: [7, 18, 107, 163, 190, 230, 242, 264, 287, 367, 407, 520, 528]},
                "ES": {
                    186: [2, 36, 51, 95, 109, 153, 174, 181, 187, 192, 208, 221, 231, 234, 253, 270, 355, 400, 410, 430,
                          451, 458, 513, 515],
                    187: [14, 22, 32, 33, 34, 43, 48, 58, 62, 82, 94, 100, 132, 140, 189, 209, 217, 236, 241, 244, 251,
                          261, 341, 344, 349, 359, 420, 449, 462, 482, 483, 488, 489, 494, 510, 525, 541, 544, 548, 554,
                          555, 559, 561]},
                "Dy": {
                    186: [19, 21, 24, 41, 63, 67, 70, 82, 86, 98, 100, 138, 141, 158, 165, 180, 189, 201, 212, 236, 239,
                          259, 267, 304, 305, 321, 337, 338, 343, 357, 361, 362, 370, 372, 373, 393, 398, 399, 408, 440,
                          443, 461, 487, 488, 489, 509, 521, 531, 554],
                    187: [9, 79, 107, 163, 170, 193, 264, 411]},
                "Do": {
                    186: [64, 229, 255, 270, 406, 432, 523],
                    187: [32, 61, 82, 86, 94, 186, 223, 224, 240, 249, 250, 267, 268, 304, 343, 356, 419, 483, 547, 558,
                          562]},
                "Re": {
                    186: [58, 111, 173, 221, 294, 412, 501, 552],
                    187: [6, 28, 30, 33, 56, 116, 118, 157, 175, 181, 223, 224, 260, 304, 388, 419, 434, 437, 468, 471,
                          472, 529, 553, 558]},
                "Pr": {
                    186: [47, 84, 93, 106, 117, 124, 136, 139, 157, 171, 186, 250, 280, 304, 307, 313, 319, 323, 338,
                          349, 375, 376, 388, 435, 436, 437, 485, 543, 547],
                    187: [78, 176, 221]},
                "St": {
                    186: [78, 118, 126, 149, 199, 204, 229, 237, 289, 396, 430, 441, 452, 491, 513],
                    187: [136, 138, 180, 213, 249, 267, 280, 297, 304, 314, 352, 365, 378, 448, 449, 480, 481, 488,
                          324]},
                "Cn": {
                    186: [6, 20, 30, 56, 67, 105, 116, 134, 145, 162, 169, 181, 225, 236, 238, 285, 296, 319, 337, 376,
                          379, 381, 418, 447, 460, 461, 529, 555],
                    187: [58, 80, 92, 96, 111, 167, 174, 220, 242, 249, 250, 291, 313, 360, 439, 444, 449, 483, 488,
                          489, 527, 548]},
                }


# 获得效度，序号-282
def validity(**kwargs):
    '''

    :param kwargs: 字典类型，key:题目id,value:答案id
    :return:
    '''
    score_dic = {"Q": 0}
    for key in scale_scores.keys():
        score_dic[key] = 0
    score_l = 0
    score_f = 0
    score_k = 0
    for item_id in kwargs.keys():
        answer_id = kwargs[item_id]
        if answer_id == 188:
            score_dic["Q"] = score_dic["Q"] + 1
        item_id = int(item_id) - 282
        for scale_score in scale_scores.keys():
            for scale_answer in scale_scores[scale_score].keys():
                if answer_id == scale_answer:
                    if item_id in scale_scores[scale_score][scale_answer]:
                        score_dic[scale_score] = score_dic[scale_score] + 1
        '''if answer_id == 187:
            if item_id in L_scale_scores[187]:
                score_l = score_l + 1
            if item_id in F_scale_scores[187]:
                score_f = score_f + 1
            if item_id in K_scale_scores[187]:
                score_k = score_k + 1
        if answer_id == 186:
            if item_id in F_scale_scores[186]:
                score_f = score_f + 1
            if item_id in K_scale_scores[186]:
                score_k = score_k + 1'''
    return score_dic, 1


def Analysis(experimentrecords, age=26):
    age = age - 22
    if age < 0:
        age = 0
    maxtime = 0.0
    Interpic = "M0000.jpg"
    if isinstance(experimentrecords, list):
        experimentrecords = list(experimentrecords)
    varmy = np.zeros((2, 2, 2), dtype=np.double)
    meanmy = np.zeros((2, 2, 2), dtype=np.double)
    listmy = np.zeros((2, 2, 2), dtype=int)
    allmy = {'00': [], '01': [], '10': [], '11': []}
    for record in experimentrecords:
        record.trialtime = record.trialtime - age * 0.01
        if record.trialtime < 2.5 and record.trialtime > 0.2 and record.judgement == 1:
            if record.trialtime > maxtime and record.scenenature == 0:
                maxtime = record.trialtime
                Interpic = record.scenename + ".jpg"
            a = record.scenenature * 2 + record.facenature
            if a == 0:
                allmy['00'].append(record.trialtime)
            if a == 1:
                allmy['01'].append(record.trialtime)
            if a == 2:
                allmy['10'].append(record.trialtime)
            if a == 3:
                allmy['11'].append(record.trialtime)
    temp = np.zeros((2), dtype=np.double)
    for i in range(0, 2):
        for j in range(0, 2):
            if allmy[str(i) + str(j)]:
                temp = np.array([np.array(allmy[str(i) + str(j)]).mean(), np.array(allmy[str(i) + str(j)]).var()])
            meanmy[i][j][0] = temp[0]
            varmy[i][j][0] = temp[1]
            listmy[i][j][0] = len(allmy[str(i) + str(j)])
    for i in range(0, 2):
        for j in range(0, 2):
            n = len(allmy[str(i) + str(j)])
            l = 0
            for k in range(0, n):
                low = meanmy[i, j, 0] * 0.6
                high = meanmy[i, j, 0] * 1.4
                if allmy[str(i) + str(j)][l] > high or allmy[str(i) + str(j)][l] < low:
                    allmy[str(i) + str(j)].remove(allmy[str(i) + str(j)][l])
                else:
                    l = l + 1
    temp = np.zeros((2), dtype=np.double)
    for i in range(0, 2):
        for j in range(0, 2):
            if allmy[str(i) + str(j)]:
                temp = np.array([np.array(allmy[str(i) + str(j)]).mean(), np.array(allmy[str(i) + str(j)]).var()])
            meanmy[i][j][1] = temp[0]
            varmy[i][j][1] = temp[1]
            listmy[i][j][1] = len(allmy[str(i) + str(j)])
    output = np.zeros((4, 2, 2), dtype=np.double)
    for i in range(0, 2):
        for j in range(0, 2):
            output[0][i][j] = meanmy[i][j][1]
            output[1][i][j] = varmy[i][j][1]
            output[2][i][j] = listmy[i][j][0]
            output[3][i][j] = listmy[i][j][1]
    return output


def plotshizi(draw, x, y):
    '''十字'''
    draw.line((x, y - 10, x, y + 10), fill=(255, 23, 140, 255), width=1)
    draw.line((x - 1, y - 10, x - 1, y + 10), fill=(255, 23, 140, 255), width=1)
    draw.line((x - 1, y - 10, x - 1, y + 10), fill=(255, 23, 140, 255), width=1)
    draw.line((x - 10, y, x + 10, y), fill=(255, 23, 140, 255), width=1)
    draw.line((x - 10, y - 1, x + 10, y - 1), fill=(255, 23, 140, 255), width=1)
    draw.line((x - 10, y + 1, x + 10, y + 1), fill=(255, 23, 140, 255), width=1)


def result(input):
    h = 1500
    w = 1100
    low = np.array([686, 704, 703, 715])
    higth = np.array([782, 791, 791, 822])
    img = Image.new("RGBA", (w, h), (255, 255, 255))
    y1 = 500
    iCount = 0
    startnum = 200
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc', 25)
    fnt10 = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc', 10)
    fnt12 = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc', 12)
    fnt18 = ImageFont.truetype('C:\\WINDOWS\\Fonts\\simsun.ttc', 18)

    draw.line((0, y1, w - 2, y1), fill=(0, 0, 0, 255), width=1)
    draw.line((0, y1 - 100, w - 2, y1 - 100), fill=(0, 0, 0, 255), width=1)
    draw.line((0, y1 - 200, w - 2, y1 - 200), fill=(0, 0, 0, 255), width=1)
    draw.line((0, y1 - 300, w - 2, y1 - 300), fill=(0, 0, 0, 255), width=1)
    draw.text((450, 20), u"心理状态评估", font=fnt, fill=(0, 0, 0, 255))
    draw.text((20, 100), u"认知速度（Cognitive Speed）", font=fnt18, fill=(0, 0, 0, 255))
    draw.line((100, y1 + 10, 100, y1 - 10), fill=(0, 0, 0, 255), width=1)

    for iIndex in range(100, w - 110, 10):
        iCount += 1
        if iCount != 5:
            draw.line((iIndex + 10, y1 + 5, iIndex + 10, y1 - 5), fill=(0, 0, 0, 255), width=1)  # 负背景负表情正常
            draw.line((iIndex + 10, y1 - 100 + 5, iIndex + 10, y1 - 100 - 5), fill=(0, 0, 0, 255), width=1)
            draw.line((iIndex + 10, y1 - 200 + 5, iIndex + 10, y1 - 200 - 5), fill=(0, 0, 0, 255), width=1)
            draw.line((iIndex + 10, y1 - 300 + 5, iIndex + 10, y1 - 300 - 5), fill=(0, 0, 0, 255), width=1)
        else:
            draw.line((iIndex + 10, y1 + 10, iIndex + 10, y1 - 10), fill=(0, 0, 0, 255), width=1)
            draw.text((iIndex, y1 + 10), str(startnum + iIndex + 10), font=fnt12, fill=(0, 0, 0, 255))
            draw.line((iIndex + 10, y1-100 + 10, iIndex + 10, y1 - 100-10), fill=(0, 0, 0, 255), width=1)
            draw.text((iIndex, y1 -100+ 10), str(startnum + iIndex + 10), font=fnt12, fill=(0, 0, 0, 255))
            draw.line((iIndex + 10, y1-200 + 10, iIndex + 10, y1 - 200-10), fill=(0, 0, 0, 255), width=1)
            draw.text((iIndex, y1 -200+ 10), str(startnum + iIndex + 10), font=fnt12, fill=(0, 0, 0, 255))
            draw.line((iIndex + 10, y1-300 + 10, iIndex + 10, y1 - 300-10), fill=(0, 0, 0, 255), width=1)
            draw.text((iIndex, y1 -300+ 10), str(startnum + iIndex + 10), font=fnt12, fill=(0, 0, 0, 255))
            iCount = 0
    cognitiveSpeedText(draw, fnt10, w, y1, [u"正常", u"异常", u"负背景", u"负表情"])
    cognitiveSpeedText(draw, fnt10, w, y1 - 100, [u"正常", u"异常", u"负背景", u"正表情"])
    cognitiveSpeedText(draw, fnt10, w, y1 - 200, [u"正常", u"异常", u"正背景", u"负表情"])
    cognitiveSpeedText(draw, fnt10, w, y1 - 300, [u"正常", u"异常", u"正背景", u"正表情"])
    splitLine(draw,fnt12)
    myspeed = np.zeros(4)
    for i in range(0, 2):
        for j in range(0, 2):
            myspeed[i * 2 + j] = (int)(input[0][i][j] * 1000)
    len = 4
    for id in range(0, len):
        x = myspeed[id]
        y = 500 - id * 100
        x = x - startnum
        plotshizi(draw, x, y)
        draw.text((x - 10, y + 20), str(x + startnum), font=fnt10, fill=(0, 0, 0, 255))

    # 认知度
    draw.text((20, 600), u"认知辨识度（Cognitive Identification）", font=fnt18, fill=(0, 0, 0, 255))
    mycolor = np.zeros(4)
    minus = np.zeros(4)
    minus[0] = myspeed[0] - myspeed[1]  # NN-NP
    minus[1] = myspeed[1] - myspeed[3]  ##NP-PP
    minus[2] = myspeed[3] - myspeed[2]  ##PP-PN
    minus[3] = myspeed[2] - myspeed[0]  ##PN-NN
    for id in range(0, 4):
        x = int(minus[id])
        answer = ""
        if x <= -50:
            answer = u"快于"
        elif x >= 50:
            answer = u"慢于"
        else:
            answer = u"适中"
        draw.text((450, 750 + id * 50), answer, font=fnt18, fill=(0, 0, 0, 255))
        draw.text((300, 750 + id * 50), str(x), font=fnt18, fill=(0, 0, 0, 255))
        draw.text((50, 750), u"负背景辨识度（NN-NP）", font=fnt18, fill=(0, 0, 0, 255))
        draw.text((50, 800), u"正表情辨识度（NP-PP）", font=fnt18, fill=(0, 0, 0, 255))
        draw.text((50, 850), u"正背景辨识度（PP-PN）", font=fnt18, fill=(0, 0, 0, 255))
        draw.text((50, 900), u"负表情辨识度（PN-NN）", font=fnt18, fill=(0, 0, 0, 255))
    reliability(draw,fnt12,input)
    img.show()
    img.save("1.png")


def cognitiveSpeedText(draw, fnt10, w, y1, text_list):
    '''写认知速度的文字'''
    draw.text((0, y1 - 20), text_list[0], font=fnt10, fill=(0, 0, 0, 255))
    draw.text((w - 100, y1 - 20), text_list[1], font=fnt10, fill=(0, 0, 0, 255))
    draw.text((0, y1 - 60), text_list[2], font=fnt10, fill=(0, 0, 0, 255))
    draw.text((0, y1 - 40), text_list[3], font=fnt10, fill=(0, 0, 0, 255))


def splitLine(draw, font,lows=[686, 704, 703, 715], highs=[782, 791, 791, 822],rgb=(250,0,0,255)):
    '''画分割线'''
    for i,low in enumerate(lows):
        draw.line((low - 200, 170 + i * 100, low - 200, 240 + i * 100), fill=rgb, width=1)
        draw.line((highs[i] - 200, 170 + i * 100, highs[i] - 200, 240 + i * 100), fill=rgb, width=1)
        draw.text((low - 220, 180 + i * 100), str(low), font=font, fill=(0, 0, 0, 255))
        draw.text((highs[i] - 200, 180 + i * 100), str(highs[i]), font=font, fill=(0, 0, 0, 255))
def reliability(draw,fnt,input):
    '''信度'''
    myvar = np.zeros(4)
    for i in range(0, 2):
        for j in range(0, 2):
            myvar[i * 2 + j] = input[1][i][ j]
    for id in range(0, 4):
        x = ((np.double)((int)(myvar[id]*1000)))/1000
        answer = ""
        if x <= 0.1:
            answer = u"正常"
        else:
            answer = u"异常"
        draw.text((850, 1250 - id * 50), str(x), font=fnt, fill=(0, 0, 0, 255))
        draw.text((1000, 1250 - id * 50), answer, font=fnt, fill=(0, 0, 0, 255))
    return myvar
def matlib():
    import matplotlib.pyplot as plt
    plt.rcdefaults()
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('Agg')
    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, people)
    plt.xlabel('Performance')
    plt.title('How fast do you want to go today?')

    plt.savefig('MyFig.jpg')
'''def wirte_excel(objs):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'YYYY-MM-DD'

    # 设置第一列位为10
    ws.write(0, 0, u'序号')
    ws.col(0).width = 1620
    ws.write(0, 1, u'题目')
    ws.col(1).width = 5115
    ws.write(0, 2, u'答案')


    i = 1
    for obj in objs:
        ws.write(i, 0, i)
        ws.write(i, 1, obj['id'])
        ws.write(i, 2, obj['item'])
        ws.write(i, 3, obj['answer'])
        i += 1
    wb.save('itme_answer.xls')'''

