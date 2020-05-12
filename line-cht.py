
#import os #無使用到檔案檢查

def write_file(filename, _chart_log):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for p in _chart_log:
            f.write(p[0] + ':' + p[1] + '\n')


def open_file(o_filename):
    data = []
    with open(o_filename, 'r' , encoding = 'UTF-8-sig') as f:
        for line in f:
            lines = line.strip()
            data.append(lines)
    return data


def convert(_chart_name):
    #s = []
    name = []
    time = []
    allen_word_count = 0
    allen_sticker_count  = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for cont in _chart_name:
        s = cont.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1    
            else:
                for m in s[2:]:
                    allen_word_count += len(m)   
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
                    
    print('viki說了', viki_word_count,'個字,傳了', viki_sticker_count, '張貼圖', viki_image_count, '張圖片')
    print('Allen說了', allen_word_count, '個字,傳了', allen_sticker_count, '張貼圖', allen_image_count, '張圖片')  
   # return conv_result


def main():
    result = open_file('LINE-Viki.txt')
    result = convert(result)
    #write_file('output.txt' , result)

main()
