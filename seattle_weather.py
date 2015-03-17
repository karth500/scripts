#!/Users/ramakk/anaconda/bin/python
import urllib2
import json
import codecs
import locale
import sys

# Wrap sys.stdout into a StreamWriter to allow writing unicode.
# answer from - http://stackoverflow.com/questions/4545661/unicodedecodeerror-when-redirecting-to-file
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

cloud_icon = u'\u2601'
rain_icon = u'\u2602'
sun_icon = u'\u2600'
snow_icon = u'\u2603'
deg_c = u'\u2103'


def get_icon(conditions):
    if conditions:
        if 'rain' in conditions.lower():
            return rain_icon
        elif 'cloud' in conditions.lower():
            return cloud_icon
        elif 'snow' in conditions.lower():
            return snow_icon

    return sun_icon


def get_weather(loc='seattle, wa'):
    f = urllib2.urlopen('http://api.wunderground.com/api/85e65207d51c7de3/geolookup/conditions/q/WA/Seattle.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    temp_c = parsed_json['current_observation']['temp_c']
    weather = str(temp_c) + deg_c + ' ' + get_icon(parsed_json['current_observation']['weather'])
    weather.encode('utf-8')
    return weather


def main():
    print get_weather()


if __name__=="__main__":
    main()
