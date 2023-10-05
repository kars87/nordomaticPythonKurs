print("Velkommen til Nordomatic sitt kule tekstspill!!!")


playerName = str(input("Hva heter du? :"))
startSpill = str(input(f"Hei {playerName} er du klar for å spille? :"))

if startSpill == "ja":
    baneValg = str(input("Hvilken bane vil spille på? ørken eller jungel?"))
else:
    print("Det var synd, du suger!")
    quit()
if baneValg == "ørken":
    desert = str(input("Trist valg, han som skal hjelpe deg er død, vil du gå eller kjøre?"))