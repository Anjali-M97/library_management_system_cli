from prettytable import PrettyTable

def tabular_data(data):
    field_names = data[0]
    rows = data[1:]
    table = PrettyTable()
    table.field_names = field_names
    for row in rows:
        table.add_row(row)
    print(table)