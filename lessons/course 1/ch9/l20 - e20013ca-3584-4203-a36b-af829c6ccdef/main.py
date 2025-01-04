# https://www.boot.dev/lessons/e20013ca-3584-4203-a36b-af829c6ccdef

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    return strongholds
