#! usr/bin/env/ python3
import csv

# def get_waypoints(filename):
#     try:
#         with open(filename, 'w+') as f:
#             f = f.read()
#             return csv.DictReader(f)
#     except FileNotFoundError:
#         print(f'{inp-".csv"} is invalid.')
#         print('Enter new file name.')
#         return 0

# print('enter file name to import.')
# while True:
#     inp = input('-->:')

#     points = get_waypoints(inp)
#     if '.csv' not in inp:
#         print('Can only read CSV files.')
#         print('Enter new file name.')
#         continue
#     if points == 0:
#         continue
#     break
# for i in points:
#     print(f'{i["name"]}')

with open('moonbyte.csv') as f:
    f = f.readlines()
    coords =  csv.DictReader(f)
    coords = [i for i in coords]

<<<<<<< HEAD





def main():
    pass

if __name__ == "__main__":
    main()
=======
def csv_reader(data):
    """Convert CSV data into usable data
    
    Arguments:
        data {list} -- list of dictionaries imported from csv file
    
    Returns:
        list -- list of data reformatted to be useful
    """
    x = 0
    for i in data:
        data[x]['x'] = int(i['x'])
        data[x]['y'] = int(i['y'])
        data[x]['z'] = int(i['z'])
        if i['visible'] == 'true':
            data[x]['visible'] == True
        if i['visible'] == 'false':
            data[x]['visible'] == False
        data[x]['red'] = float(i['red'])
        data[x]['green'] = float(i['green'])
        data[x]['blue'] = float(i['blue'])
        data[x]['type'] = i['type'].split('/')
        data[x]['dimension'] = i['dimension'].replace('_', ' ')
        data[x]['dimension'] = i['dimension'].split('/')
        x += 1
    return data
    
for i in csv_reader(coords):
    print(i)
>>>>>>> 4cdca07814f064c2930c0b1667a6b89a12c6f4d5
