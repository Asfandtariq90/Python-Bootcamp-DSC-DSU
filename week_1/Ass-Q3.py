import time

song = """  Pal bhar thaher jao,
Dil ye sambhal jaaye,
Kaise tumhe roka karu,

Meri taraf aata,
Har gham phisal jaaye,
Ankhon mein tumko bharun,

Bin bole baatein tumse karoon,
Agar tum saath ho,
Agar tum saath ho,

Behti rehti..,
Nehar nadiya si,
Teri duniya mein, meri duniya hai,
Teri chahaton mein, main dhal jaati hun,
Teri aadaton mein,
Agar tum saath ho,

Teri nazron me hai tere sapne,
Tere sapno me hai naraazi,
Mujhe lagta hain ke baatein dil ki,
Hoti lafzon ki dhokebaazi,

Tum saath ho ya na ho,
Kya fark hai,
Bedard thi zindagi bedard hai,
Agar tum saath ho,
Agar tum saath ho,

Palke jhapakte hi,
Din ye nikal jaaye,
Bethi bethi bhaagi phiroon,

Meri taraf aata,
Har gham phisal jaaye,
Aankhon mein tumko bharun,

Bin bole baatein tumse karoon,
Agar tum saath ho,
Agar tum saath ho,
    """
x = song.split(",")

for elements in x:
    time.sleep(1.2)
    print(elements)
