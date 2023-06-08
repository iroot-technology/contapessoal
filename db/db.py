import configparser
from pathlib import Path

base_path = Path(__file__).parent
db_ini = "{}/db.ini".format(base_path)

def config(filename=db_ini, section='contapessoal'):
    #import pdb; pdb.set_trace()
    parser = configparser.ConfigParser()
    parser.read(filename)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

