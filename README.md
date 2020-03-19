# Minepoint
## The Minecraft waypoint viewer and editor

The current features are as follows.

In attempt-3.py:
- CSV file enterpreter with error correction(incomplete)

In command_engine.py:
- Create waypoints
- Edit waypoints
- View waypoints
- Syntax helper
- List all waypoints
- Filter list of waypoints by certain criteria
- Delete waypoints

To test the file enterpreter with a working file,
in line 125, place 'moonbyte.csv' into the class call.
To test the file enterpreter's error correction, 
place 'test.csv' into the class call.


Syntax for the commands in command_engine.py:

- Quit  -  Quit the program
    - -->: quit
- Help  -  Show command syntax
    - -->: help [command]
- Create  -  Create a waypoint
    - -->: create [str:name] [int:x] [int:y] [int:z] [bool:visible] [int:red] [int:green] [int:blue] [use1/use2/...] [dimensions]
    - enter dimensions as a list with '/' separating each
- Filter  -  Filter waypoints
    - -->: filter [subcommand]
    - subcommands:
        - clear
            - -->: filter clear
        - add
            - -->: filter add [subsubcommand]
            - subsubcommands
                - area
                    - -->: filter add area [name] [x1] [z1] [x2] [z2]
                - elevation
                    - -->: filter add elevation [name] [above/below/at] [y]
                - uses
                    - -->: filter add uses [use1/use2/...]
                - dimensions
                    - -->: filter add dimensions [dimensions]
                    - enter dimensions as a list with '/' between each
        - remove
            - -->: filter remove [name]
            - -->: filter remove [uses/dimensions]
        - list
            - -->: filter list
- List  -  List waypoints
    - -->: list
- Edit  -  Edit values in waypoint
    - -->: edit [name] [tag] [value]
- View  -  View details about a specific waypoint
    - -->: view [name]
- Delete  -  Delete waypoints
    - -->: delete [name]

[] means a value instead of literal text. All commands are non case sensitive.


import_csv.py, convert.py, and main.py were my first attempts at the file enterpreter.
However I scrapped those structures.

Turns out this is all I'm submitting because the workspace im using has a limited amout of usage time per month 

