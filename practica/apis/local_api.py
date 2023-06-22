import csv

def get_data_csv(csv_file):
    data = []

    with open(csv_file, 'r') as file:
        lector_csv = csv.reader(file)
        headers = next(lector_csv)

        for row in lector_csv:
            diccionario = dict(zip(headers, row))
            data.append(diccionario)

    return {"header": headers, "data": data}

if __name__ == "__main__":
    csv_file = "practica/apis/data.csv"
    data = get_data_csv(csv_file)
    print(data)
