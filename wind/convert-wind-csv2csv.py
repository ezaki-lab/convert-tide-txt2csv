import os
import sys
import csv
import argparse
import datetime

# 配列をcsvに保存
def save_csv(array, csv_file_name):
    with open(csv_file_name, mode='w') as converted_file:
        csvwriter = csv.writer(converted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        columnTitleRow = ["year","month","day","hour","wind_speed","wind_direction"]
        csvwriter.writerow(columnTitleRow)
        for line in array:
            csvwriter.writerow(line)


def indexOfWinddirection(wind_direction):
    if wind_direction == '北':
        return 0
    elif wind_direction == '北北東':
        return 1
    elif wind_direction == '北東':
        return 2
    elif wind_direction == '東北東':
        return 3
    elif wind_direction == '東':
        return 4
    elif wind_direction == '東南東':
        return 5
    elif wind_direction == '南東':
        return 6
    elif wind_direction == '南南東':
        return 7
    elif wind_direction == '南':
        return 8
    elif wind_direction == '南南西':
        return 9
    elif wind_direction == '南西':
        return 10
    elif wind_direction == '西南西':
        return 11
    elif wind_direction == '西':
        return 12
    elif wind_direction == '西北西':
        return 13
    elif wind_direction == '北西':
        return 14
    elif wind_direction == '北北西':
        return 15
    elif wind_direction == '静穏':
        return 16
    else:
        return -1


def csv2array(input_file):
    array = []

    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dt_str = row[0]
        dt = datetime.datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S')
        year  = dt.year
        month = dt.month
        day   = dt.day
        hour = dt.hour
        wind_speed = row[1]
        wind_direction = indexOfWinddirection(row[3])
        array.append([year]+[month]+[day]+[hour]+[wind_speed]+[wind_direction])

    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()

    new_file_name = os.path.join(os.path.dirname(args.input), "converted-" + os.path.basename(args.input))
    input_file_name = args.input

    with open(input_file_name, 'r', encoding='shift_jis') as csv_file:
        array = csv2array(csv_file)
        save_csv(array, new_file_name)