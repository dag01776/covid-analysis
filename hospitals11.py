# e!/usr/bin/python
# or
#!/bin/bash

import re
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import date, timedelta
import datetime
import sys
import pandas as pd

# from today back to March 15 ;
previousDates = []
startDate = date(2020, 3, 17)
verboseDate = datetime.datetime.now()
todaysDate = date(verboseDate.year, verboseDate.month, verboseDate.day)
endDate = todaysDate
if len(sys.argv) > 1:
    endDate = todaysDate + timedelta(days=int(sys.argv[1]))
    print(startDate, todaysDate, todaysDate + timedelta(days=int(sys.argv[1])))

for i in range((endDate - startDate).days):
    previousDates.append(str(startDate + timedelta(days=i)))
print("previousDates", previousDates)

allStates = [
    "Mississippi",
    "Oklahoma",
    "Missouri",
    "Minnesota",
    "Alaska",
    "Illinois",
    "Arkansas",
    "New Mexico",
    "Ohio",
    "Indiana",
    "Maryland",
    "Louisiana",
    "Texas",
    "Wyoming",
    "Arizona",
    "Wisconsin",
    "Michigan",
    "Kansas",
    "Utah",
    "Virginia",
    "Oregon",
    "Connecticut",
    "New York",
    "California",
    "Massachusetts",
    "South Carolina",
    "New Hampshire",
    "Vermont",
    "Georgia",
    "North Dakota",
    "Pennsylvania",
    "West Virginia",
    "Florida",
    "Hawaii",
    "Kentucky",
    "Rhode Island",
    "Nebraska",
    "Iowa",
    "Alabama",
    "South Dakota",
    "Colorado",
    "Idaho",
    "New Jersey",
    "Washington",
    "North Carolina",
    "Tennessee",
    "Montana",
    "Nevada",
    "Delaware",
    "Maine",
]

showStates = [
    # "All",
    "Mississippi",
    "Oklahoma",
    "Missouri",
    "Minnesota",
    "Alaska",
    "Illinois",
    "Arkansas",
    "New Mexico",
    "Ohio",
    "Indiana",
    "Maryland",
    "Louisiana",
    "Texas",
    "Wyoming",
    "Arizona",
    "Wisconsin",
    "Michigan",
    "Kansas",
    "Utah",
    "Virginia",
    "Oregon",
    "Connecticut",
    "New York",
    "California",
    "Massachusetts",
    "South Carolina",
    "New Hampshire",
    "Vermont",
    "Georgia",
    "North Dakota",
    "Pennsylvania",
    "West Virginia",
    "Florida",
    "Hawaii",
    "Kentucky",
    "Rhode Island",
    "Nebraska",
    "Iowa",
    "Alabama",
    "South Dakota",
    "Colorado",
    "Idaho",
    "New Jersey",
    "Washington",
    "North Carolina",
    "Tennessee",
    "Montana",
    "Nevada",
    "Delaware",
    "Maine",
]

t6 = {
    "All": 1772369,
    "New York": 302280,
    "California": 116533,
    "Florida": 114580,
    "Washington": 87911,
    "New Jersey": 82166,
    "Pennsylvania": 77771,
    "Massachusetts": 71937,
    "Texas": 70938,
    "Louisiana": 60325,
    "Illinois": 58983,
    "Michigan": 45748,
    "Tennessee": 45300,
    "Ohio": 43756,
    "North Carolina": 40045,
    "Maryland": 28337,
    "Georgia": 27832,
    "Arizona": 27410,
    "Missouri": 27173,
    "Minnesota": 26777,
    "Wisconsin": 25971,
    "Colorado": 25773,
    "Virginia": 23671,
    "Connecticut": 23270,
    "Indiana": 22652,
    "Oregon": 20624,
    "Nevada": 19908,
    "South Carolina": 18976,
    "Kentucky": 18767,
    "New Mexico": 16909,
    "Hawaii": 13314,
    "Alabama": 13078,
    "Arkansas": 11143,
    "Iowa": 10841,
    "Idaho": 10261,
    "West Virginia": 8838,
    "New Hampshire": 8370,
    "Kansas": 8223,
    "Rhode Island": 8102,
    "Mississippi": 7218,
    "Delaware": 6994,
    "District Of Columbia": 6834,
    "Montana": 6789,
    "North Dakota": 6787,
    "Vermont": 6582,
    "Maine": 6544,
    "Alaska": 6284,
    "Nebraska": 5933,
    "South Dakota": 5593,
    "Utah": 30892,
    "Wyoming": 3227,
    "Oklahoma": 2655,
}

