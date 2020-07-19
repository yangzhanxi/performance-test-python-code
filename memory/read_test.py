import csv
import sys
sys.path.append(r"./")

csv_file = "./nfvi_traffic_summary.csv"

five_thousand_lines_res = "./five_thousand_lines_res.csv"
ten_thousand_lines_res = "./ten_thousand_lines_res.csv"
fifteen_thousand_lines_res = "./fifteen_thousand_lines_res.csv"
twenty_thousand_lines_res = "./twenty_thousand_lines_res.csv"
hunder_thousand_lines_res = "./hunder_thousand_lines_res.csv"
million_lines_res = "./million_lines_res.csv"

@profile
def read_csv_file(file_name):
    res_rows = list()

    with open(file_name, "r", encoding='UTF-8-sig') as resd_file:
        rows = csv.DictReader(resd_file)
        for i in rows:
            res_rows.append(i)

    print("total lines: %s" % len(res_rows))


if __name__ == "__main__":
    row = list()

    # five_thousand_lines_res
    # read_csv_file(five_thousand_lines_res)
    # ten_thousand_lines_res
    #read_csv_file(ten_thousand_lines_res)
    # fifteen_thousand_lines_res
    # read_csv_file(fifteen_thousand_lines_res)
    # twenty_thousand_lines_res
    #read_csv_file(twenty_thousand_lines_res)
    # hunder_thousand_lines_res
    # read_csv_file(hunder_thousand_lines_res)
    # million_lines_res
    read_csv_file(million_lines_res)
