# script to create a combined list of kanji, hanzi and hanja
import re


def get_kanji():
    with open('../../kanji_dashboard/data/joyo_quick.txt', encoding='utf8') as file:
        for line in file.readlines():
            line = line.rstrip()
            if len(line.split('\t')) != 4:
                print(line, line.split('\t'))
            eng_meaning, kanji, reading, name = line.split('\t')
            yield kanji, reading, name


def get_hsk_hanzi():
    with open('../../hanzi_dashboard/lists/hsk_list.txt', encoding='utf8') as file:
        for line in file.readlines():
            line = line.rstrip()
            if len(line.split('\t')) != 8:
                print(line, line.split('\t'))
            hanzi, pinyin, definition, radical, stroke_number, hsk_level, general_standard, frequency_rank = \
                line.split('\t')
            yield hanzi, pinyin, definition


def get_simpl_to_trad():
    with open('../../hanzi_dashboard/lists/wenlin_freq.txt', encoding='utf8') as file:
        for line in file.readlines()[2:]:
            line = line.rstrip()
            if len(line.split('\t')) != 4:
                print(line, line.split('\t'))
            simplified,	traditional, pinyin, meaning = line.split('\t')
            yield simplified, traditional


def get_yarxi_names():
    with open('../../hanzi_dashboard/python/yarxi_names.txt', encoding='utf8') as file:
        for line in file.readlines()[:]:
            line = line.rstrip()
            if len(line.split('\t')) != 3:
                #print(line, line.split('\t'))
                kanji, name = line.split('\t')
                meaning = ''
            else:
                kanji, name, meaning = line.split('\t')
            yield kanji, name, meaning


def simplified_to_trad():
    kanji = dict((kanji, (reading, name)) for kanji, reading, name in get_kanji())
    raw_hanzi = list(get_hsk_hanzi())
    hanzi = dict((hanzi, (pinyin, definition)) for hanzi, pinyin, definition in raw_hanzi)
    hanzi_by_freq = [hanzi for hanzi, pinyin, definition in raw_hanzi if len(hanzi)]
    trad_to_simpl = {}
    for trad in simplified, trad in get_simpl_to_trad():
        for ch in trad:
            trad_to_simpl[ch] = simplified

    for index, hanzi in enumerate(hanzi_by_freq):
        pinyin, eng_definition = hanzi[hanzi]
        trad = simpl_to_trad.get(hanzi, '')
        if hanzi not in kanji:
            #print(f'{index+1}\t{hanzi}\t{simpl_to_trad[hanzi]}')
            print(f'{hanzi}\t{simpl_to_trad[hanzi]}')


def get_trad_hsk_hanzi():
    with open('../../hanzi_dashboard/python/hsk_list_trad_hanzi_only.txt', encoding='utf8') as file:
        for line in file.readlines()[1:]:
            hanzi = line.rstrip()
            yield hanzi


def get_hanja_reading():
    with open('../../hanja_dashboard/lists/exam_hanja_list.txt', encoding='utf8') as file:
        for line in file.readlines()[1:]:
            hanzi, reading, meaning, grade = line.rstrip().split('\t')
            yield hanzi, reading


def do_smth():
    for hanja in trad_hsk_hanzi[:]:
        if len(hanja) == 1:
            print(hanja_reading.get(hanja, ''))
        else:
            for ch in hanja:
                if ch in hanja_reading:
                    print(hanja_reading.get(ch, ''))
                    break
            else:
                print('')


def get_trad_kanji():
    with open('../../hanzi_dashboard/python/old_kanji.txt', encoding='utf8') as file:
        for line in file.readlines():
            line = line.rstrip()
            new, old = line.split('\t')
            yield old, new


