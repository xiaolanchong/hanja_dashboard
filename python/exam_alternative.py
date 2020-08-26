
import os
import pprint
import collections
import functools
import re

Record = collections.namedtuple('Record', 'reading meaning')

def is_hanja(sym):
    return 0x4E00 <= ord(sym) <= 0x9FFF

def read_compatibility_map():
    filename = 'compatibilty_map.txt'
    mapping = {}
    with open(filename, encoding='utf8') as f:
        for line in f.readlines():
            parts = line.split(' ')
            if parts[2] == '?':
                continue
            from_cjk = chr(int(parts[0], 16))
            to_cjk = chr(int(parts[2], 16))
            mapping[from_cjk] = to_cjk
    return mapping


compatibility = read_compatibility_map()

def read_data(filename, grade, read_hanja=None):
    def start(fline):
        if len(fline) == 0:
            return start
        elif len(fline) == 1:
            current_hanja = fline[0]
            if not is_hanja(current_hanja):
                if current_hanja not in compatibility:
                    print(f'{line}: incorrect format, {hex(ord(current_hanja))}')
                else:
                    current_hanja = compatibility[current_hanja]
            return functools.partial(hanja_read, current_hanja)
        else:
            print(fline)
            assert False

    def info_read(hanja, info, fline):
        parts = fline.split('|')
        hanja_records = []
        for part in parts:
            part = part.strip()
            if ' ' not in part:
                print(hanja, fline)
                assert False
            space = part.rindex(' ')
            reading = part[space+1:]
            meaning = part[:space]
            hanja_records.append(Record(reading, meaning))
        rec = (hanja, hanja_records[0] if len(hanja_records) == 1 else hanja_records, info, grade)
        if hanja in read_hanja:
            #print(f'---------- {hanja} already read ----------------------------')
            pass
        else:
            records.append(rec)
            read_hanja.add(hanja)
        return start

    def hanja_read(hanja, fline):
        m = re.match('부수:(.) \| 총획:(\d{1,2})획', fline)
        if m is None:
            print(hanja, fline)
            assert False
        radical = m.group(1)
        strokes = int(m.group(2))
        return functools.partial(info_read, hanja, (radical, strokes))

    read_hanja = read_hanja if read_hanja is not None else set()
    records = []
    with open(os.path.join('exam2', filename), encoding='utf8') as f:
        current_state = start
        for line in f.readlines():
            line = line.strip()
            current_state = current_state(line)
    return records

def print_records(filename, records):
    with open(filename, mode='w', encoding='utf8') as f:
        for record in records:
            hanja, recs, info, grade = record
            if isinstance(recs, list):
                readings = ', '.join(reading for reading, meaning in recs)
                meanings = ', '.join(f'[{reading}] {meaning}' for reading, meaning in recs)
            else:
                readings, meanings = recs
            f.write(f'{hanja}\t{readings}\t{meanings}\t{grade}\t{info[0]}\t{info[1]}\n')


def write_main():
    records = []
    all_hanja = set()
    records += read_data('8.txt',   8, all_hanja)
    records += read_data('7-2.txt', 7, all_hanja)
    records += read_data('7.txt',   7, all_hanja)
    records += read_data('6-2.txt', 6, all_hanja)
    records += read_data('6.txt',   6, all_hanja)
    records += read_data('5-2.txt', 5, all_hanja)
    records += read_data('5.txt',   5, all_hanja)
    records += read_data('4-2.txt', 4, all_hanja)
    records += read_data('4.txt',   4, all_hanja)
    records += read_data('3-2.txt', 3, all_hanja)
    records += read_data('3.txt',   3, all_hanja)
    records += read_data('2.txt',   2, all_hanja)
    records += read_data('1.txt',   1, all_hanja)
    #pprint.pprint(records)
    print_records('hanja_main_alt.txt', records)

write_main()
