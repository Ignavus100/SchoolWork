dictionary = {
    "a":"e",
    "b":"h",
    "c":"",
    "d":"",
    "e":"",
    "f":"t",
    "g":"",
    "h":"",
    "i":"",
    "j":"",
    "k":"",
    "l":"",
    "m":"",
    "n":"",
    "o":"",
    "p":"",
    "q":"",
    "r":"",
    "s":"",
    "t":"",
    "u":"",
    "v":"",
    "w":"",
    "x":"",
    "y":"",
    "z":"",
}
newtext = ""
cyphertext = "FBALLQUQMNLQUQSLQUQKWQWMOFBQUANKIQDIQUALKRGKRALYOWARQWQVQIC QDRUAQFQDKUQLZYQDRAQDIOLFONAWWKDIAVNABKWVQDKIFKUAWQLFBMOSBAQ NLYGNKFANWIMUVQNARLLQUQWFMWBAAVFBAKNWKUKLQNKFYFMFBAIQUALGQW WMMDNAIMSDKHARFBAYGANAKDILORARKDFBASADOWIQUALOWQLMDSGKFBQLVQI QKDFBAWYWFAUQDQFONQAMJLKDDQAOWWMUAMDAADINYVFKDSQUAWWQSAIQDU QCARAINYVFKMDUMNARKJJKIOLFZYIBMMWKDSODOWOQLGMNRWQDRNAUMXKDS VODIFOQFKMDQDRFBAWVQIKDSZAFGAADGMNRWWAAKJYMOIQDGMNCMOFFBAUAF BMROWARJMNADINYVFKDSFBKWUAWWQSAFBKDCQZMOFWAEOADIAWKJYMOSAFW FOIC".lower()
for i in cyphertext:
    try:
        if dictionary[i] in "qwertyuiopasdfghjklzxcvbnm":
            newtext += dictionary[i]
        else:
            newtext += "_"
    except:
        newtext += i

print(newtext)