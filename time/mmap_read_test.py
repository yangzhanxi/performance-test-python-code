# import csv
import sys
import timeit
import mmap
sys.path.append(r"./")

file_name = r"./million_lines_res.csv"

def mmap_read_file(file_name):
    with open(file_name, "r", encoding='utf8') as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
            # print(text)


if __name__ == "__main__":
    mmap_read_time = timeit.timeit("mmap_read_file(file_name)", number=1, globals=globals())

    print("mmap read file: {}s".format(mmap_read_time))


