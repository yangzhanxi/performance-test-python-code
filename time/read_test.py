# import csv
import sys
import timeit
import mmap
sys.path.append(r"./")

file_name = r"./million_lines_res.csv"

def read_file(file_name):
    with open(file_name, "r", encoding='utf8') as file_obj:
        text = file_obj.read()
        # print(text)


if __name__ == "__main__":
    read_time = timeit.timeit("read_file(file_name)", number=1, globals=globals())

    print("read file: {}s".format(read_time))

