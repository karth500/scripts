import requests
from multiprocessing import Pool as ThreadPool
import time

locs = ['Seattle,WA', 98119, 98109, 02452, 48105, 10001, 10002, 10005]
weather_api = 'http://api.openweathermap.org/data/2.5/weather?q={0}'


def get_weather(loc):
    return requests.get(weather_api.format(str(loc))).json()


def main():
    print "No threads"
    n = time.time()
    for l in locs:
        print get_weather(l)
    print "Without threads = " + str(time.time() - n)

    t = ThreadPool(8)
    s = time.time()
    w_results = t.map(get_weather , locs)
    print "Map time = " + str(time.time() - s)
    for w in w_results:
        print w

    print "\n\n"

    a = time.time()
    ws = t.map_async(get_weather, locs)
    w_results = ws.get()
    print "async map time = " + str(time.time() - a)
    for w in w_results:
        print w
    print "async map time = " + str(time.time() - a)

    print "\n\n"

    b = time.time()
    async_results = [t.apply_async(get_weather, args=(l,)) for l in locs]

    print "async apply time split 1 = " + str(time.time() - b)
    for a_r in async_results:
        print a_r.get()
    print "async apply time split 2 = " + str(time.time() - b)


if __name__=="__main__":
    main()