t7 = {
    "All": 2075739,
    "New York": 340058,
    "New Jersey": 94974,
    "Michigan": 50332,
    "California": 143800,
    "Louisiana": 74655,
    "Massachusetts": 81344,
    "Pennsylvania": 91278,
    "Florida": 139669,
    "Illinois": 68732,
    "Georgia": 33785,
    "Texas": 88649,
    "Washington": 91375,
    "Connecticut": 29036,
    "Indiana": 28764,
    "Colorado": 28094,
    "Ohio": 50838,
    "Maryland": 31627,
    "Tennessee": 52874,
    "Virginia": 28645,
    "North Carolina": 41082,
    "Missouri": 31969,
    "Wisconsin": 29014,
    "Arizona": 33375,
    "South Carolina": 23680,
    "Alabama": 14916,
    "Nevada": 21818,
    "Mississippi": 20547,
    "Utah": 34647,
    "Oklahoma": 13293,
    "Rhode Island": 8628,
    "District Of Columbia": 7823,
    "Idaho": 11898,
    "Oregon": 23007,
    "Kentucky": 21604,
    "Minnesota": 29260,
    "Iowa": 12718,
    "Arkansas": 13691,
    "Delaware": 8568,
    "Kansas": 9514,
    "New Mexico": 22245,
    "New Hampshire": 8734,
    "Vermont": 7129,
    "Maine": 6607,
    "Nebraska": 7453,
    "West Virginia": 12059,
    "Hawaii": 13665,
    "South Dakota": 6270,
    "Montana": 6985,
    "North Dakota": 7703,
    "Wyoming": 3929,
    "Alaska": 6913,
}

t8 = {
    "All": 2208901,
    "New York": 365153,
    "New Jersey": 100326,
    "Michigan": 51708,
    "California": 144264,
    "Louisiana": 81406,
    "Massachusetts": 87511,
    "Pennsylvania": 98538,
    "Florida": 144570,
    "Illinois": 75066,
    "Georgia": 38787,
    "Texas": 96258,
    "Washington": 92073,
    "Connecticut": 31700,
    "Indiana": 30869,
    "Colorado": 29199,
    "Maryland": 38462,
    "Ohio": 53341,
    "Tennessee": 56618,
    "Virginia": 30645,
    "North Carolina": 42987,
    "Missouri": 34110,
    "Wisconsin": 32871,
    "Arizona": 34564,
    "South Carolina": 24634,
    "Alabama": 18982,
    "Nevada": 22865,
    "Mississippi": 20635,
    "Utah": 36116,
    "Oklahoma": 13345,
    "Rhode Island": 12132,
    "District Of Columbia": 8283,
    "Kentucky": 21620,
    "Oregon": 24564,
    "Idaho": 11898,
    "Minnesota": 30753,
    "Iowa": 13966,
    "Delaware": 8744,
    "Arkansas": 14909,
    "Kansas": 10183,
    "New Mexico": 23807,
    "New Hampshire": 9177,
    "Vermont": 7749,
    "Maine": 6625,
    "Nebraska": 7978,
    "West Virginia": 12859,
    "Hawaii": 15149,
    "South Dakota": 6748,
    "Montana": 7398,
    "North Dakota": 8607,
    "Wyoming": 4064,
    "Alaska": 7068,
}

