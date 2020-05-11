
import os


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
    _n_title = ''
    conv_result = []
    for cont in _chart_name:
        if 'Allen' in cont:
            _n_title = 'Allen'
        elif 'Tom' in cont:
            _n_title = "Tom"
        else:
            conv_result.append([_n_title , cont])
    return conv_result

def main():
    result = open_file('input.txt')
    c_result = convert(result)
    write_file('output.txt' , c_result)

main()
