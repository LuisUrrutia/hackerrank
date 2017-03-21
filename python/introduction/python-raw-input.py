def read():
    s = raw_input()
    s = s.strip()
    if len(s) >= 1 and len(s) <= 500:
        return s
