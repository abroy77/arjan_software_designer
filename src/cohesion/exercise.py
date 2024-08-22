import csv
from typing import Any

Record = dict[str, Any]


def read_data(file_path: str) -> list[Record]:
    with open(file_path) as f:
        reader = csv.DictReader(f)
        data: list[Record] = list(reader)
        return data

def process_data(data: list[Record]) -> list[Record]:
        processed_data: list[Record] = []
        for row in data:
            row_copy = row.copy()
            if row_copy["status"] == "active":
                row_copy["is_active"] = True
            else:
                row_copy["is_active"] = False
        processed_data.append(row_copy) 
        return processed_data
def write_csv(path: str, data: list[Record]) -> None:
    with open(path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "status", "is_active"])
        writer.writeheader()
        writer.writerows(data) 
    
    return 
        

def main() -> None:
    data = read_data("data.csv")
    processed_data = process_data(data)
    write_csv("processed.csv", processed_data)



if __name__ == "__main__":
    main()
