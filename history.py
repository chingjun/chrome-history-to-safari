import sqlite3
import calendar
from collections import OrderedDict
import plistlib
import sys

def load_chrome_history(filename):
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    c = sqlite3.connect(filename).cursor()
    c.row_factory = dict_factory

    return c.execute('''
        SELECT u.*, (u.last_visit_time - 11644473600000000) time FROM urls u
        ''').fetchall()

def transform_chrome_to_safari(history):
    reference = calendar.timegm((2001,1,1,0,0,0,0,0,0))
    return [ OrderedDict([
            ('', i['url']),
            ('D', [1]),
            ('lastVisitedDate', str(int((i['time']/1000000.0 - reference)*10)/10.0)),
            ('title', i['title']),
            ('visitCount', i['typed_count'] + i['visit_count']),
        ]) for i in sorted(history, key = (lambda x: x['time']), reverse = True) ]

def write_safari_history(filename, history):        
    data = {
        'WebHistoryDates' : history,
        'WebHistoryFileVersion' : 1,
    }
    plistlib.writePlist(data, filename)

if len(sys.argv) < 3:
    print >> sys.stderr, 'Usage: python history.py [Chrome history file] [output file]'
    sys.exit(1)

write_safari_history(sys.argv[2], transform_chrome_to_safari(load_chrome_history(sys.argv[1])))
