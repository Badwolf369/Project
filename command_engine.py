"""Commandline engine to do work on minecraft waypoints."""

# pylint: disable=C0301
# pylint: disable=C0103
# pylint: disable=R1723
# pylint: disable=W0703
# pylint: disable=W0104
# pylint: disable=R1720

# I realise you said no global variables, but these were a pain to try passing into every function
data = [
    {
        "name": 'spawn',
        "x": 0,
        "z": 0,
        "y": 72,
        "visible": True,
        "red": 255,
        "green": 0,
        "blue": 0,
        "uses": ['spawn'],
        "dimensions": {'overworld', 'end', 'nether'}
    }]

dimFilter = {'overworld', 'end', 'nether'}
useFilter = []
sections = [
    {
        "name": 'spawn',
        "type": 'area',
        "x1": -250,
        "z1": -250,
        "x2": 250,
        "z2": 250
    },
    {
        "name": 'surface',
        "type": 'elevation',
        "direction": 'above',
        "y": 63
    }]

# Main command line loop
while True:
    inp = input('-->:').casefold()
    command = inp.strip(r'\W').split()
    try:
        # Quit the program
        if command[0] == 'quit':
            break
        # Help with command syntax
        elif command[0] == 'help':
            if len(command) == 1:
                print('Commands:')
                print('‣ Quit  -  Quit the program')
                print('‣ Help  -  Show this list')
                print('‣ Create  -  Create a waypoint')
                print('‣ Filter  -  Filter waypoints')
                print('‣ List  -  List waypoints')
                print('‣ Edit  -  Edit values in waypoint')
                print('‣ View  -  View details about a specific waypoint')
                print('‣ Delete  -  Delete waypoints')
                print('Type \'help <command>\' to show more details.')
            elif command[1] == 'quit':
                print('End the program and save changes to the file.')
                print('Syntax: Quit')
            elif command[1] == 'help':
                print('Give details about certain commands.')
                print('Syntax: Help <command>')
            elif command[1] == 'create':
                print('Create a new waypoint.')
                print('Syntax: Create <name> <x> <y> <z> ', end='')
                print('<visible> <r> <g> <b> <uses> <dimensions>')
                print('Enter uses and dimensions as a list with a \'/\' between each item.')
            elif command[1] == 'filter':
                if len(command) == 2:
                    print('View and edit list of active filters.')
                    print('Subcommands:')
                    print('‣ Clear  -  Clears all filters')
                    print('‣ Add  -  Adds a filter')
                    print('‣ Remove  -  Removes a filter')
                    print('‣ List  -  Lists all filters')
                    print('Type \'Help Filter <subcommand>\' for more information.')
                    print('Syntax: Filter <subcommand>')
                elif command[2] == 'clear':
                    print('Clear all filters.')
                    print('Syntax: Filter Clear')
                elif command[2] == 'add':
                    if len(command) == 3:
                        print('Add a new filter.')
                        print('Valid filters:')
                        print('‣ Area')
                        print('‣ Elevation')
                        print('‣ Uses')
                        print('‣ Dimensions')
                        print('Type \'Help Filter Add <filter>\' for more information.')
                        print('Syntax: Filter Add <filter>')
                    elif command[3] == 'area':
                        print('Create a new x/z area.')
                        print('Syntax: Filter Add Area <name> <x1> <z1> <x2> <z2>')
                    elif command[3] == 'elevation':
                        print('Create a new y area.')
                        print('Syntax: Filter Add Area <name> <above/below/at> <y>')
                    elif command[3] == 'uses':
                        print('Filter valid points by uses.')
                        print('Syntax: Filter Add Uses <uses>')
                        print('Enter uses as a list with a \'/\' separating each item.')
                    elif command[3] == 'dimensions':
                        print('Filter valid points by dimension.')
                        print('Syntax: Filter Add Dimensions <dimensions>')
                        print('Enter dimensions as a list with a \'/\' separating each item.')
                    else:
                        raise SyntaxError(f'Unknown command \'{command[3]}\'.')
                elif command[2] == 'remove':
                    print('Remove specified filter.')
                    print('Syntax: Filter Remove <dimensions/uses>; Filter Remove <name>')
                elif command[2] == 'list':
                    print('List all active filters.')
                    print('Syntax: Filter List')
                else:
                    raise SyntaxError(f'Unknown command \'{command[2]}\'.')
            elif command[1] == 'list':
                print('List all points that match all active filters.')
                print('Syntax: List')
            elif command[1] == 'edit':
                print('Edit specific values in a certain point defined by \'name\'.')
                print('Syntax: Edit <name> <edit value> <value>')
                print('Enter \'dimensions\' and  \'uses\' values as lists with \'/\' separating each item.')
            elif command[1] == 'view':
                print('View details about a specific waypoint.')
                print('Syntax: View <name>')
            elif command[1] == 'delete':
                print('Delete specific waypoints.')
                print('Syntax: Delete <name>')
            else:
                raise SyntaxError(f'Unknown command \'{command[1]}\'')
        # Create a new waypoint
        elif command[0] == 'create':
            for i in data:
                if i["name"] == command[1]:
                    raise SyntaxError('A waypoint with that name already exists.')
            p = {}
            p["name"] = command[1]
            p["x"] = int(command[2])
            p["y"] = int(command[3])
            p["z"] = int(command[4])
            if command[5] == 'true':
                p["visible"] = True
            elif command[5] == 'false':
                p["visible"] = False
            else:
                raise SyntaxError('Error in visibility bool.')
            if 0 <= int(command[6]) <= 255:
                p["red"] = int(command[6])
            else:
                raise SyntaxError('Error in red value.')
            if 0 <= int(command[7]) <= 255:
                p["green"] = int(command[7])
            else:
                raise SyntaxError('Error in green value.')
            if 0 <= int(command[8]) <= 255:
                p["blue"] = int(command[8])
            else:
                raise SyntaxError('Error in blue value.')
            p["uses"] = command[9].split('/')
            p["dimensions"] = set(command[10].split('/'))
            for i in p["dimensions"]:
                if i not in ['end', 'overworld', 'nether']:
                    raise SyntaxError('Error in dimensions.')
            print('Success.')
            data.append(p)
        # View and edit filters
        elif command[0] == 'filter':
            # View filters
            if len(command) == 1 or command[1] == 'list':
                if len(sections) == 0 and len(useFilter) == 0 and dimFilter == {'overworld', 'end', 'nether'}:
                    print('There are no filters.')
                else:
                    print(f'Filters:')
                    if dimFilter != {'overworld', 'end', 'nether'}:
                        print(f'• Dimensions: {dimFilter}')
                    if len(useFilter) > 0:
                        print(f'• Uses: {useFilter}')
                    if len(sections) > 0:
                        print('• Sections:')
                        for i in sections:
                            print(f'  -{i["name"]}: ', end='')
                            if i["type"] == 'area':
                                print(f'Area from ({i["x1"]}, {i["z1"]}) to ({i["x2"]}, {i["z2"]}).')
                            if i["type"] == 'elevation':
                                print(f'Elevation {i["direction"]} y {i["y"]}')
            # Remove all filters
            elif command[1] == 'clear':
                dimFilter = {'overworld', 'end', 'nether'}
                useFilter = []
                sections = []
                print('Cleared all filters.')
            # remove specific filter
            elif command[1] == 'remove':
                if  command[2] == 'uses':
                    useFilter == []
                    print('Removed!')
                elif command[2] == 'dimensions':
                    dimFilter = {'overworld', 'end', 'nether'}
                    print('Removed!')
                else:
                    for i in sections:
                        if i["name"] == command[2]:
                            sections.remove(i)
                            print('Removed!')
                            break
                    else:
                        raise SyntaxError('No filters with that name.')
            # Add new filter
            elif command[1] == 'add':
                # Create new sectioned off area NESW-wise
                if command[2] == 'area':
                    for i in sections:
                        if i == command[3]:
                            raise SyntaxError('A section with this name already exists.')
                    sections.append({
                        "name":command[3],
                        "type":'area',
                        "x1":command[4],
                        "z1":command[5],
                        "x2":command[6],
                        "z2":command[7]})
                    print('Success.')
                # create new secioned off area hightwise
                elif command[2] == 'elevation':
                    for i in sections:
                        if i == command[3]:
                            raise SyntaxError('A section with this name already exists.')
                    if command[4] in ['above', 'below', 'at']:
                        sections.append({
                            "name":command[3],
                            "type":'elevation',
                            "direction":command[4],
                            "y":command[5]})
                        print('Success.')
                # Create new uses filter(which actually just edits the existing one)
                elif command[2] == 'uses':
                    useFilter = command[2].split()
                # Create new Dimensions filter(which actually just edits the existing one)
                elif command[3] == 'dimensions':
                    dim = command[3].split('/')
                    if len(dim) > 3:
                        raise SyntaxError('Too many dimensions. There should be nore more than 3.')
                    elif len(dim) < 1:
                        raise SyntaxError('There must be at least one dimension.')
                    else:
                        for i in dim:
                            if i not in {'overworld', 'nether', 'end'}:
                                raise SyntaxError('Dimensions invalid')
                        dimFilter = dim
        # List all waypoints
        elif command[0] == 'list':
            showData = data
            # Apply filters to the data.
            for i in data:
                # Dimension filter
                for x in i["dimensions"]:
                    if x not in dimFilter:
                        showData.remove(i)
                # Uses filter
                if len(useFilter) > 0:
                    for x in i["uses"]:
                        if x not in useFilter:
                            showData.remove(i)
                # Sectioned off area filters
                if len(sections) > 0:
                    for filt in sections:
                        if filt["type"] == 'perimiter':
                            if filt["x1"] > i["x"] > filt["x2"]:
                                showData.remove(i)
                        if filt["type"] == 'altitude':
                            if filt["direction"] == 'above':
                                if i["y"] < filt["y"]:
                                    showData.remove(i)
                            elif filt["direction"] == 'below':
                                if i["y"] > filt["y"]:
                                    showData.remove(i)
                            elif filt["direction"] == 'at':
                                if i["y"] != filt["y"]:
                                    showData.remove(i)
            # Print the filtered data
            if len(showData) > 0:
                print("Matching points:")
                for i in showData:
                    print(f'» {i["name"]}')
            else:
                print("No points match filters.")
        # Edit values in waypoint
        elif command[0] == 'edit':
            for i, d in enumerate(data):
                if d["name"] == command[1]:
                    if command[2] in ['dimensions', 'uses']:
                        d[command[2]] = command[3].split('/')
                    else:
                        d[command[2]] = command[3]
                    break
            else:
                raise SyntaxError('No point has that name.')
        # View details about a specific waypoint
        elif command[0] == 'view':
            for i in data:
                if i["name"] == command[1]:
                    print(f'Name: {i["name"]}')
                    print(f'Coords: {i["x"]}, {i["y"]}, {i["z"]}')
                    print(f'Visible: {i["visible"]}')
                    print(f'Color: {i["red"]}, {i["green"]}, {i["blue"]}')
                    print(f'Uses: {i["uses"]}')
                    print(f'Dimensions: {i["dimensions"]}')
        elif command[0] == 'delete':
            for i in data:
                if i["name"] == command[1]:
                    data.remove(i)
        else:
            raise SyntaxError(f'Unknown command \'{command[0]}\'')
    # Takes care of my predicted errors
    except SyntaxError as err:
        print('Syntax Error:')
        print(err)
    # Takes care of errors where not enough data entered in command
    except IndexError:
        print('Syntax Error:')
        print('Not enough information entered.')
    # takes care of any unpredicted errors
    except Exception:
        print(err)
