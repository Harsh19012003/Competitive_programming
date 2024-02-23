def convert_hms(s):
    hours = int(s/(60*60))

    remaining_secs = s - (hours*60*60)

    mins = int(remaining_secs/60)

    secs = remaining_secs - (mins*60)

    return (hours, mins, secs)


h, m, s = convert_hms(500000)

print(h, m, s)