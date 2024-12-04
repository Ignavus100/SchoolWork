alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
reverse = "zyxwvutsrqponmlkjihgfedcba"
reverse = list(reverse)
substring = "Dvoo wlmv, blf'ev hloevw xrksvi xszoovmtv mfnyvi gdl. Gsrh gbkv lu xrksvi rh z hkvxrzo hfyhgrgfgrlm xrksvi pmldm zh Zgyzhs, zmw rh nzwv yb ivevihrmt gsv zokszyvg zmw ivkozxrmt gsv ozhg ovggvi drgs gsv urihg, gsv kvmfogrnzgv ovggvi drgs gsv hvxlmw, zmw hl lm. Rg rh xzoovw Zgyzhs yvxzfhv rg dzh lirtrmzoob wlmv drgs gsv Svyivd zokszyvg, zmw rg gllp rgh mznv uiln gsv urihg zmw ozhg, zmw hvxlmw zmw kvmfogrnzgv ovggvih rm gszg zokszyvg. Hfyhgrgfgrlm xrksvih ivkozxv gsv ovggvih lu gsv nvhhztv drgs lgsvi ovggvih. Xzvhzi hsrug zmw Zgyzhs ziv uzriob hrnkov hfyhgrgfgrlm xrksvih gl xizxp, yvxzfhv lmxv blf'ev nzwv z uvd tfvhhvh rg'h vzhb gl hklg gsv hbhgvn gszg szh yvvm fhvw gl wvxrwv lm gsv hfyhgrgfgrlmh. Gsv mvcg nvhhztv dlm'g yv jfrgv hl vzhb gl xizxp, hl ivnvnyvi gl ollp uli kfmxgfzgrlm, hrmtov ovggvih zmw hslig dliwh. Urmzoob, gsv pvbdliw gl zxxvhh gsv gsriw xszoovmtv rh gvzxzpv."
substring = substring.lower()
new = ""
for i in substring:
    try:
        new += (reverse[alphabet.index(i)])
    except:
        new += " "

print(new)