t9 = {
    "All": 2353096,
    "New York": 391549,
    "New Jersey": 100326,
    "Michigan": 52866,
    "California": 163500,
    "Massachusetts": 94958,
    "Pennsylvania": 105602,
    "Louisiana": 86919,
    "Florida": 158375,
    "Illinois": 80857,
    "Texas": 106134,
    "Georgia": 41085,
    "Connecticut": 33502,
    "Washington": 92073,
    "Indiana": 32133,
    "Colorado": 31180,
    "Maryland": 41529,
    "Ohio": 55985,
    "Tennessee": 59849,
    "Virginia": 33026,
    "North Carolina": 47809,
    "Missouri": 38282,
    "Arizona": 37178,
    "Wisconsin": 34309,
    "Alabama": 20605,
    "South Carolina": 27367,
    "Nevada": 26074,
    "Mississippi": 20635,
    "Utah": 38373,
    "Rhode Island": 14008,
    "Oklahoma": 3205,
    "District Of Columbia": 8724,
    "Kentucky": 23170,
    "Idaho": 13094,
    "Oregon": 25627,
    "Iowa": 14973,
    "Minnesota": 32294,
    "Delaware": 9890,
    "Arkansas": 15702,
    "Kansas": 10775,
    "New Mexico": 23931,
    "New Hampshire": 9551,
    "Vermont": 8181,
    "Nebraska": 8707,
    "Maine": 6625,
    "West Virginia": 13863,
    "South Dakota": 7147,
    "Hawaii": 15751,
    "Montana": 7860,
    "North Dakota": 8990,
    "Wyoming": 4064,
    "Alaska": 7223,
}

t10 = {
    "All": 2538888,
    "New York": 417885,
    "New Jersey": 113523,
    "Michigan": 72044,
    "California": 164863,
    "Massachusetts": 102372,
    "Pennsylvania": 113019,
    "Louisiana": 92280,
    "Florida": 167141,
    "Illinois": 87527,
    "Texas": 115918,
    "Georgia": 46147,
    "Connecticut": 33502,
    "Washington": 92999,
    "Maryland": 44448,
    "Indiana": 35040,
    "Colorado": 32653,
    "Ohio": 58573,
    "Tennessee": 62799,
    "Virginia": 35459,
    "North Carolina": 57645,
    "Missouri": 40740,
    "Arizona": 37734,
    "Wisconsin": 36293,
    "South Carolina": 28183,
    "Alabama": 20605,
    "Nevada": 27286,
    "Mississippi": 21101,
    "Utah": 40762,
    "Rhode Island": 15432,
    "Oklahoma": 22370,
    "Kentucky": 24288,
    "District Of Columbia": 9355,
    "Idaho": 13764,
    "Iowa": 15953,
    "Oregon": 27224,
    "Minnesota": 33894,
    "Delaware": 9890,
    "Arkansas": 17151,
    "Kansas": 11414,
    "New Mexico": 27098,
    "New Hampshire": 9958,
    "Vermont": 8657,
    "Nebraska": 9474,
    "Maine": 6625,
    "West Virginia": 15101,
    "South Dakota": 7647,
    "Hawaii": 16149,
    "Montana": 8297,
    "North Dakota": 9608,
    "Wyoming": 5255,
    "Alaska": 7432,
}

t11 = {
    "All": 2670674,
    "New York": 440980,
    "New Jersey": 120193,
    "Michigan": 76014,
    "Massachusetts": 108776,
    "California": 164863,
    "Pennsylvania": 120153,
    "Louisiana": 96915,
    "Illinois": 92779,
    "Florida": 173187,
    "Texas": 120533,
    "Georgia": 51715,
    "Connecticut": 39831,
    "Washington": 92999,
    "Maryland": 47238,
    "Indiana": 39215,
    "Colorado": 34873,
    "Ohio": 60471,
    "Tennessee": 66828,
    "Virginia": 37999,
    "North Carolina": 60393,
    "Missouri": 43172,
    "Arizona": 40530,
    "Alabama": 20605,
    "Wisconsin": 37893,
    "South Carolina": 30093,
    "Nevada": 28335,
    "Mississippi": 21101,
    "Rhode Island": 18207,
    "Utah": 42546,
    "Oklahoma": 22511,
    "Kentucky": 24567,
    "District Of Columbia": 10039,
    "Iowa": 17132,
    "Delaware": 11103,
    "Oregon": 28638,
    "Minnesota": 35404,
    "Idaho": 14308,
    "Kansas": 12343,
    "Arkansas": 18617,
    "New Mexico": 28692,
    "New Hampshire": 10925,
    "Vermont": 9258,
    "Nebraska": 10197,
    "South Dakota": 8004,
    "Maine": 6625,
    "West Virginia": 15819,
    "Hawaii": 17531,
    "Montana": 8581,
    "North Dakota": 10080,
    "Wyoming": 5353,
    "Alaska": 7732,
}

