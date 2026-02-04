screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")
try:
    screen_res[0]=1280
except TypeError:
    print("Tuples cannot be modified!")