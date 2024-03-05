def count_letters(string):
    stats = {}
    for c in string:
        if c in stats:
            stats[c] += 1
        else:
            stats[c] = 1
    return stats

txt = """
W Pacanowie kozy kują
więc Koziołek, mądra głowa,
błąka się po całym świecie,
aby dojść do Pacanowa.
Właśnie nową zaczął podróż,
by ją skończyć w Pacanowie.
A co przeżył i co widział
ten artykuł wszystko wam opowie
"""
print(count_letters(txt))
