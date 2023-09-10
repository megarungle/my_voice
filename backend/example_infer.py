from src.core import Core

from typing import List
from src.structs import InferStatus, Data


class Infer:
    def get_redirect_url(self, _input):
        core = Core()
        print("Waiting for infer request")
        status, data = core.infer(_input)
        if status is InferStatus.status_ok:
            for answer in data:
                answer.data_print()
        return "new_url"


if __name__ == "__main__":
    infer = Infer()
    _input = {
        "id": 23097,
        "question": "Напишите свою ассоциацию со словом \"бюрократ\"",
        "answers": [
            {
                "answer": "\"а справочка имеется?\" ©️",
                "count": 1
            },
            {
                "answer": "\"буквоед\"",
                "count": 1
            },
            {
                "answer": "буквает",
                "count": 1
            },
            {
                "answer": "буквоед",
                "count": 77
            },
            {
                "answer": "лишнее буквоедство",
                "count": 1
            },
            {
                "answer": "не спешащий буквоед.",
                "count": 1
            },
            {
                "answer": "важный формалист",
                "count": 1
            },
            {
                "answer": "избыточный формалист",
                "count": 1
            },
            {
                "answer": "форма важнее содержания",
                "count": 1
            },
            {
                "answer": "формализация",
                "count": 2
            },
            {
                "answer": "формализист",
                "count": 1
            },
            {
                "answer": "формализм",
                "count": 31
            },
            {
                "answer": "формализованный",
                "count": 1
            },
            {
                "answer": "формалист",
                "count": 206
            },
            {
                "answer": "формалист для которого форма",
                "count": 1
            },
            {
                "answer": "формалист зануда",
                "count": 1
            },
            {
                "answer": "формалист швондер",
                "count": 1
            },
            {
                "answer": "формалист/канцелярская крыса",
                "count": 1
            },
            {
                "answer": "формально",
                "count": 1
            },
            {
                "answer": "формальное выполнение работы",
                "count": 1
            },
            {
                "answer": "формальное затягивание",
                "count": 1
            },
            {
                "answer": "формальности",
                "count": 1
            },
            {
                "answer": "формальность",
                "count": 51
            },
            {
                "answer": "формальные правила",
                "count": 1
            },
            {
                "answer": "формальный",
                "count": 8
            },
            {
                "answer": "формальный подход.",
                "count": 1
            },
            {
                "answer": "формолист",
                "count": 1
            },
            {
                "answer": "канцеляр",
                "count": 1
            },
            {
                "answer": "канцелярия",
                "count": 4
            },
            {
                "answer": "канцелярская власть",
                "count": 1
            },
            {
                "answer": "канцелярская крыса",
                "count": 4
            },
            {
                "answer": "канцелярщик",
                "count": 1
            },
            {
                "answer": "канцелярщина",
                "count": 1
            },
            {
                "answer": "канцелярьщина",
                "count": 1
            },
            {
                "answer": "\"крючкотворец\"",
                "count": 1
            },
            {
                "answer": "бюрократ",
                "count": 1
            },
            {
                "answer": "бюрократ - времякрад",
                "count": 1
            },
            {
                "answer": "бюрократ - куче документов рад",
                "count": 1
            },
            {
                "answer": "бюрократ не человек росатома",
                "count": 1
            },
            {
                "answer": "бюрократия",
                "count": 4
            },
            {
                "answer": "бюрократия канцелярская власть",
                "count": 1
            },
            {
                "answer": "бюрократу важен процесс",
                "count": 1
            },
            {
                "answer": "бюросвалка",
                "count": 1
            },
            {
                "answer": "крючкотвор",
                "count": 32
            },
            {
                "answer": "крючкотворение",
                "count": 1
            },
            {
                "answer": "крючкотворец",
                "count": 8
            },
            {
                "answer": "крючкотворство",
                "count": 3
            },
            {
                "answer": "подменяющий смысл формой",
                "count": 1
            },
            {
                "answer": "\"бумажкодел\"",
                "count": 1
            },
            {
                "answer": "бумага",
                "count": 22
            },
            {
                "answer": "бумаги",
                "count": 22
            },
            {
                "answer": "бумаги волокита формальность",
                "count": 1
            },
            {
                "answer": "бумаговед",
                "count": 2
            },
            {
                "answer": "бумагодел",
                "count": 4
            },
            {
                "answer": "бумагомножитель",
                "count": 1
            },
            {
                "answer": "бумагоплодитель",
                "count": 2
            },
            {
                "answer": "бумаготворец",
                "count": 1
            },
            {
                "answer": "бумаготворитель",
                "count": 1
            },
            {
                "answer": "бумажка",
                "count": 3
            },
            {
                "answer": "бумажка на бумажку",
                "count": 1
            },
            {
                "answer": "бумажка на каждую проблему",
                "count": 1
            },
            {
                "answer": "бумажка ради бумажки",
                "count": 2
            },
            {
                "answer": "бумажки",
                "count": 14
            },
            {
                "answer": "бумажкодел",
                "count": 1
            },
            {
                "answer": "бумажная валокита",
                "count": 1
            },
            {
                "answer": "бумажная волокита",
                "count": 7
            },
            {
                "answer": "бумажная душа",
                "count": 11
            },
            {
                "answer": "бумажная работа",
                "count": 1
            },
            {
                "answer": "бумажная формальность",
                "count": 1
            },
            {
                "answer": "бумажник",
                "count": 2
            },
            {
                "answer": "бумажный",
                "count": 5
            },
            {
                "answer": "бумажный ад",
                "count": 1
            },
            {
                "answer": "бумажный педант",
                "count": 1
            },
            {
                "answer": "бумажный человек",
                "count": 3
            },
            {
                "answer": "бумажный червь",
                "count": 11
            },
            {
                "answer": "бумажный червяк",
                "count": 1
            },
            {
                "answer": "возня с бумагами",
                "count": 1
            },
            {
                "answer": "документ",
                "count": 6
            },
            {
                "answer": "документарный оборот",
                "count": 1
            },
            {
                "answer": "документации",
                "count": 1
            },
            {
                "answer": "документация",
                "count": 6
            },
            {
                "answer": "документоемкость",
                "count": 1
            },
            {
                "answer": "документолюбитель",
                "count": 1
            },
            {
                "answer": "документооборот",
                "count": 3
            },
            {
                "answer": "документопоклонник",
                "count": 1
            },
            {
                "answer": "документосвалка",
                "count": 1
            },
            {
                "answer": "документы",
                "count": 16
            },
            {
                "answer": "король бумажек",
                "count": 1
            },
            {
                "answer": "лишние жокументы",
                "count": 1
            },
            {
                "answer": "лишний документооборот",
                "count": 1
            },
            {
                "answer": "любитель бумаг",
                "count": 1
            },
            {
                "answer": "любитель процессов и бумаг",
                "count": 1
            },
            {
                "answer": "макулатура",
                "count": 2
            },
            {
                "answer": "макулатуроплодитель",
                "count": 1
            },
            {
                "answer": "мастер по бумажкам",
                "count": 1
            },
            {
                "answer": "много бумаги",
                "count": 1
            },
            {
                "answer": "много лишних бумаг",
                "count": 1
            },
            {
                "answer": "многобумаги",
                "count": 1
            },
            {
                "answer": "многобумажник",
                "count": 1
            },
            {
                "answer": "огромная стопка ненужных бумаг",
                "count": 1
            },
            {
                "answer": "перебирать бумаги",
                "count": 1
            },
            {
                "answer": "перекладывающий бумажки",
                "count": 1
            },
            {
                "answer": "повелитель бумаг",
                "count": 1
            },
            {
                "answer": "погрязший в бумагах",
                "count": 1
            },
            {
                "answer": "пожиратель бумаги",
                "count": 1
            },
            {
                "answer": "сборщик макулатуры",
                "count": 1
            },
            {
                "answer": "стопка бумаг",
                "count": 1
            },
            {
                "answer": "человек в бумажках",
                "count": 1
            },
            {
                "answer": "человек который плодит бумаги",
                "count": 1
            },
            {
                "answer": "человек-бумажка",
                "count": 1
            },
            {
                "answer": "\"бумажный червь\"",
                "count": 1
            },
            {
                "answer": "беспощадный бумагомаратель",
                "count": 1
            },
            {
                "answer": "бессмысленная бумажная волокит",
                "count": 2
            },
            {
                "answer": "бумагамаратель",
                "count": 1
            },
            {
                "answer": "бумагоед",
                "count": 2
            },
            {
                "answer": "бумаголюб",
                "count": 2
            },
            {
                "answer": "бумагомарака",
                "count": 4
            },
            {
                "answer": "бумагомарание",
                "count": 2
            },
            {
                "answer": "бумагомаратель",
                "count": 21
            },
            {
                "answer": "бумагомаратель,",
                "count": 1
            },
            {
                "answer": "бумагомарательство",
                "count": 1
            },
            {
                "answer": "бумагопреклонный",
                "count": 1
            },
            {
                "answer": "администрация по бумажкам",
                "count": 1
            },
            {
                "answer": "графоман",
                "count": 1
            },
            {
                "answer": "делопроизводитель",
                "count": 3
            },
            {
                "answer": "делопроизводство",
                "count": 1
            },
            {
                "answer": "бумажный произвол",
                "count": 1
            },
            {
                "answer": "работает для галочки",
                "count": 1
            },
            {
                "answer": "создающий видимость деятельнос",
                "count": 1
            },
            {
                "answer": "фиктивность",
                "count": 1
            },
            {
                "answer": "показуха",
                "count": 1
            },
            {
                "answer": "много лишней отчетности",
                "count": 1
            },
            {
                "answer": "много отчетов",
                "count": 1
            },
            {
                "answer": "ненужные отчеты",
                "count": 1
            },
            {
                "answer": "отчет",
                "count": 1
            },
            {
                "answer": "отчёт ради отчёта",
                "count": 1
            },
            {
                "answer": "отчетность",
                "count": 2
            },
            {
                "answer": "отчеты",
                "count": 2
            },
            {
                "answer": "отчёты и опросы",
                "count": 1
            },
            {
                "answer": "отчёт",
                "count": 1
            },
            {
                "answer": "\"душнила\"",
                "count": 1
            },
            {
                "answer": "«душнила»",
                "count": 1
            },
            {
                "answer": "въедливый",
                "count": 1
            },
            {
                "answer": "дотошность",
                "count": 1
            },
            {
                "answer": "дотошный",
                "count": 13
            },
            {
                "answer": "душная зануда",
                "count": 1
            },
            {
                "answer": "душнила",
                "count": 9
            },
            {
                "answer": "душный",
                "count": 4
            },
            {
                "answer": "зануда",
                "count": 47
            },
            {
                "answer": "занудный",
                "count": 2
            },
            {
                "answer": "занудство",
                "count": 2
            },
            {
                "answer": "мелочный",
                "count": 1
            },
            {
                "answer": "ненужный педантизм",
                "count": 1
            },
            {
                "answer": "педант",
                "count": 7
            },
            {
                "answer": "педант.",
                "count": 1
            },
            {
                "answer": "перфекционист",
                "count": 1
            },
            {
                "answer": "придирки",
                "count": 1
            },
            {
                "answer": "придирки до неважных мелочей",
                "count": 1
            },
            {
                "answer": "придирчивость",
                "count": 2
            },
            {
                "answer": "придирчивый",
                "count": 3
            },
            {
                "answer": "скрупулезность",
                "count": 1
            },
            {
                "answer": "скрупулёзность",
                "count": 1
            },
            {
                "answer": "скурпулезность",
                "count": 1
            },
            {
                "answer": "чересчур правильный",
                "count": 1
            },
            {
                "answer": "педантичный",
                "count": 1
            },
            {
                "answer": "запятуепривержинец",
                "count": 1
            },
            {
                "answer": "зацикленный на ненужных мелоча",
                "count": 1
            },
            {
                "answer": "недовольный жизнью зануда",
                "count": 1
            },
            {
                "answer": "нудила",
                "count": 1
            },
            {
                "answer": "нудно",
                "count": 2
            },
            {
                "answer": "нудный",
                "count": 6
            },
            {
                "answer": "нудный человек",
                "count": 1
            },
            {
                "answer": "\"заевшийся\"",
                "count": 1
            },
            {
                "answer": "толстопуз",
                "count": 1
            },
            {
                "answer": "толстый",
                "count": 1
            },
            {
                "answer": "\"замок\" ф. кафка",
                "count": 1
            },
            {
                "answer": "\"заноза\"",
                "count": 1
            },
            {
                "answer": "\"редиска\"",
                "count": 1
            },
            {
                "answer": "гад",
                "count": 1
            },
            {
                "answer": "заноза",
                "count": 2
            },
            {
                "answer": "зараза",
                "count": 1
            },
            {
                "answer": "негодяй",
                "count": 1
            },
            {
                "answer": "\"каждый суслик - агроном\"",
                "count": 1
            },
            {
                "answer": "«эксперт»",
                "count": 1
            },
            {
                "answer": "каждый суслик агроном",
                "count": 1
            },
            {
                "answer": "псевдопрофи",
                "count": 1
            },
            {
                "answer": "\"паленый\" самогон на поминках",
                "count": 1
            },
            {
                "answer": "\"ручник\" (ручной тормоз)",
                "count": 1
            },
            {
                "answer": "\"тормоз\"",
                "count": 1
            },
            {
                "answer": "задерживающий процесс",
                "count": 1
            },
            {
                "answer": "задержка",
                "count": 4
            },
            {
                "answer": "задержка; круговорот; душнила;",
                "count": 1
            },
            {
                "answer": "замедление",
                "count": 2
            },
            {
                "answer": "замедление времени",
                "count": 1
            },
            {
                "answer": "замедлитель",
                "count": 1
            },
            {
                "answer": "замедлитель работы",
                "count": 1
            },
            {
                "answer": "замедляющий",
                "count": 1
            },
            {
                "answer": "заминка",
                "count": 1
            },
            {
                "answer": "затормаживающий",
                "count": 1
            },
            {
                "answer": "затягивает принятие решений",
                "count": 1
            },
            {
                "answer": "затягивание",
                "count": 6
            },
            {
                "answer": "затягивание дела",
                "count": 1
            },
            {
                "answer": "затягивание процесса",
                "count": 1
            },
            {
                "answer": "затягивание процессов",
                "count": 1
            },
            {
                "answer": "затягиватель",
                "count": 2
            },
            {
                "answer": "затягиватель процессов",
                "count": 1
            },
            {
                "answer": "затягивать",
                "count": 1
            },
            {
                "answer": "затягивающий",
                "count": 3
            },
            {
                "answer": "затягивающий процесс",
                "count": 3
            },
            {
                "answer": "затягивающий процессы",
                "count": 1
            },
            {
                "answer": "затяжной",
                "count": 1
            },
            {
                "answer": "затянувшийся",
                "count": 1
            },
            {
                "answer": "звтягивание",
                "count": 1
            },
            {
                "answer": "идеалист тормозящий процесс",
                "count": 1
            },
            {
                "answer": "канитель",
                "count": 2
            },
            {
                "answer": "затягивание времени",
                "count": 1
            },
            {
                "answer": "останавливающий",
                "count": 1
            },
            {
                "answer": "останавливающий работу",
                "count": 1
            },
            {
                "answer": "торможение",
                "count": 2
            },
            {
                "answer": "тормоз",
                "count": 29
            },
            {
                "answer": "тормоз деятельности",
                "count": 1
            },
            {
                "answer": "тормоз производства",
                "count": 1
            },
            {
                "answer": "тормоз процесса",
                "count": 1
            },
            {
                "answer": "тормозит процесс",
                "count": 1
            },
            {
                "answer": "тормозитель",
                "count": 1
            },
            {
                "answer": "тормозной",
                "count": 1
            },
            {
                "answer": "тормозящий",
                "count": 4
            },
            {
                "answer": "тормозящий процедуру",
                "count": 1
            },
            {
                "answer": "тормозящий процесс",
                "count": 2
            },
            {
                "answer": "тот кто затягивает дело",
                "count": 1
            },
            {
                "answer": "удерживающий процесс",
                "count": 1
            },
            {
                "answer": "производственный тормоз",
                "count": 1
            },
            {
                "answer": "ручник",
                "count": 1
            },
            {
                "answer": "срыв сроков",
                "count": 1
            },
            {
                "answer": "стоп",
                "count": 2
            },
            {
                "answer": "стоп-кран",
                "count": 1
            },
            {
                "answer": "стопор",
                "count": 1
            },
            {
                "answer": "увеличение времени",
                "count": 1
            },
            {
                "answer": "увеличивающий сроки",
                "count": 1
            },
            {
                "answer": "удлинитель",
                "count": 1
            },
            {
                "answer": "удлиняющий",
                "count": 1
            },
            {
                "answer": "человек \"затягивающий\" рабочий",
                "count": 1
            },
            {
                "answer": "задержки",
                "count": 1
            },
            {
                "answer": "\"старовер\"",
                "count": 1
            },
            {
                "answer": "архаичный",
                "count": 1
            },
            {
                "answer": "динозавр",
                "count": 1
            },
            {
                "answer": "закоренелый",
                "count": 1
            },
            {
                "answer": "закостенелость",
                "count": 1
            },
            {
                "answer": "закостенелый",
                "count": 2
            },
            {
                "answer": "заскорузлость",
                "count": 1
            },
            {
                "answer": "застой",
                "count": 3
            },
            {
                "answer": "консервативность",
                "count": 1
            },
            {
                "answer": "консервативный",
                "count": 3
            },
            {
                "answer": "консерватизм",
                "count": 1
            },
            {
                "answer": "консерватор",
                "count": 7
            },
            {
                "answer": "костный",
                "count": 1
            },
            {
                "answer": "мракобес",
                "count": 1
            },
            # ==============================
            # {
            #     "answer": "несовременный",
            #     "count": 2
            # },
            # {
            #     "answer": "отсталый",
            #     "count": 1
            # },
            # {
            #     "answer": "регрессивный",
            #     "count": 1
            # },
            # {
            #     "answer": "ретроград",
            #     "count": 2
            # },
            # {
            #     "answer": "рудимент",
            #     "count": 2
            # },
            # {
            #     "answer": "старовер",
            #     "count": 3
            # },
            # {
            #     "answer": "старорежимник",
            #     "count": 1
            # },
            # {
            #     "answer": "устаревший",
            #     "count": 10
            # },
            # {
            #     "answer": "устаревший нудный человек",
            #     "count": 1
            # },
            # {
            #     "answer": "устарелый",
            #     "count": 2
            # },
            # {
            #     "answer": "косность",
            #     "count": 1
            # },
            # {
            #     "answer": "7 кругов ада",
            #     "count": 1
            # },
            # {
            #     "answer": "ад",
            #     "count": 1
            # },
            # {
            #     "answer": "www.buro.ru -\"бюрократ\" мебель",
            #     "count": 1
            # },
            # {
            #     "answer": "австро-венгрия",
            #     "count": 1
            # },
            # {
            #     "answer": "автократ",
            #     "count": 1
            # },
            # {
            #     "answer": "властитель",
            #     "count": 1
            # },
            # {
            #     "answer": "властный",
            #     "count": 1
            # },
            # {
            #     "answer": "власть",
            #     "count": 23
            # },
            # {
            #     "answer": "господство",
            #     "count": 2
            # },
            # {
            #     "answer": "властолюбие",
            #     "count": 1
            # },
            # {
            #     "answer": "администратор",
            #     "count": 1
            # },
            # {
            #     "answer": "администрация",
            #     "count": 1
            # }
        ]
    }
    infer.get_redirect_url(_input)
