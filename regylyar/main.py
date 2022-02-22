import re

txt = (
  'Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru',
  'Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,',
  'Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,',
  'Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,',
  'Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru',
  'Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru',
  'Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),',
  'Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru')
text =('Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru; Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,; Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,; Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,; Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru; Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru; Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),; Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru; ')
code = '(\+7|8)?(\-|\ |)(\()?(\d+)(\))?(\-|\ |)(\d+)[\s-]*(\d+)[\s-]*(\d+)'
sent_line = re.findall(code, text)
new_txt = text.split()
new_work_text = []
for letters in txt:
    splet = letters
    sple = splet.split()
    success = sple[0:3]
    new_work_text.append(success)

new_work_one = new_work_text[0]
new_work_two = new_work_text[1]
new_work_three = new_work_text[2]
new_work_four = new_work_text[3]
new_work_five = new_work_text[4]
new_work_six = new_work_text[5]
new_work_seven = new_work_text[6]
new_work_eight = new_work_text[7]
print(new_work_text)

for letters in new_work_one[2]:
    if letters == 'ч':
        inde = new_work_one[2].index(letters)
        index = int(inde) + 1
        i = range(index, len(new_work_one[2]))
        for letters in i:
            list(new_work_one[2]).pop(letters)

for letters in new_work_two[2]:
    if letters == 'ч':
        inde = new_work_one[2].index(letters)
        index = int(inde) + 1
        i = range(index, len(new_work_one[2]))
        for letters in i:
            list(new_work_one[2]).pop(letters)

for lettes in new_work_three:
    list(new_work_three).remove(new_work_three[2])
    new_work_three[0].split()
    for letters in new_work_three[1]:
        if letters == 'ч':
            inde = new_work_one[1].index(letters)
            index = int(inde) + 1
            i = range(index, len(new_work_one[1]))
            for letters in i:
                list(new_work_one[1]).pop(letters)


for letter in new_work_four:
    for letters in new_work_four[0]:
        if letters == 'ч':
            inde = new_work_one[2].index(letters)
            index = int(inde) + 1
            i = range(index, len(new_work_one[2]))
            for letters in i:
                list(new_work_one[2]).pop(letters)
    list(new_work_three).remove(new_work_three[2])
    list(new_work_three).remove(new_work_three[1])

for letters in new_work_five[2]:
    if letters == 'ч':
        inde = new_work_one[2].index(letters)
        index = int(inde) + 1
        i = range(index, len(new_work_one[2]))
        for letters in i:
            list(new_work_one[2]).pop(letters)

for letters in new_work_six[2]:
    if letters == 'ч':
        inde = new_work_one[2].index(letters)
        index = int(inde) + 1
        i = range(index, len(new_work_one[2]))
        for letters in i:
            list(new_work_one[2]).pop(letters)

for letters in new_work_seven[2]:
    if letters == 'ч':
        inde = new_work_one[2].index(letters)
        index = int(inde) + 1
        i = range(index, len(new_work_one[2]))
        for letters in i:
            list(new_work_one[2]).pop(letters)
for work_letters in new_work_text:
    for work_letter in new_work_one[0:2]:
        for work_lette in new_work_two[0:2]:
            for work_lett in new_work_three[0:2]:
                for work_let in new_work_four[0:2]:
                    for work_le in new_work_five[0:2]:
                        for work_l in new_work_six[0:2]:
                            for work_ in new_work_seven[0:2]:
                                if work_letter == work_lette:
                                    no_double = zip(new_work_one, new_work_two)
                                elif work_letter == work_lett:
                                    no_double = zip(new_work_one, new_work_three)
                                elif work_letter == work_let:
                                    no_double = zip(new_work_one, new_work_four)
                                elif work_letter == work_le:
                                    no_double = zip(new_work_one, new_work_five)
                                elif work_letter == work_l:
                                    no_double = zip(new_work_one, new_work_six)
                                elif work_letter == work_:
                                    no_double = zip(new_work_one, new_work_seven)

                                if work_lette == work_letter:
                                    no_double = zip(new_work_one, new_work_two)
                                elif work_lette == work_lett:
                                    no_double = zip(new_work_two, new_work_three)
                                elif work_lette == work_let:
                                    no_double = zip(new_work_two, new_work_four)
                                elif work_lette == work_le:
                                    no_double = zip(new_work_two, new_work_five)
                                elif work_lette == work_l:
                                    no_double = zip(new_work_two, new_work_six)
                                elif work_lette == work_:
                                    no_double = zip(new_work_two, new_work_seven)

                                if work_lett == work_letter:
                                    no_double = zip(new_work_one, new_work_three)
                                elif work_lett == work_lette:
                                    no_double = zip(new_work_two, new_work_three)
                                elif work_lett == work_let:
                                    no_double = zip(new_work_three, new_work_four)
                                elif work_lett == work_le:
                                    no_double = zip(new_work_three, new_work_five)
                                elif work_lett == work_l:
                                    no_double = zip(new_work_three, new_work_six)
                                elif work_lett == work_:
                                    no_double = zip(new_work_three, new_work_seven)

                                if work_let == work_letter:
                                    no_double = zip(new_work_one, new_work_four)
                                elif work_let == work_lette:
                                    no_double = zip(new_work_four, new_work_two)
                                elif work_let == work_lett:
                                    no_double = zip(new_work_three, new_work_four)
                                elif work_let == work_le:
                                    no_double = zip(new_work_four, new_work_five)
                                elif work_let == work_l:
                                    no_double = zip(new_work_four, new_work_six)
                                elif work_let == work_:
                                    no_double = zip(new_work_four, new_work_seven)

                                if work_le == work_letter:
                                    no_double = zip(new_work_one, new_work_five)
                                elif work_le == work_lette:
                                    no_double = zip(new_work_two, new_work_five)
                                elif work_le == work_lett:
                                    no_double = zip(new_work_five, new_work_three)
                                elif work_let == work_le:
                                    no_double = zip(new_work_four, new_work_five)
                                elif work_le == work_l:
                                    no_double = zip(new_work_five, new_work_six)
                                elif work_le == work_:
                                    no_double = zip(new_work_five, new_work_seven)

                                if work_letter == work_l:
                                    no_double = zip(new_work_one, new_work_six)
                                elif work_lette == work_l:
                                    no_double = zip(new_work_two, new_work_six)
                                elif work_lett == work_l:
                                    no_double = zip(new_work_six, new_work_three)
                                elif work_let == work_l:
                                    no_double = zip(new_work_six, new_work_four)
                                elif work_le == work_l:
                                    no_double = zip(new_work_five, new_work_six)
                                elif work_l == work_:
                                    no_double = zip(new_work_six, new_work_seven)

                                if work_letter == work_:
                                    no_double = zip(new_work_one, new_work_seven)
                                elif work_lette == work_:
                                    no_double = zip(new_work_two, new_work_seven)
                                elif work_lett == work_:
                                    no_double = zip(new_work_three, new_work_seven)
                                elif work_let == work_:
                                    no_double = zip(new_work_four, new_work_seven)
                                elif work_le == work_:
                                    no_double = zip(new_work_five, new_work_seven)
                                elif work_l == work_:
                                    no_double = zip(new_work_six, new_work_seven)