# The aim is to change the string as follows.

# before: "data science and machine learning bootcamp"
# after: "DaTa sCiEnCe aNd mAcHiNe lEaRnInG BoOtCaMp"

def app(sent):
    string = ""
    for index in range(len(sent)):
        if index % 2 == 0:
            string += sent[index].upper()
        else:
            string += sent[index].lower()
    print(string)
app("data science and machine learning bootcamp")
