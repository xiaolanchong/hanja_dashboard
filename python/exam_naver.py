# All levels: https://hanja.dict.naver.com/level

import os
import pprint
import collections

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


def read_data(filename, grade, read_hanja: set):
    #filename = '6-2.txt'
    records = []
    with open(os.path.join('exam', filename), encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            hanja = line[0]
            if not is_hanja(hanja):
                if hanja not in compatibility:
                    print(f'{line}: incorrect format, {hex(ord(hanja))}')
                else:
                    hanja = compatibility[hanja]
            parts = line[1:].split(',')
            readings = []
            for part in parts:
                part = part.strip()
                reading_sound = None
                same_sound_meanings = ''
                for slashes in part.split('/'):
                    space_pos = slashes.rindex(' ')
                    if reading_sound is not None:
                        if slashes[space_pos + 1:] != reading_sound:
                            print(f'====== {reading_sound} vs {slashes[space_pos + 1:]}')
                            assert(false)
                    reading_sound = slashes[space_pos + 1:]
                    if len(same_sound_meanings):
                        same_sound_meanings += ', '
                    same_sound_meanings += slashes[:space_pos]
                    #readings.append((slashes[:space_pos], slashes[space_pos + 1:]))
                readings.append(Record(reading=reading_sound, meaning=same_sound_meanings))
            if hanja not in read_hanja:
                records.append((hanja, grade, readings))
                read_hanja.add(hanja)
    return records


def write_txt(records, filename):
    with open(filename, mode='w', encoding='utf8') as f:
        for hanja, grade, readings in records:
            readings_all = ', '.join(reading for reading, meaning in readings)
            if len(readings) > 1:
                meanings = ', '.join(f'[{reading}] {meaning}' for reading, meaning in readings)
            else:
                meanings = readings[0].meaning
            f.write(f'{hanja}\t{readings_all}\t{meanings}\t{grade}\n')


def write_main():
    read_hanja = set()
    records = []
    records += read_data('8.txt', 8, read_hanja)
    records += read_data('7-2.txt', 7, read_hanja)
    records += read_data('7-1.txt', 7, read_hanja)
    records += read_data('6-2.txt', 6, read_hanja)
    records += read_data('6-1.txt', 6, read_hanja)
    records += read_data('5-2.txt', 5, read_hanja)
    records += read_data('5-1.txt', 5, read_hanja)
    records += read_data('4-2.txt', 4, read_hanja)
    records += read_data('4-1.txt', 4, read_hanja)
    records += read_data('3-2.txt', 3, read_hanja)
    records += read_data('3-1.txt', 3, read_hanja)
    records += read_data('2.txt', 2, read_hanja)
    records += read_data('1.txt', 1, read_hanja)
    #pprint.pprint(records)
    write_txt(records, 'hanja_main.txt')


def write_special():
    read_hanja = set()
    records = []
    records += read_data('0-special-2.txt', 's2', read_hanja)
    records += read_data('0-special.txt', 's', read_hanja)
    #pprint.pprint(records)
    write_txt(records, 'hanja_special.txt')

write_main()
write_special()