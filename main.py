from pyodide.http import pyfetch
from pyscript import document, when

nimet = [
    'sisapiha',
    'teiskontien-aula',
    'palvelukatu',
    'tietotalon-aula',
    'juhlasali',
    'kuntokadun-aula'
]

async def lue_paikat(nimet):
    paikkalista = {}
    for nimi in nimet:
        response = await pyfetch(f"./{nimi}.json")
        if response.ok:
            paikkalista[nimi] = await response.json()
        else:
            paikkalista[nimi] = {"virhe": f"Tiedostoa ei löytynyt: {nimi}.json"}
    return paikkalista

@when("click", "#lataa")
async def lataa_paikat(event):
    data = await lue_paikat(nimet)
    document.querySelector("#tulos").innerText = str(data)
    
