
import jinja2
import os

def is_hiragana(sym):
    return 0x3040 <= ord(sym) <= 0x309f

class KanjiDict:
    def __init__(self):
        self.meanings = {}
        with open('kanji.dat', encoding='utf8') as f:
            for line in f.readlines():
                parts = line.split('|')
                kanji, chinese, onkun, nanori, bushumei, english = parts
                hiragana_start = next((i for i, sym in enumerate(onkun) if is_hiragana(sym)), None)
                on = onkun[:hiragana_start] if hiragana_start is not None else onkun
                on = on.strip()
                #on.split(' ')
                self.meanings[kanji] = (english, on)
        variants = {
            '敎': '教',
            '靑': '青',
            '內': '内',
            '淸': '清',
            '說': '説',
            '歲': '歳',
            '稅': '税',
            '戶': '戸',
            '脫': '脱',
            '尙': '尚',
            '悅': '悦',
            '旣': '既',
            '畓': '',
            '閱': '閲',
            '銳': '鋭',
            '娛': '娯',
            '毁': '毀',
            '乭': '',
            '卨': '',
            '吳': '呉',
            '嬅': '',
            '姬': '',
            '癎': '',
            '媤': '',
            '篡': '',
        }
        for key, value in variants.items():
            if len(value):
                self.meanings[key] = self.meanings[value]

    def get_meaning(self, kanji):
        meaning = self.meanings.get(kanji)
        #if meaning is None:
        #    print(f"'{kanji}': '', ")
        return ' '.join(meaning) if meaning is not None else None


def read_exam_hanja():
    grade_styles = {
        8: 1,
        7: 2,
        6: 3,
        5: 4,
        4: 5,
        3: 6,
        2: 'S',
        1: 'S'
    }
    kanji_dict = KanjiDict()
    with open(os.path.join('..', 'lists', 'exam_hanja_list.txt'), encoding='utf8') as f:
        for line in f.readlines()[1:]:
            hanja, readings, meanings, grade = line.split('\t')
            readings = readings.replace(':', '').replace('-', '')
            eng_meaning = kanji_dict.get_meaning(hanja)
            meanings = meanings + '; ' + eng_meaning if eng_meaning else meanings
            yield hanja, readings, meanings, int(grade), grade_styles[int(grade)]


def str_to_list(hanja_str):
    if len(hanja_str.strip()) == 0:
        return []
    else:
        return list(ch.strip() for ch in hanja_str.split(','))


def read_school_hanja():
    with open(os.path.join('..', 'lists', 'school_hanja_list.txt'), encoding='utf8') as f:
        for line in f.readlines()[1:]:
            syllable, mid_school, high_school = line.split('\t')
            yield syllable, str_to_list(mid_school), str_to_list(high_school)


def generate_school_hanja(env):
    mid_high_school_tmpl = env.get_template('midhighschool.template.html')
    data = read_school_hanja()
    # print(list(data))
    html = mid_high_school_tmpl.render(records=data)
    with open(os.path.join('..', 'index.html'), mode='w', encoding='utf8') as file:
        file.write(html)


def generate_exam_hanja(env):
    exam_tmpl = env.get_template('exam_hanja.template.html')
    data = list(read_exam_hanja())
    # print(list(data))
    html = exam_tmpl.render(records=data)
    with open(os.path.join('..', 'exam_hanja.html'), mode='w', encoding='utf8') as file:
        file.write(html)

glob_env = jinja2.Environment(
    loader=jinja2.PackageLoader('create_dashboard', package_path=os.path.join('..', 'template')),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

generate_school_hanja(glob_env)
generate_exam_hanja(glob_env)
