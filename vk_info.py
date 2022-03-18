import requests


gender = []

age = []

city = []

best_family = []

title = []

vk_id = []


class information:
    def start_gender(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        s = text[-20:]

        for letters in s:

            if letters == "s":

                next_day = int(s.index(letters)) + 1

                if s[next_day] == "e":

                    se = int(next_day) + 1

                    if s[se] == "x":

                        end = se + 3
                        sex = s[end]
                        gender.append(sex)

    def age_old(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        txt = text.split()
        found_work = txt[8]

        for letters in found_work:

            if letters == "d":

                x = found_work.index(letters)

                if found_work[x + 1] == "a":

                    if found_work[x + 2] == "t":

                        if found_work[x + 3] == "e":

                            date = found_work[x + 7:x + 16]

                            age_ = 2022 - int(date[5:])

                            age.append(age_)

    def start_city(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        txt = text.split()
        founds = txt[8]
        for i in founds:

            if i == "y":

                x = founds.index(i)
                new_founds = founds[x+9:]

        def cities():
            nonlocal new_founds

            for letters in new_founds:

                if letters == "l":

                    y = new_founds.index(letters)

                    if new_founds[y+1] == "e":

                        for let in new_founds[y+5:]:

                            if let == "}":

                                end = new_founds.index(let)
                                cit = new_founds[y+5:end]
                                city.append(cit)

        return cities

    def end_family(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        txt = text.split()
        search_found = txt[12]

        for letters in search_found:

            if letters == "r":

                x = search_found.index(letters)

                if search_found[x+1] == "e":

                    if search_found[x+2] == "l":

                        if search_found[x+3] == "a":

                            if search_found[x+4] == "t":

                                if search_found[x+5] == "i":

                                    if search_found[x+6] == "o":

                                        if search_found[x+7] == "n":

                                            famil = search_found[x+10]

                                            if 1 in gender:

                                                if famil == "1":

                                                    best_family.append("не замужем")

                                                elif famil == "2":

                                                    best_family.append('есть подруга,')

                                                elif famil == "3":

                                                    best_family.append('помолвлена')

                                                elif famil == "4":

                                                    best_family.append("замужем")

                                                elif famil == "7":

                                                    best_family.append("влюблена")

                                            if 2 in gender:

                                                if famil == "1":

                                                    best_family.append("не женат")

                                                elif famil == "2":

                                                    best_family.append('есть друг,')

                                                elif famil == "3":

                                                    best_family.append('помолвлен')

                                                elif famil == "4":

                                                    best_family.append("женат")

                                                elif famil == "7":

                                                    best_family.append("влюблен")

                                            if famil == "5":

                                                best_family.append("всё сложно,")

                                            if famil == "6":

                                                best_family.append("в активном поиске")

                                            if famil == "8":

                                                best_family.append("в гражданском браке,")

                                            if famil == "0":

                                                best_family.append("не указано")


    def fr_name(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        txt = text.split()
        last_found = txt[8]

        for letters in last_found:

            if letters == "n":

                x = last_found.index(letters)

                if last_found[x+1] == "a":

                    if last_found[x+2] == "m":

                        if last_found[x+3] == "e":

                            first_name = last_found[x+6:35]
                            title.append(first_name)

    def id(self):
        url = "https://api.vk.com/method/account.getProfileInfo?&access_token=958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008&v=5.131"
        responce = requests.get(url)
        responce.raise_for_status()

        text = responce.text
        txt = text.split()
        vk_work = txt[0]

        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for letters in vk_work:

            if letters == "i":

                x = vk_work.index(letters)

                if vk_work[x+1] == "d":

                    if vk_work[x+4] in num:

                        if vk_work[x+5] in num:

                            if vk_work[x+6] in num:

                                if vk_work[x+7] in num:

                                    if vk_work[x+8] in num:

                                        if vk_work[x+9] in num:

                                            if vk_work[x+10] in num:

                                                if vk_work[x+11] in num:

                                                    if vk_work[x+12] in num:

                                                        if vk_work[x+13] in num:

                                                            if vk_work[x+14] in num:

                                                                if vk_work[x+15] in num:

                                                                    if vk_work[x+16] in num:

                                                                        if vk_work[x+17] in num:

                                                                            if vk_work[x+18] in num:

                                                                                if vk_work[x+19] in num:
                                                                                    pass

                                                                                if vk_work[x+19] not in num:
                                                                                    vk_id.append(vk_work[x+4:x+19])

                                                                            elif vk_work[x+18] not in num:
                                                                                vk_id.append(vk_work[x+4:x+18])

                                                                        elif vk_work[x+17] not in num:
                                                                            vk_id.append(vk_work[x+4:x+17])

                                                                    elif vk_work[x+16] not in num:
                                                                        vk_id.append(vk_work[x+4:x+16])

                                                                elif vk_work[x+15] not in num:
                                                                    vk_id.append(vk_work[x+4:x+15])

                                                            elif vk_work[x+14] not in num:
                                                                vk_id.append(vk_work[x+4:x+14])

                                                        elif vk_work[x+13] not in num:
                                                             vk_id.append(vk_work[x+4:x+13])

                                                    elif vk_work[x+12] not in num:
                                                        vk_id.append(vk_work[x+4:x+12])

                                                elif vk_work[x+11] not in num:
                                                    vk_id.append(vk_work[x+4:x+11])

                                            elif vk_work[x+10] not in num:
                                                vk_id.append(vk_work[x+4:x+10])

                                        elif vk_work[x+9] not in num:
                                            vk_id.append(vk_work[x+4:x+9])

                                    elif vk_work[x+8] not in num:
                                        vk_id.append(vk_work[x+4:x+8])

                                elif vk_work[x+7] not in num:
                                    vk_id.append(vk_work[x+4:x+7])

                            elif vk_work[x+6] not in num:
                                vk_id.append(vk_work[x+4:x+6])

                        elif vk_work[x+5] not in num:
                            vk_id.append(vk_work[x+4:x+5])

    for letters in title:

        if letters == f'"':

            title.remove(letters)

        elif letters == ',':

            title.remove(letters)

    for letters in gender:

        if letters == f'"':

            gender.remove(letters)

        elif letters == ',':

            gender.remove(letters)

    for letters in age:

        if letters == f'"':

            age.remove(letters)

        elif letters == ',':

            age.remove(letters)

    for letters in city:

        if letters == f'"':

            city.remove(letters)

        elif letters == ',':

            city.remove(letters)

    for letters in best_family:

        if letters == f'"':

            best_family.remove(letters)

        elif letters == ',':

            best_family.remove(letters)


print(information.fr_name(1))

print(information.end_family(1))

print(information.age_old(1))

print(information.start_city(1))

print(information.start_gender(1))

print(information.id(1))

