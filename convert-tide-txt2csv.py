import os
import sys
import csv
import argparse

# 配列をcsvに保存
def save_csv(array, csv_file_name):
    with open(csv_file_name, mode='w') as converted_file:
        csvwriter = csv.writer(converted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        columnTitleRow = ["year","month","day","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
        csvwriter.writerow(columnTitleRow)
        for line in array:
            csvwriter.writerow(line)

# テキストから配列に変換
def txt2array(txt_file):
    txt_line_array = []

    for line in txt_file:
        line_split = line.split(' ')
        # 1日~9日 → 01日~09日
        if len(line_split[1]) < 3:
            line_split[1] = str(line_split[1]) + "0" + str(line_split[2])
        # 1月~9月 → 01月~09月
        if int(line_split[1][0]) < 10:
            line_split[1] = "0" + line_split[1]

        tides_txt_line = line_split[0][:72]
        tides = [tides_txt_line[i:i+3] for i in range(0, len(tides_txt_line), 3)]
        year  = line_split[0][72:]
        month = line_split[1][:2]
        day   = line_split[1][2:4]

        txt_line_array.append([year]+[month]+[day]+tides)
    
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