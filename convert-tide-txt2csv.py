import os
import sys
import csv
import argparse

# 配列をcsvに保存
def save_csv(array, csv_file_name):
    with open(csv_file_name, mode='w') as converted_file:
        csvwriter = csv.writer(converted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        columnTitleRow = ["year","month","day","hour","tide"]
        csvwriter.writerow(columnTitleRow)
        for line in array:
            csvwriter.writerow(line)

# テキストから配列に変換
def txt2array(txt_file):
    txt_line_array = []

    for line in txt_file:
        tides_txt_line = line[:72]
        year  = line[72:74]
        month = line[74:76]
        day   = line[76:78]
        for i in range(24):
            hour  = i
            tide = tides_txt_line[i*3:i*3+3]
            txt_line_array.append([year]+[month]+[day]+[hour]+[tide])
    
    return txt_line_array


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()

    csv_file_name = args.input + ".csv"
    txt_file_name = args.input
    txt_file = open(txt_file_name, 'r')

    txt_array = txt2array(txt_file)
    save_csv(txt_array, csv_file_name)