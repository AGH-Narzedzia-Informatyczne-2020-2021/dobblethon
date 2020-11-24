
import speech_recognition as sr

# Tuples with names of thing and number on card
L1 = (1, "słońce", "słoneczko")
L2 = (2, "lampa", "lampka")
L3 = (3, "kropla")
L4 = (4, "nuta")
L5 = (5, "kot", "kotek")
L6 = (6, "gwiazda", "gwiazdka")
L7 = (7, "arbuz")
L8 = (8, "wiśnie", "wiśnia", "czereśnie", "czereśnia")
L9 = (9, "księżyc")
L10 = (10, "piłka")
L11 = (11, "komputer")
L12 = (12, "butelka")
L13 = (13, "oko")
L14 = (14, "piorun")
L15 = (15, "chmura", "chmurka")
L16 = (16, "ser")
L17 = (17, "kwiat", "kwiatek")
L18 = (18, "kaktus")
L19 = (19, "piórnik")
L20 = (20, "słoń")
L21 = (21, "serce", "serduszko")
L22 = (22, "zegar", "zegarek")
L23 = (23, "pudełko", "pudło", "pudełeczko")
L24 = (24, "kubek")
L0 = (0, "książka", "księga")


lst_tuple = [L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11,
                 L12, L13, L14, L15, L16, L17, L18, L19, L20,
                 L21, L22, L23, L24]
# print(lst_tuple)
r = sr.Recognizer()

with sr.Microphone() as source: #voice recognizer
    print('Mów :')
    audio = r.listen(source)
text1=""
try:
    text1 = r.recognize_google(audio, None, "pl-PL")
    print("Powiedziałeś : {}". format(text1))

except:
    print("Nie zrozumiałem")

for x in range(25):
    if text1 in lst_tuple[x]:
        print(x)
    # k = lst_tuple[x][-1]
    # for y in range(1, k + 1):
    #     if(lst_tuple[x][y] is text1):
    #         result = 1
    #     else:
    #         result = 0