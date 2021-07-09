import requests

weeks = {
    'Понедельник': 0,
    'Вторник': 1,
    'Среда': 2,
    'Четверг': 3,
    'Пятница': 4
}
groups = {
    '100': '23',
    '101': '24'
}


def get_schedule_from_api(group_number, week_day):
    group_index = groups[group_number]
    week_index = weeks[week_day]
    req = requests.get(f'https://rasp.source-point.ru/timetable/rasp?gid={group_index}').json()

    for lesson in range(0, 8):
        print(req[week_index]['result'][str(lesson)])


if __name__ == '__main__':
    get_schedule_from_api('101', 'Вторник')
