import csv
def make_csv(content,name):
    columns_name = []
    for i in content[0].keys():
        columns_name.append(i)
    with open('./data/original/'+name+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns_name)
        for i in content:
            row = []
            for j in columns_name:
                    row.append(i[j])
            writer.writerow(row)
