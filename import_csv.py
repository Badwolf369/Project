import csv
from collections import OrderedDict


def isInt(*args, base=10):
    
    for i in args:
        try:
            int(i, base)
            return True
        except ValueError:
            return False

class csv_file():
    def __init__(self, filename):
        self.filename = filename


    def read_file(self, fn):
        with open(fn, 'r') as f:
            f = csv.DictReader(f)
            f = list(f)
            for i, d in enumerate(f):
                f[i] = dict(d)
            return f

    
    def write_file(self, fn, keys, data):
        print('writing changes to file')


    def check_data(self, data):
        damage = []
        for i, d in enumerate(data):
            if not isInt(d["x"], d["y"], d["z"]):
                print(f'Error loading coordinates in point: {d["name"]}')
                damage.append([i, 'xyz'])
            if type(d["visible"]) == str:
                if d["visible"].casefold() not in ['true', 'false']:
                    print(f'Error loading visibility modifier in point: {d["name"]}')
                    damage.append([i, 'vis'])
            if not isInt(d["red"], d["green"], d["blue"], base=16):
                print(f'Error loading RGB values in point: {d["name"]}')
                damage.append([i, 'rgb'])
            if type(d["dimensions"]) == str:
                d["dimensions"] = d["dimensions"].split('/')
            for dim in d["dimensions"]:
                if dim not in ['end', 'nether', 'overworld']:
                    print(f'Error loading dimensions in point: {d["name"]}')
                    damage.append([i, 'dim'])
                    break

        if len(damage) != 0:
            print(f'There are {len(damage)} errors in the file')
            return damage
        else:
            print('Successfully imported file')
            return None

    
    def repair_data(self, data, dmg):
        def fix_num(dat, ndx, b=10):
            print(f'Value looks like {dat[ndx]}')
            print('What\'s it suppose to be?')
            while True:
                inp = input('-->:')
                if isInt(inp, b):
                    dat[ndx] = inp
                    print('Excellent. Fixed!')
                    return dat[ndx]
                else:
                    if b == 10:
                        print('That value is invalid too. I need a whole integer.')
                    elif b == 16:
                        print('That value is invalid too. I need a 2 digit hex value.')

        print('Locating specific errors...')
        if dmg == 'xyz':
            if not isInt(data["x"]):
                print(f'Error found in x value of point {data["name"]}.')
                data["x"] = fix_num(data, "x")
            elif not isInt(data["y"]):
                print(f'Error found in y value of point {data["name"]}.')
                data["y"] = fix_num(data, "y")
            elif not isInt(data["z"]):
                print(f'Error found in z value of point {data["name"]}.')
                data["z"] = fix_num(data, "z")
        elif dmg == 'vis':
            if data["visible"].casefold() not in ['true', 'false']:
                print(f'What the heck is {data["visible"]}?')
                print(f'It\'s in point {data["name"]}.')
                while True:
                    print('What\'s it supposed to be?')
                    inp = input('-->:')
                    if inp.casefold() == 'true':
                        print('Got it.')
                        data["visible"] = True
                        break
                    elif inp.casefold() == 'false':
                        print('Got it.')
                        data["visible"] = False
                        break
                    else:
                        print(f'I dont know what "{inp}" means')
        elif dmg == 'rgb':
            if not isInt(data["red"]):
                print(f'Error found in red value of point {data["name"]}.')
                data["red"] = fix_num(data, "red", 16)
            elif not isInt(data["green"]):
                print(f'Error found in green value of point {data["name"]}.')
                data["green"] = fix_num(data, "green", 16)
            elif not isInt(data["blue"]):
                print(f'Error found in blue value of point {data["name"]}.')
                data["blue"] = fix_num(data, "blue", 16)
        elif dmg == 'dim':
            print(f'I have no idea how to enterpret the dimensions in point {data["name"]}.')
            print(f'The current dimensions are {data["dimensions"]}.')
            while True:
                print('What are they supposed to be.')
                print('Type each separated by whitespace.')
                inp = input('-->:')
                inp = inp.split(r'\s')
                for i in inp:
                    if i not in ['overworld', 'nether', 'end']:
                        print('I still dont understand.')
                else:
                    print('Got it.')
                    data["dimensions"] = inp
                    break
        return data
            
            
    def format_data(self, data):
        for i, d in enumerate(data):
            d["x"] = int(d["x"])
            d["y"] = int(d["y"])
            d["z"] = int(d["z"])
            if type(d["visible"]) == str:
                if d["visible"].casefold() == 'true':
                    d["visible"] == True
                elif d["visible"].casefold() == 'false':
                    d["visible"] == False
            d["red"] = int(d["red"], 16)
            d["green"] = int(d["green"], 16)
            d["blue"] = int(d["blue"], 16)
            if '/' in d["dimensions"]:
                d["dimensions"] = d["dimensions"].split('/')
            data[i] = d
        return data


    data = get_file(filename)
    errors = check_data(data)
    while errors != None:
        for i, e in errors:
            attempt_repair(data[i], e)
        errors = check_data(data)
    data = format_data(data)
    print('The file is now ready to use.')

    


def main():
    get_waypoints_CSV('test.csv')

if __name__ == "__main__":
    main()
