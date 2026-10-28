from pprint import pp
import paikat

nimet = ['sisapiha', 'teiskontien-aula', 'palvelukatu', 'tietotalon-aula', 'juhlasali', 'kuntokadun-aula']

lista = paikat.lue_paikat(nimet)
pp(lista)
