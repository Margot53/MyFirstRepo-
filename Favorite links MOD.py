import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=nW82fRNJc84", "https://www.youtube.com/watch?v=ZeIr0FVJwGs"]


music = ["https://www.spotify.com/us/premium/?utm_source=us-en_brand_contextual_text&utm_medium=paidsearch&utm_campaign=alwayson_ucanz_us_performancemarketing_core_brand+contextual+text+exact+us-en+google&gclid=CPHL-a60t9kCFcrBswodwlMEfA&gclsrc=ds","https://www.youtube.com/watch?v=3tmd-ClpJxA"]



answer = pg.prompt (
"""
Which would you like to do?
a) Watch videos
b) Listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.open(i)
