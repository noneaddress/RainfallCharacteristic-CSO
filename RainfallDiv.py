"""
rainfall div
"""
import os
filePath = ''
file_rainfall = open(filePath, 'r', encoding="UTF-8")
count = 0
i = input(f"please enter the interval threshold to divide rainfall")
interval = int(i)

line = file_rainfall.readline()
while line:

    line = line.strip()

    new_line = line.split('\t')

    if new_line[5] != "0":
        first_time = f"{new_line[0]}_{new_line[1]}_{new_line[2]}_{new_line[3]}_{new_line[4]}"

        name_first_time = f"{first_time}.txt"

        time_rainfall = open(os.path.join(filePath,f"result\\{name_first_time}"), 'a', encoding="UTF-8")

        time_rainfall.write(f"{new_line[0]}/{new_line[1]}/{new_line[2]} {new_line[3]}:{new_line[4]}\t{new_line[5]}\n")

        line = file_rainfall.readline()

        while line:
            line = line.strip()
            new_line = line.split('\t')
            first_time = f"{new_line[0]}/{new_line[1]}/{new_line[2]} {new_line[3]}:{new_line[4]}"

            if new_line[5] == "0":

                count += 1

                if count == interval:

                    time_rainfall.flush()
                    time_rainfall.close()

                    break
                else:
                    time_rainfall.write(f"{first_time}\t{new_line[5]}\n")

                line = file_rainfall.readline()

            else:

                time_rainfall.write(f"{first_time}\t{new_line[5]}\n")
                count = 0

                line = file_rainfall.readline()

        del_360 = open(os.path.join(filePath,f"result\\{name_first_time}"), 'r', encoding="UTF-8")
        lines = del_360.readlines()
        del lines[-interval + 1:]

        del_360.flush()
        del_360.close()
        file_new = open(os.path.join(filePath,f"result\\{name_first_time}"), 'w', encoding="UTF-8")
        file_new.writelines(lines)
        file_new.flush()
        file_new.close()

    line = file_rainfall.readline()

file_rainfall.flush()
file_rainfall.close()

