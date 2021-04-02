from datetime import date
import time

subjectlist = {
    3162001: 'DESIGN OF MECHANISM',
    3162008: 'HYDRAULIC & PNEUMATIC SYSTEMS',
    3162006: 'Computer Aided Design and Modeling',
    3162003: 'Control of Electric Drives',
    3162009: 'Machine Vision',
    3162005: 'Electro Mechanical Measurements & Instruments',
    3162011: 'Entrepreneurship Devlopment',
    3160001: 'Design Dengineering - II B',
    3160002: 'Contributor Personility Devlopment Course'
}

timetableB = {0: '222-397-',
              1: '-11-5144',
              2: '-83-581-',
              3: '-55-5712',
              4: '7-------',
              5: '932-1---'}

subjectcode = []
subjectnames = []

for x in subjectlist.keys():
    subjectcode.append(x)

for y in subjectlist.values():
    subjectnames.append(y)


def checkbatch(enrolment):
    enrol = str(enrolment)
    if len(enrol) == 12:
        year = enrol[0] + enrol[1]  # 180110120020
        rest_all = str(enrol[2:9])
        if year == '18' or '19' and rest_all == '01101200':
            roll_no = str(enrol[10]) + str(enrol[11])  # 180110120020
            if int(roll_no) < 20:
                return 'A'
            elif int(roll_no) > 50:
                return 'C'
            else:
                return 'B'
        return 'sorry you are not in mechatronics'
    return 'sorry the enrollment is not in our university'


def lecturenow(enrollment):
    day = date.today().weekday()  # 0 for monday
    h = int(time.strftime("%H", time.localtime()))
    m = int(time.strftime("%M", time.localtime()))

    day = 0
    h = 16
    m = 20

    if day <= 5:
        batch = checkbatch(enrollment)

        if batch == 'A' or 'B' or 'C':

            if h - 9 >= 0 and h - 9 < 9:
                leclist = timetableB[day]
                if m < 30:
                    lec = leclist[h - 10]
                    if lec != '-':
                        lec = int(lec)
                        return str(subjectcode[lec - 1]) + ' : ' + subjectnames[lec - 1]
                    else:
                        return 'not any lecturenow , have fun'

                elif h < 17:
                    lec = int(leclist[h - 9])
                    if lec != '-':
                        lec = int(lec)
                        return str(subjectcode[lec - 1]) + ' : ' + subjectnames[lec - 1]
                    else:
                        return 'not any lecture now, have fun'
                else:
                    return 'not any lecture after 5:30 today ckeck tomorraw'
            else:
                return 'not any lecture after 5:30 today ckeck tomorraw'
        else:
            return batch
    else:
        return 'its Sunday come on do want to study'


