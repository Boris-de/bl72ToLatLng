import math


# algorithms adapted from http://zoologie.umh.ac.be/tc/algorithms.aspx
# noinspection PyPep8Naming
def bl72_to_latlng(x, y):
    LongRef = 0.076042943
    nLamb = 0.7716421928
    aCarre = pow(6378388, 2)
    bLamb = 6378388 * (1 - (1 / 297))
    eCarre = (aCarre - pow(bLamb, 2)) / aCarre
    KLamb = 11565915.812935
    eLamb = math.sqrt(eCarre)
    Tan1 = (x - 150000.01256) / (5400088.4378 - y)
    Lambda = LongRef + (1 / nLamb) * (0.000142043 + math.atan(Tan1))
    RLamb = math.sqrt(pow((x - 150000.01256), 2) + pow((5400088.4378 - y), 2))
    TanZDemi = pow((RLamb / KLamb), (1 / nLamb))
    Lati1 = 2 * math.atan(TanZDemi)
    Haut = 0

    while True:
        eSin = eLamb * math.sin(Lati1)
        Mult1 = 1 - eSin
        Mult2 = 1 + eSin
        Mult = pow((Mult1 / Mult2), (eLamb / 2))
        LatiN = (math.pi / 2) - (2 * (math.atan(TanZDemi * Mult)))
        Diff = LatiN - Lati1
        Lati1 = LatiN
        if abs(Diff) <= 0.0000000277777:
            break

    lat = (LatiN * 180) / math.pi
    lng = (Lambda * 180) / math.pi

    Lat = (math.pi / 180) * lat
    Lng = (math.pi / 180) * lng

    SinLat = math.sin(Lat)
    SinLng = math.sin(Lng)
    CoSinLat = math.cos(Lat)
    CoSinLng = math.cos(Lng)

    dx = -125.8
    dy = 79.9
    dz = -100.5
    da = -251.0
    df = -0.000014192702

    LWf = 1 / 297
    LWa = 6378388
    LWe2 = (2 * LWf) - (LWf * LWf)
    Adb = 1 / (1 - LWf)

    Rn = LWa / math.sqrt(1 - LWe2 * SinLat * SinLat)
    Rm = LWa * (1 - LWe2) / pow((1 - LWe2 * Lat * Lat), 1.5)

    DLat = -dx * SinLat * CoSinLng - dy * SinLat * SinLng + dz * CoSinLat
    DLat = DLat + da * (Rn * LWe2 * SinLat * CoSinLat) / LWa
    DLat = DLat + df * (Rm * Adb + Rn / Adb) * SinLat * CoSinLat
    DLat = DLat / (Rm + Haut)

    DLng = (-dx * SinLng + dy * CoSinLng) / ((Rn + Haut) * CoSinLat)

    LatWGS84 = ((Lat + DLat) * 180) / math.pi
    LngWGS84 = ((Lng + DLng) * 180) / math.pi

    return {
        "latitude": LatWGS84,
        "longitude": LngWGS84
    }