t12 = {
    "All": 2832258,
    "New York": 461601,
    "New Jersey": 126735,
    "Massachusetts": 116730,
    "Michigan": 76014,
    "California": 203400,
    "Pennsylvania": 124890,
    "Illinois": 100735,
    "Louisiana": 104045,
    "Florida": 185520,
    "Texas": 124553,
    "Georgia": 54453,
    "Connecticut": 41220,
    "Washington": 92999,
    "Maryland": 47238,
    "Indiana": 42489,
    "Colorado": 37153,
    "Ohio": 63243,
    "Tennessee": 70747,
    "Virginia": 39985,
    "North Carolina": 62139,
    "Missouri": 45064,
    "Alabama": 20605,
    "Arizona": 42109,
    "Wisconsin": 39257,
    "South Carolina": 31426,
    "Nevada": 29579,
    "Mississippi": 21101,
    "Rhode Island": 20350,
    "Utah": 44234,
    "Oklahoma": 22511,
    "Kentucky": 25866,
    "District Of Columbia": 10640,
    "Delaware": 11820,
    "Minnesota": 37421,
    "Iowa": 17592,
    "Oregon": 29758,
    "Idaho": 14308,
    "Kansas": 13253,
    "Arkansas": 19722,
    "New Mexico": 30515,
    "New Hampshire": 10925,
    "Nebraska": 10710,
    "South Dakota": 8553,
    "Vermont": 9841,
    "Maine": 12168,
    "West Virginia": 16257,
    "Hawaii": 18827,
    "Montana": 8913,
    "North Dakota": 10350,
    "Alaska": 8038,
    "Wyoming": 5614,
}

t13 = {
    "All": 2943955,
    "Mississippi": 21101,
    "Iowa": 17592,
    "Oklahoma": 28225,
    "Delaware": 12304,
    "Minnesota": 38427,
    "Alaska": 8038,
    "Illinois": 105768,
    "District Of Columbia": 10934,
    "Arkansas": 21014,
    "New Mexico": 31970,
    "Indiana": 44539,
    "Maryland": 51751,
    "Louisiana": 108091,
    "Texas": 133226,
    "Wyoming": 5963,
    "Arizona": 42109,
    "Wisconsin": 40197,
    "Michigan": 76014,
    "Kansas": 13864,
    "Utah": 45787,
    "Virginia": 41401,
    "Oregon": 31121,
    "Connecticut": 44309,
    "Tennessee": 76195,
    "California": 203400,
    "Massachusetts": 122049,
    "West Virginia": 16748,
    "South Carolina": 31426,
    "New Hampshire": 11610,
    "Vermont": 10365,
    "Georgia": 57038,
    "North Dakota": 10781,
    "Pennsylvania": 129792,
    "Florida": 197996,
    "Hawaii": 18827,
    "Kentucky": 26683,
    "Rhode Island": 20350,
    "Nebraska": 11384,
    "Missouri": 45064,
    "Ohio": 63243,
    "Alabama": 29140,
    "South Dakota": 9002,
    "Colorado": 37153,
    "Idaho": 14881,
    "New Jersey": 131219,
    "Washington": 92999,
    "North Carolina": 63388,
    "New York": 478357,
    "Montana": 9098,
    "Nevada": 30628,
    "Maine": 12168,
}

