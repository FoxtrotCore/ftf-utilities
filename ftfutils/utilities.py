import json
from color import *
from cstring import *
from mode import *

def log(mode, message):
    if(isinstance(mode, Mode)):
        if(mode == Mode.INFO): color = Color.GREEN
        elif(mode == Mode.DEBUG): color = Color.BLUE
        elif(mode == Mode.WARN): color = Color.B_YELLOW
        else: color = Color.RED
        print("[" + CString(color, mode.name) + "]: " + CString(Color.B_WHITE, message))
    else: raise TypeError("Expected: (" + str(type(Mode)) + "), got: (" + str(type(mode)) + ")")

def load_json(file_path):
    # Read the raw JSON data
    file = open(file_path)
    file_data = file.read()
    file.close()

    # Transpose raw JSON into dictionary, store it in the object instance
    return json.loads(file_data)

def dump_json(file_path, dictionary):
    # Transpose dictionary into raw JSON
    data = json.dumps(dictionary, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=2, separators=None, default=None, sort_keys=True)

    # Write the raw JSON data to the specified file
    file = open(file_path, mode='w+')
    file.write(data)
    file.close()

    return dictionary