variants = {
    '敎': '教',
    '靑': '青',
    '內': '内',
    '每': '毎',
    '淸': '清',
    '綠': '緑',
    '溫': '温',
    '黃': '黄',
    '德': '徳',
    '歷': '歴',
    '說': '説',
    '歲': '歳',
    '黑': '黒',
    '錄': '録',
    '步': '歩',
    '狀': '状',
    '稅': '税',
    '硏': '研',
    '增': '増',
    '鄕': '郷',
    '虛': '虚',
    '戶': '戸',
    '擊': '撃',
    '緣': '縁',
    '脫': '脱',
    '槪': '概',
    '寬': '寛',
    '郞': '郎',
    '曆': '暦',
    '鍊': '錬',
    '賴': '頼',
    '尙': '尚',
    '緖': '緒',
    '悅': '悦',
    '卽': '即',
    '徵': '徴',
    '橫': '横',
    '渴': '渇',
    '繫': '繋',
    '俱': '倶',
    '旣': '既',
    '畓': '畔',
    '淚': '涙',
    '屢': '屡',
    '屛': '屏',
    '涉': '渉',
    '閱': '閲',
    '銳': '鋭',
    '娛': '娯',
    '玆': '滋',
    '毁': '毀',
   # '珏': '',
    '鉀': '甲',
   # '塏': '',
    '揭': '掲',
   # '璟': '',
   # '炅': '',
   # '儆': '',
   # '琯': '',
    '鷗': '鴎',
  #  '琪': '',
  #  '璣': '',
  #  '琦': '',
    '燾': '濤', #???
  #  '乭': '',
 #   '鄧': '',
    '萊': '莱',
  #  '樑': '',
    '沔': '',
    '汶': '',
    '珉': '',
    '玟': '',
    '旼': '',
    '磻': '',
    '龐': '',
    '裵': '',
    '昞': '',
    '昺': '',
    '倂': '併',
    '潽': '',
    '毖': '',
    '揷': '挿',
    '晳': '皙',
    '奭': '',
    '瑄': '',
    '璇': '',
    '璿': '',
    '卨': '',
    '巢': '巣',
    '珣': '',
    '湜': '',
    '倻': '',
    '姸': '',
    '燁': '',
    '芮': '',
    '濊': '',
    '吳': '呉',
    '鈺': '',
    '邕': '',
    '瑢': '',
    '鏞': '',
    '頊': '',
    '昱': '',
    '煜': '',
    '瑗': '',
    '庾': '',
    '鈗': '',
    '誾': '',
    '佾': '',
    '蔣': '',
    '獐': '',
    '楨': '',
    '珽': '',
    '曺': '',
    '琮': '',
    '埈': '',
    '晙': '',
    '璨': '',
    '瓚': '',
    '埰': '',
    '澈': '',
    '喆': '',
    '沆': '',
    '爀': '',
    '炫': '',
    '峴': '',
    '邢': '',
    '瀅': '',
    '澔': '',
    '祜': '',
    '嬅': '',
    '壎': '',
    '薰': '',
    '姬': '姫',
}


def create_hanja_with_yarxi_meaning():
    re_reading = re.compile(r' ?\(«.+?»\)')
    hanja_reading = list(get_hanja_reading())

    yarxi = dict((kanji, (name, meaning)) for kanji, name, meaning in get_yarxi_names())
    old_kanji = dict(get_trad_kanji())
    for hanja, reading in hanja_reading:
        hanja_lookup = old_kanji.get(hanja, hanja)
        name_meaning = yarxi.get(hanja_lookup)
        if name_meaning is None:
            new_kanji = variants.get(hanja_lookup)
            name_meaning = yarxi.get(new_kanji)

        hangul = reading.replace(':', '').replace('-', '')
        if name_meaning is not None:
            no_reading = re_reading.sub('', name_meaning[1])
            print(f'{hanja}\t{hangul}\t{name_meaning[0]}\t{no_reading}')
            #break
        else:
            print(f'{hanja}\t{hangul}\t\t')


create_hanja_with_yarxi_meaning()
