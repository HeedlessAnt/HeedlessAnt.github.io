import json

def lue_paikat(nimet):
    paikkalista = {}
    for nimi in nimet:
        with open(f"{nimi}.json") as tiedosto:
            paikkalista[nimi] = json.load(tiedosto)
    return paikkalista
