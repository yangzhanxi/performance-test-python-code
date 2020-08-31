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
def create_csv_file(file_name, header, row, row_num):
    with open(file_name, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = header)
        writer.writeheader()
        for i in range(0, row_num):
            writer.writerow(row)
       

if __name__ == "__main__":
    row = list()

    with open(csv_file, "r", encoding='UTF-8-sig') as resd_file:
        rows = csv.DictReader(resd_file)
        for i in rows:
            row = i
            print(i)
            break

    header = ["Snapshot Name","Trial","Frame Size (bytes)","Load (fps)","Agg Intended Load (fps)","Agg Offered Load (fps)","Agg Forwarding Rate (fps)","Agg Offered L1 Load (bps)","Agg Forwarding L1 Rate (bps)","Frame Loss (%)","Tx Count (frames)","Rx Count (frames)","Frame Loss (frames)","Duplicate Count (frames)","Tx Queue Full Drop Frame Count (frames)","Tx Queue Full Retry Frame Count (frames)","Tx Queue Full Drop (%)","Stream Avg Latency (µs)","Avg Jitter (µs)","Expected Stream Count","Missing Stream Count","Flooded Stream Count","Flooded Count (frames)"]

    # 5000 rows
    create_csv_file(five_thousand_lines_res, header, row, 5000)

    # 10000 rows
    create_csv_file(ten_thousand_lines_res, header, row, 10000)

    # 15000 rows
    create_csv_file(fifteen_thousand_lines_res, header, row, 15000)

    # 200000 rows
    create_csv_file(twenty_thousand_lines_res, header, row, 20000)

    # 100000 rows
    create_csv_file(hunder_thousand_lines_res, header, row, 100000)

    # 1000000 rows
    create_csv_file(million_lines_res, header, row, 1000000)