t14 = {
    "All": 3065019,
    "Mississippi": 21101,
    "Iowa": 17592,
    "Oklahoma": 28225,
    "Delaware": 12869,
    "Minnesota": 39241,
    "Alaska": 8348,
    "Illinois": 110616,
    "District Of Columbia": 11518,
    "Arkansas": 21203,
    "New Mexico": 32850,
    "Indiana": 46017,
    "Maryland": 53733,
    "Louisiana": 118422,
    "Texas": 146467,
    "Wyoming": 6129,
    "Arizona": 44096,
    "Wisconsin": 41552,
    "Michigan": 76014,
    "Kansas": 14147,
    "Utah": 46476,
    "Virginia": 42763,
    "Oregon": 31121,
    "Connecticut": 45841,
    "New York": 499143,
    "California": 212900,
    "Massachusetts": 126551,
    "West Virginia": 17224,
    "South Carolina": 33872,
    "New Hampshire": 11847,
    "Vermont": 10585,
    "Georgia": 61795,
    "North Dakota": 10916,
    "Pennsylvania": 133631,
    "Florida": 205413,
    "Hawaii": 19857,
    "Kentucky": 27697,
    "Rhode Island": 23926,
    "Nebraska": 11757,
    "Missouri": 45064,
    "Ohio": 67874,
    "Alabama": 33050,
    "South Dakota": 9296,
    "Colorado": 39580,
    "Idaho": 15398,
    "New Jersey": 131219,
    "Washington": 92999,
    "North Carolina": 65039,
    "Tennessee": 78831,
    "Montana": 9234,
    "Nevada": 32178,
    "Maine": 12168,
}


beds = {
    "Mississippi": 9857,
    "Oklahoma": 9174,
    "Wyoming": 1677,
    "Minnesota": 11673,
    "Illinois": 26231,
    "Georgia": 21099,
    "Arkansas": 7995,
    "New Mexico": 3124,
    "Ohio": 27099,
    "Indiana": 15051,
    "Maryland": 9511,
    "Louisiana": 12702,
    "Idaho": 2811,
    "Tennessee": 16407,
    "Arizona": 11451,
    "Iowa": 7837,
    "New York": 43490,
    "Michigan": 20672,
    "Kansas": 7960,
    "Utah": 4778,
    "Virginia": 14841,
    "Oregon": 5587,
    "Connecticut": 5904,
    "Montana": 2920,
    "New Hampshire": 2363,
    "Massachusetts": 13234,
    "South Carolina": 10231,
    "California": 58889,
    "Vermont": 1084,
    "Delaware": 1733,
    "North Dakota": 2713,
    "Pennsylvania": 30740,
    "West Virginia": 5638,
    "Florida": 46237,
    "Hawaii": 2227,
    "Kentucky": 11837,
    "Alaska": 1332,
    "Nebraska": 5766,
    "Missouri": 15753,
    "Wisconsin": 10123,
    "Alabama": 12585,
    "Rhode Island": 1842,
    "South Dakota": 3515,
    "Colorado": 9059,
    "New Jersey": 17650,
    "Washington": 10718,
    "North Carolina": 18236,
    "District of Columbia": 2570,
    "Texas": 55220,
    "Nevada": 5355,
    "Maine": 2782,
}

populations = {
    "Mississippi": 2976149,
    "Oklahoma": 3956971,
    "Wyoming": 578759,
    "Minnesota": 5639632,
    "Illinois": 12671821,
    "Georgia": 10617423,
    "Arkansas": 3017825,
    "New Mexico": 2096829,
    "Ohio": 11689100,
    "Indiana": 6732219,
    "Maryland": 6045680,
    "Louisiana": 4648794,
    "Idaho": 1787065,
    "Tennessee": 6833174,
    "Arizona": 7278717,
    "Iowa": 3155070,
    "New York": 19453561,
    "Michigan": 9986857,
    "Kansas": 2913314,
    "Utah": 3205958,
    "Virginia": 8535519,
    "Oregon": 4217737,
    "Connecticut": 3565287,
    "Montana": 1068778,
    "New Hampshire": 1359711,
    "Massachusetts": 6949503,
    "Puerto Rico": 3193694,
    "South Carolina": 5148714,
    "California": 39512223,
    "Vermont": 623989,
    "Delaware": 973764,
    "North Dakota": 762062,
    "Pennsylvania": 12801989,
    "West Virginia": 1792147,
    "Florida": 21477737,
    "Hawaii": 1415872,
    "Kentucky": 4467673,
    "Alaska": 731545,
    "Nebraska": 1934408,
    "Missouri": 6137428,
    "Wisconsin": 5822434,
    "Alabama": 4903185,
    "Rhode Island": 1059361,
    "South Dakota": 884659,
    "Colorado": 5758736,
    "New Jersey": 8882190,
    "Washington": 7614893,
    "North Carolina": 10488084,
    "District of Columbia": 705749,
    "Texas": 28995881,
    "Nevada": 3080156,
    "Maine": 1344212,
}

