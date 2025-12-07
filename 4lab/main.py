class Colon:
    def __init__(self, line):
        self.line = line
        self.total = 0

    def seconds(self):
        time = self.line.split(' ')
        if 'hms' in time:
            h, m, s = map(int, time[1].split(':'))
            self.total = float(h * 3600 + m * 60 + s)
        elif 'ms' in time:
            h, m, s = map(int, time[1].split(':'))
            s, ms = map(int, s.split('.'))
            self.total = float(h * 3600 + m * 60 + s + ms / 1000)
        elif 'minsec' in time:
            m, s = map(int, time[1].split(':'))
            self.total = float(m * 60 + s)
        elif 'hm' in time:
            h, m = map(int, time[1].split(':'))
            self.total = float(h * 3600 + m * 60)
        elif 'secms' in time:
            s, ms = map(int, time[1].split(':'))
            self.total = float(s + ms / 1000)
        elif 'hours' in time:
            raise ValueError(f'Для часов должен быть формат hh:mm:ss или h.s, или h')
        elif 'minutes' in time:
            raise ValueError(f'Для минут должен быть формат hh:mm:ss или m, или m.ms')
        elif 'seconds' in time:
            raise ValueError(f'Для секунд должен быть формат hh:mm:ss или s')
        return self.total


class OneNumber:
    def __init__(self, line):
        self.line = line
        self.total = 0

    def seconds(self):
        number = self.line.split(' ')
        if 'hms' in number:
            raise ValueError(f'Одно число не является форматом hms')
        elif 'ms' in number:
            self.total = float(int(number[1]) / 1000)
        elif 'minsec' in number:
            raise ValueError(f'Одно число не является форматом minsec')
        elif 'hm' in number:
            raise ValueError(f'Одно число не является форматом hm')
        elif 'secms' in number:
            raise ValueError(f'Одно число не является форматом secms')
        elif 'hours' in number:
            self.total = int(number[1]) * 3600
        elif 'minutes' in number:
            self.total = int(number[1]) * 60
        elif 'seconds' in number:
            self.total = int(number[1])
        return self.total


class TwoNumbers:
    def __init__(self, line):
        self.line = line
        self.total = 0

    def seconds(self):
        two_num = self.line.split(' ', 1)
        first_num, second_num = map(int, two_num[1].split(' '))
        if 'hms' in two_num:
            raise ValueError(f'Два числа не являются форматом hms')
        elif 'ms' in two_num:
            raise ValueError(f'Два числа не являются форматом ms')
        elif 'minsec' in two_num:
            self.total = float(first_num * 60 + second_num)
        elif 'hm' in two_num:
            self.total = float(first_num * 3600 + second_num * 60)
        elif 'secms' in two_num:
            self.total = float(first_num + second_num / 1000)
        elif 'hours' in two_num:
            raise ValueError(f'Два числа не являются форматом hours')
        elif 'minutes' in two_num:
            raise ValueError(f'Два числа не являются форматом minutes')
        elif 'seconds' in two_num:
            raise ValueError(f'Два числа не являются форматом seconds')
        return self.total
        

class Point:
    def __init__(self, line):
        self.line = line
        self.total = 0

    def seconds(self):
        point_number = self.line.split(' ')
        if 'hms' in point_number:
            raise ValueError(f'Одно число не является форматом hms')
        elif 'ms' in point_number:
            raise ValueError(f'У числа формата ms нет меньших временных значений')
        elif 'minsec' in point_number:
            raise ValueError(f'Одно число не является форматом minsec')
        elif 'hm' in point_number:
            raise ValueError(f'Одно число не является форматом hm')
        elif 'secms' in point_number:
            raise ValueError(f'Одно число не является форматом secms')
        elif 'hours' in point_number:
            self.total = float(point_number[1]) * 3600.0
        elif 'minutes' in point_number:
            self.total = float(point_number[1]) * 60.0
        elif 'seconds' in point_number:
            self.total = float(point_number[1])
        return self.total

def format_hms(new_time):
    new_time = round(new_time)
    hours = new_time // 3600
    minutes = new_time % 3600 // 60
    seconds = new_time % 3600 % 60
    format_of_time = []
    if hours > 0:
        format_of_time.append(f'{hours} h')
    if minutes > 0 or (hours == 0 and seconds > 0):
        format_of_time.append(f'{minutes} min')
    if seconds > 0 or (hours == 0 and minutes == 0 and seconds == 0):
        format_of_time.append(f'{seconds} s')
    return ' '.join(format_of_time) if format_of_time else '0 s'

def tranlate_string(line):
    testing_whitespace = line.split(' ', 1)
    if ':' in line:
        return Colon(line)
    elif '.' in line:
        return Point(line)
    elif ' ' in testing_whitespace[1]:
        return TwoNumbers(line)
    elif ':' not in line and '.' not in line and ' ' not in testing_whitespace[1]:
        return OneNumber(line)


strings = [
    "minsec 10:00",
    "ms 90000",
    "hm 10 45",
    "minutes 0.5"
]

time_strings = []
for string in strings:
    seconds_string = tranlate_string(string)
    time_strings.append(seconds_string)

format_in_sec = [i.seconds() for i in time_strings]

sum_seconds = sum(format_in_sec)
print(f"Total: {format_hms(sum_seconds)}")

average_seconds = sum_seconds / len(format_in_sec)
print(f"Average: {format_hms(average_seconds)}")

max_seconds = max(format_in_sec)
print(f"Max: {format_hms(max_seconds)}")

min_seconds = min(format_in_sec)
print(f"Min: {format_hms(min_seconds)}")
