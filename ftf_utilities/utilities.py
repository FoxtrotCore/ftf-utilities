import json, os.path
from .color import Color
from .cstring import CString
from .mode import Mode

def log(mode, message):
    """
    mode: A Mode enumeration that determines the message type (See ftf_utilities.Mode)
    message: A message to forward to stdout

    Prints a message to stdout with color and formatting
    """
    if(isinstance(mode, Mode)):
        if(mode == Mode.INFO): color = Color.GREEN
        elif(mode == Mode.DEBUG): color = Color.BLUE
        elif(mode == Mode.WARN): color = Color.B_YELLOW
        else: color = Color.RED
        print("[" + CString(color, mode.name) + "]: " + CString(Color.B_WHITE, message))
    else: raise TypeError("Expected: (" + str(type(Mode)) + "), got: (" + str(type(mode)) + ")")

def load_json(filename):
    """
    filename: Path to JSON file to read from

    Loads a JSON  file and returns it as a python dictionary
    """
    if(not os.path.exists(filename)): raise FileNotFoundError
    file = open(filename)
    file_data = file.read()
    file.close()
    return json.loads(file_data)

def dump_json(filename, dictionary, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=2, separators=None, default=None, sort_keys=True):
    """
    filename:  Path to JSON file to write to
    dictionary: Python dictionary to transpose into JSON
    kwargs: Optional arguments for controlling the JSON output

    Takes a python dictionary and dumps it to a file as JSON
    """
    data = json.dumps(dictionary, skipkeys=skipkeys,
                                  ensure_ascii=ensure_ascii,
                                  check_circular=check_circular,
                                  allow_nan=allow_nan,
                                  cls=cls,
                                  indent=indent,
                                  separators=separators,
                                  default=default,
                                  sort_keys=sort_keys)

    # Write the raw JSON data to the specified file
    file = open(filename, mode='w+')
    file.write(data)
    file.close()

    return dictionary