populations["All"] = sum(populations.values())


def avgL(x):
    rL = [x[0]]
    for i in range(len(x) - 2):
        rL.append((x[i] + x[i + 1] + x[i + 2]) / 3)
    rL.append(x[-1])
    return rL


def timesList(*, values, multiply_by):
    return list(map(lambda element: element * multiply_by, values))


def getTest(state, a, b, c, d, e, f, g):
    return [
        b[state] - a[state],
        c[state] - b[state],
        d[state] - c[state],
        e[state] - d[state],
        f[state] - e[state],
        g[state] - f[state],
    ]


def dieEst(allD, newCases, dieRate):
    kL = []
    kM = diffL(allD)
    for px in range(len(newCases) + 15):
        kL.append(0)
    for py in range(len(newCases)):
        pZ = getNorm(6, 2, int(max(1, dieRate * newCases[py])))
        for pR in range(15):
            kL[py + pR] += pZ[pR]
    return kL


def getNorm(u, s, n):
    s3 = np.random.normal(u, s, n)
    #  defaults to 7,2, n   capped at 1 and 15
    gL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in s3:
        gL[(min(max(int(x), 1), 15))] += 1
    return gL


print(sum(getNorm(7, 2, 100)), getNorm(7, 2, 100))


def notDB(x):
    return round(math.exp(1.0 * x * math.log(2) / 6), 2)


def recoveries(x):
    if len(x) < 15:
        return [0]
    y = len(x)
    zL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for w in range(len(x) - 14):
        zL.append(int(0.75 * x[w]))
    return zL


def addSubList(a, b, thisSign):
    zL = []
    for i in range(min(len(a), len(b))):
        zL.append(a[i] + (thisSign * b[i]))
    return zL


def diffL(x):
    rL = [x[0]]
    for p in range(len(x) - 1):
        rL.append(x[1 + p] - x[p])
    return rL


def dbRed(x, y):  # Reduction in CB,  x as percent of y on Log scale
    z = 1.0 * (y - x) / y
    return round(6.0 * math.log(z) / math.log(2), 2)


def dbList(x):
    rL = [0]
    for p in range(len(x) - 1):
        rL.append(round(6.0 * math.log(x[p + 1] / x[p]) / math.log(2), 1))
    return rL


def divideL(a, b):
    tL = []
    print(a)
    print(b)
    for q in range(len(a)):
        tL.append(a[q] / b[q])
    print(tL)
    return tL


zw = divideL([5, 10, 15, 20], [50, 100, 150, 200])


def getRate(state, hist):
    db = 6.0 / math.log(2)
    rL = []
    zL = []
    for z in hist.keys():
        if state in z and (len(z) - 10 == len(state)) and int(hist[z][0]) > 9:
            rL.append([z[5:10], int(hist[z][0]), int(hist[z][1])])
    pL = sorted(rL)
    for f in range(len(pL) - 1):
        if pL[f][2] > 0:
            zL.append(
                [
                    pL[f + 1][0],
                    pL[f + 1][1],
                    round(1.0 * pL[f + 1][1] / pL[f][1], 2),
                    pL[f + 1][2],
                    round(1.0 * pL[f + 1][2] / pL[f][2], 2),
                ]
            )
        else:
            zL.append(
                [
                    pL[f + 1][0],
                    pL[f + 1][1],
                    round(1.0 * pL[f + 1][1] / pL[f][1], 2),
                    pL[f + 1][2],
                    1,
                ]
            )
    return zL


def dropSpace(x):
    if len(x.split(" ")) == 2:
        return x.split(" ")[0] + "_" + x.split(" ")[1]
    return x


def dateNum(x):
    y = x.split("-")
    return date(int(y[0]), int(y[1]), int(y[2]))


def getLine(state, target):
    rL = []
    # print ("KEYS", sorted(state.keys()));
    for a in sorted(state.keys()):
        #  print (a, state[a].keys()) ;
        rL.append(state[a][target])
    return rL


z5 = {}

