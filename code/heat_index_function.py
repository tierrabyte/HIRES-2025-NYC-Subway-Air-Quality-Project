def calculate_heat_index(temp_f, rh):
    c1 = -42.379; c2 = 2.04901523; c3 = 10.14333127
    c4 = -0.22475541; c5 = -6.83783e-3; c6 = -5.481717e-2
    c7 = 1.22874e-3; c8 = 8.5282e-4; c9 = -1.99e-6
    hi = (c1 + c2 * temp_f + c3 * rh + c4 * temp_f * rh +
          c5 * temp_f**2 + c6 * rh**2 + c7 * temp_f**2 * rh +
          c8 * temp_f * rh**2 + c9 * temp_f**2 * rh**2)
    if rh < 13 and 80 <= temp_f <= 112:
        hi -= ((13 - rh) / 4) * ((17 - abs(temp_f - 95)) / 17)**0.5
    elif rh > 85 and 80 <= temp_f <= 87:
        hi += ((rh - 85) / 10) * ((87 - temp_f) / 5)
    if hi < 80:
        hi = 0.5 * (temp_f + 61 + ((temp_f - 68) * 1.2) + (rh * 0.094))
    return hi
