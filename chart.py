
import os


def write_file(filename, _chart_log):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for p in _chart_log:
            f.write(p[0] + ':' + p[1] + '\n')

def open_file(o_filename):
    data = []
    _chart_name = []
    _n_title = ''
    with open(o_filename, 'r' , encoding = 'UTF-8') as f:
        for line in f:
            _chart_name = line.strip()
            if 'Allen' in _chart_name:
                _n_title = 'Allen'
            elif 'Tom' in _chart_name:
                _n_title = "Tom"
            else:
                data.append([_n_title ,_chart_name])
    return data

def main():
    result = open_file('input.txt')
    write_file('output.txt' , result)

main()