hist = {}

records_df = pd.read_csv("hospitals4-12.csv")

filtered_records_df = records_df[(records_df['location_name'].isin(allStates)) & (records_df['date'].isin(previousDates))]
hist_with_tuple_keys = filtered_records_df.set_index(['location_name', 'date']).to_dict(orient='index')
hist_items = [
    {
        location_name_date_tuple[0]: {
            location_name_date_tuple[1]: {
                key: item[key] for key in ['allbed_mean', 'ICUbed_mean', 'InvVen_mean', 'deaths_mean', 'totdea_mean']
            }
        }
    }
    for location_name_date_tuple, item in hist_with_tuple_keys.items()]
print(hist_items)
result = {}
for d in hist_items:
    result.update(d)

print(result)
exit()
# for index, row in records_df.iterrows():
#     if row["location_name"] in allStates and row["date"] in previousDates:
#         state_and_date_string_key = row['date'] + row["location_name"]
#         hist[state_and_date_string_key] = list(
#             row[
#                 [
#                     "allbed_mean",
#                     "ICUbed_mean",
#                     "InvVen_mean",
#                     "deaths_mean",
#                     "totdea_mean",
#                 ]
#             ].values
#         )


for t in hist.keys():
    state = t[10:]
    thisDate = t[5:10]
    if state not in z5.keys():
        z5[state] = {}
    if thisDate not in z5[state].keys():
        z5[state][thisDate] = {
            "admits": hist[t][0],
            "icu": hist[t][1],
            "vents": hist[t][2],
            "dayDeaths": hist[t][3],
            "allDeaths": hist[t][4],
        }
# for p6 in sorted(z5['Washington'].keys()) : print ("KEYS New York", p6) ;

stateDate = {}
sL = []
states = open("us-states-16.csv", "r")
for g in states:
    h = g[:-1].split(",")
    if g[:4] == "2020" and h[1] in allStates:
        if h[1] in allStates and h[1] not in z5.keys():
            z5[h[1]] = {}
        thisDate = g[5:10]
        ## if thisDate in z5[h[1]].keys() : z5[h[1]][thisDate]['cases'] = int(h[3]) ;
        ####### print ("HERE", h[1], thisDate, int(h[3]), int(h[4])) ;
        #######if thisDate not in z5[h[1]].keys() and g[6] == '4' :  z5[h[1]][thisDate] = {} ;
        if thisDate in z5[h[1]].keys():
            z5[h[1]][thisDate]["cases"] = int(h[3])
            z5[h[1]][thisDate]["allDeaths"] = int(h[4])
        stateDate[h[0] + h[1]] = [int(h[3]), int(h[4])]
        if h[0] + "All" not in stateDate.keys():
            stateDate[h[0] + "All"] = [int(h[3]), int(h[4])]
        else:
            stateDate[h[0] + "All"][0] += int(h[3])
            stateDate[h[0] + "All"][1] += int(h[4])

z5["All"] = {}
for df in previousDates:
    z5["All"][df[5:10]] = {}
    for pt in ["cases", "admits", "icu", "dayDeaths", "allDeaths", "vents"]:
        z5["All"][df[5:10]][pt] = 0
print("z5-All", z5["All"]["04-14"])


for state in allStates:
    for rp in previousDates:
        month_day_date = rp[5:10]
        for column_name in ["cases", "admits", "icu", "vents", "dayDeaths", "allDeaths"]:
            print(state)
            desired_value = z5[state][month_day_date][column_name]
            z5["All"][month_day_date][column_name] += desired_value

print(z5["All"]["04-14"])

sL = []
for x in showStates:
    sL.append([z5[x][previousDates[-1][5:10]]["cases"], x])
sortedShowStates = sorted(sL, reverse=True)

print("sortedShowStates", sortedShowStates)
showStates2 = []
for x in sortedShowStates:
    showStates2.append(x[1])
print("showStates2", showStates2)

