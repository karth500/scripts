#!/Users/ramakk/anaconda/bin/python
from sh import ioreg
import re
import codecs
import locale
import sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
# answer from - http://stackoverflow.com/questions/4545661/unicodedecodeerror-when-redirecting-to-file
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

batt_params = {}
batt_icon = u'\U0001F50B'
charging_icon = u'\U0001F50C'

batt_parse = re.compile(r'"MaxCapacity"\s*=\s*\d+|"CurrentCapacity"\s*=\s*\d+|"IsCharging"\s*=\s*\w+|"FullyCharged"\s*=\s*\w+')


def parse_batt_params():
    ioreg_batt_params = ioreg("-n", "AppleSmartBattery", "-r")
    param_list = []
    batt_param_str = batt_parse.findall(unicode(ioreg_batt_params))
    for param_str in batt_param_str:
        param_str = param_str.replace('"', '').replace(' ', '')
        param_list.append(tuple(param_str.split('=')))
    batt_params.update(param_list)


def print_batt_stats():
    current_charge = float(batt_params['CurrentCapacity'])/float(batt_params['MaxCapacity'])
    icon = charging_icon if batt_params['IsCharging'] is u'Yes' else batt_icon
    print u'{0:3.2f}% {1}'.format(current_charge*100, icon)


def main():
    parse_batt_params()
    print_batt_stats()


if __name__=="__main__":
    main()
