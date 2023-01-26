import random
def szamol():
    szam=random.randint(1,50)
    print("I/A:")

    if szam%5==0:
        print("\n\tA szám öttel osztható")
    elif szam%3==0:
        print("\n\tA szám hárommal osztható")
    elif szam%5==0 and szam%3==0:
        print("\n\tA szám öttel és hárommal is osztható")

