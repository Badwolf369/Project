"""Simple program to import and format a CSV file."""

# pylint: disable=C0103
# pylint: disable=R0201
# pylint: disable=R1723

import csv


class CSVfile():
    """Imported and formatted CSV file.

    Raises:
        ValueError: During format of RGB values

    Returns:
        list -- list of dicts gathered from passed in file
    """

    def __init__(self, filename):
        """Load the file and format it when the object is created.

        Arguments:
            filename {str} -- Name of file to be opened.
        """
        self.filename = filename
        self.load(filename)

    def format_xyz(self, i, d):
        """Format XYZ values in given waypoint.

        Arguments:
            i {str} -- index to be edited (x, y or z)
            d {dict} -- single waypoint

        Returns:
            int -- formatted index value
        """
        try:
            d[i] = int(d[i])
        except ValueError:
            print(f'Error loading {i} value in point {d["name"]}.')
            print(f'Value looks like {d[i]}.')
            while True:
                print('What\'s it supposed to be?')
                inp = input('-->:')
                try:
                    d[i] = int(inp)
                    print('Got it.')
                    break
                except ValueError:
                    print('Still can\'t load.')
                    print('Whole integer is required.')
        return d[i]

    def format_vis(self, d):
        """Format visibility modifier in given waypoint.

        Arguments:
            d {dict} -- single waypoint

        Returns:
            bool -- visibility boolean
        """
        if d["visible"].casefold() == 'true':
            d["visible"] = True
        elif d["visible"].casefold() == 'false':
            d["visible"] = False
        else:
            print(f'Error loading visibility boolean in point {d["name"]}.')
            print(f'Boolean looks like {d["visible"]}')
            while True:
                inp = input('-->:')
                inp = inp.casefold()
                if inp == 'true':
                    d["visible"] = True
                    break
                elif inp == 'false':
                    d["visible"] = False
                    break
                else:
                    print('I still do not understand.')
                    print('Value must be boolean.')
        return d["visible"]

    def format_rgb(self, i, d):
        """Format RGB values in given waypoint.

        Arguments:
            i {str} -- Index to be edited (red, green, or blue)
            d {dict} -- Single waypoint

        Raises:
            ValueError: To shortcut some code if incorrect valaue entered

        Returns:
            int -- formatted value at the specified index
        """
        try:
            d[i] = int(d[i])
        except ValueError:
            print(f'Error loading {i} value in point {d["name"]}')
            print(f'Value looks like {d[i]}.')
            while True:
                print('What\'s it supposed to be?')
                inp = input('-->:')
                try:
                    d[i] = int(inp)
                    if not 0 < d[i] < 255:
                        raise ValueError()
                    break
                except ValueError:
                    print('Still can\'t understand.')
                    print('Must be a whole integer between 0 and 255.')
        return d[i]

    def format_dim(self, d):
        """Format dimensions value in given waypoint.

        Arguments:
            d {dict} -- Single waypoint

        Returns:
            list -- Formatted list of dimensions
        """
        d["dimensions"] = set(d["dimensions"].split('/'))
        for i in d["dimensions"]:
            if i not in ['end', 'overworld', 'nether']:
                print(f'I dont understand the dimensions of point {d["name"]}')
                print(f'The list looks like {d["dimensions"]}')
                while True:
                    print('What are the dimensions supposed to be?')
                    print('Type them separated by white space.')
                    inp = input('-->:').split(r'\s')
                    for x in inp:
                        if x not in ['end', 'overworld', 'nether']:
                            print('I still dont understand.')
                            break
                    else:
                        print('Got it.')
                        d["dimensions"] = inp
                        break
        return d["dimensions"]

    def load(self, filename):
        """Load given file.

        Arguments:
            filename {str} -- name of file to be loaded
        """
        with open(filename, 'r') as f:
            f = csv.DictReader(f)
            f = list(f)
            for i, d in enumerate(f):
                f[i] = dict(d)
            self.data = f

        for i, d in enumerate(self.data):
            d["x"] = self.format_xyz("x", d)
            d["y"] = self.format_xyz("y", d)
            d["z"] = self.format_xyz("z", d)
            d["visible"] = self.format_vis(d)
            d["red"] = self.format_rgb("red", d)
            d["green"] = self.format_rgb("green", d)
            d["blue"] = self.format_rgb("blue", d)
            d["uses"] = set(d["uses"].split('/'))
            d["dimensions"] = self.format_dim(d)
        self.data[i] = d
        self.write()

    def write(self):
        """Write current data to the file passed in during object creation."""
        with open(self.filename, 'w') as f:
            keys = [
                'name',
                'x',
                'y',
                'z',
                'visible',
                'red',
                'green',
                'blue',
                'uses',
                'dimensions']
            w = csv.DictWriter(f, keys)
            w.writeheader()
            w.writerows(self.data)


coords = CSVfile('moonbyte.csv')
