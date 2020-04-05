import re


def parsePrice(priceStr):
    if priceStr is None:
        return -1
    if priceStr != priceStr:
        return -1
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(priceStr)
    if result:
        return priceStr

    prefix = priceStr[0:1]
    if prefix.isdigit() is False:
        priceStr = priceStr[1:]
    unit = priceStr[-1:]
    if unit.isdigit() is False:
        priceStr = priceStr[:-1]
    price = float(priceStr)
    if 'B' == unit.upper():
        price *= 1000000000
    elif 'M' == unit.upper():
        price *= 1000000
    return price


def parseNumber(numberStr):
    if numberStr != numberStr:
        return -1
    else:
        return numberStr