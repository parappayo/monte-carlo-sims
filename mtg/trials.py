import math


def run(testFunc, count, bucketSize=None):
    """Runs the given testFunc count times, returns a dict of results totals."""
    results = {}
    for n in range(count):
        result = None
        if bucketSize == None:
            result = testFunc()
        else:
            result = math.floor(testFunc() / bucketSize) * bucketSize
        if not result in results:
            results[result] = 1
        else:
            results[result] += 1
    return results


def normalizeCounts(data, trialCount):
    """Given a dict of trial results, normalizes each total to be in the range [0,1]."""
    for d in data.items():
        data[d[0]] = d[1] / trialCount


def formatToCSV(data, keyCaptions=None):
    """Given a dict of trial results, returns a comma separated value format string."""
    sortedData = sorted(data.items())
    keys = [d[0] for d in sortedData]
    values = [d[1] for d in sortedData]
    if keyCaptions == None:
        return ','.join(map(str, keys)) + '\n' + ','.join(map(str, values))
    else:
        return ','.join(map(lambda k: keyCaptions[k], keys)) + '\n' + ','.join(map(str, values))