for thisState in showStates2:
    cases = getLine(z5[thisState], "cases")
    if max(diffL(cases)) > 500:
        print()
        fixedState = dropSpace(thisState) + (16 - len(thisState)) * " "
        z = getRate(thisState, stateDate)

        ######print ("ZZZ555 THIS STATE", z5[thisState]) ;
        allDeaths = getLine(z5[thisState], "allDeaths")
        admits = getLine(z5[thisState], "admits")
        icu = getLine(z5[thisState], "icu")
        dayDeaths = getLine(z5[thisState], "dayDeaths")

        allCasesDB = dbList(cases)
        totalCases = cases[-1]
        newCases = diffL(cases)
        doubleRate = int(0.5 + 18 / (sum(dbList(cases)[-3:])))
        recov = recoveries(newCases)
        died = z[-1][3]
        wL = []
        for i in range(len(z) - 1):
            if i < 15:
                wL.append(int(z[i + 1][1] - z[i][1] - (z[i + 1][3] - z[i][3])))
                ###  no reductions for cured
            if 14 < i:
                wL.append(
                    int(
                        z[i + 1][1]
                        - z[i][1]
                        - (z[i + 1][3] - z[i][3])
                        - 0.8 * (wL[i - 13])
                    )
                )
                ### reduced by 80% of net new cases from 14 days earlier
            active = z[-1][1] - z[-1][3] - sum(wL[:-14])
            ##### check this :14  ########

        rX = []

        for r in z:
            rX.append(r[3])
        allD = []
        for s in rX:
            if s > 0:
                allD.append(s)

        print(thisState, "allDeaths", allDeaths)
        totalDeaths = allDeaths[-1]

        kL = []
        kM = diffL(allD)
        for px in range(len(newCases) + 15):
            kL.append(0)
        for py in range(len(newCases)):
            pZ = getNorm(6, 2, int(max(1, 0.05 * newCases[py])))
            # print (fixedState, "XXX", int(max(1,.04*newCases[py])), pZ) ;
            for pR in range(15):
                kL[py + pR] += pZ[pR]

        kF = len(newCases)
        thisPop = populations[thisState]
        diePC = 5 * totalDeaths / sum(kL[:kF])
        est = sum(dieEst(allD, newCases, diePC / 100)[:kF])
        actEstDiff = totalDeaths - est

        #########print (thisState, "admits", admits, z5[thisState]['04-12']['admits']) ;

        plt.plot(
            timesList(values=avgL(avgL(diffL(cases))), multiply_by=1), label="newCases"
        )
        # plt.plot(timesList(cases,.05), label = '5%cases') ;
        plt.plot(timesList(values=admits, multiply_by=0.4), label="40%inHosp")
        plt.plot(timesList(values=icu, multiply_by=1), label="icu")
        plt.plot(
            timesList(values=avgL(avgL(dayDeaths)), multiply_by=10), label="10xDeaths"
        )

        plt.title(
            thisState
            + "  "
            + str(cases[-1])[:-3]
            + ","
            + str(cases[-1])[-3:]
            + "  cases"
        )
        plt.legend()
        plt.xlabel("days")
        plt.ylabel("per day")
        plt.show()

        print(
            fixedState,
            "\t",
            totalCases,
            "cases",
            "\t",
            "1 in",
            int(thisPop / totalCases),
            "\t",
            doubleRate,
            "days to Double",
            "\t",
            round(diePC, 1),
            "% die",
            "\t",
            "actual",
            totalDeaths,
            "\t",
            "est",
            est,
            actEstDiff,
            "\t\t",
            "1 in",
            int(
                populations[thisState]
                / totalCases
                / (0.05 * totalDeaths / sum(kL[:kF]))
            ),
            round(
                100
                * sum(getTest(thisState, t6, t7, t8, t9, t10, t11, t12))
                / populations[thisState],
                2,
            ),
            getTest(thisState, t6, t7, t8, t9, t10, t11, t12),
        )
        print(fixedState, "XXX  kL", kL, len(kL), sum(kL))
        print(fixedState, "here recoveries", recov, sum(recov))
        # print (fixedState, "die/Case", round(100*rX[-1]/sum(newCases),2), "%" , "       newDie",  len(diffL(rX)),  diffL(rX)[-15:], sum(diffL(rX)) ) ;
    # print (fixedState, "XX die/NewCases", divideL(diffL(rX)[-20:],newCases[-20:]) ) ;


states.close()
records.close()
