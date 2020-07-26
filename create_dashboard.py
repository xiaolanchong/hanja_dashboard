
import jinja2


def read_exam_hanja():
    with open('exam_hanja_list.txt', encoding='utf8') as f:
        for line in f.readlines()[1:]:
            hanja, readings, meanings, grade = line.split('\t')
            return hanja, readings, meanings, grade


def str_to_list(hanja_str):
    if len(hanja_str.strip()) == 0:
        return []
    else:
        return list(ch.strip() for ch in hanja_str.split(','))


def read_school_hanja():
    with open('school_hanja_list.txt', encoding='utf8') as f:
        for line in f.readlines()[1:]:
            syllable, midschool, highschool = line.split('\t')
            yield syllable, str_to_list(midschool), str_to_list(highschool)


env = jinja2.Environment(
    loader=jinja2.PackageLoader('create_dashboard', package_path='template'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

mid_high_school_tmpl = env.get_template('midhighschool.template.html')

data = read_school_hanja()
#print(list(data))
html = mid_high_school_tmpl.render(records=data)
with open('index.html', mode='w', encoding='utf8') as file:
    file.write(html)

