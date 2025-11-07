# shakki-ai
Shakin tekoälyprojekti

## Dokumentit
- [Määrittelydokumentti](docs/maarittelydokumentti.md)


## Rajaukset
Ensimmäisessä versiossa ei tueta
- tornitusta
- ohestalyöntiä
- korotusta
Nämä lisätään myöhemmin, kun peruslogiikka ja tekoäly saadaan alkuun.


## Miten ajetaan?
Poetry asennettuna:
1) Asennus: poetry install
2) Käynnistys (Tekstikäyttöliittymä): poetry run python -m shakki_ai.cli
3) Testit: Poetry run pytest -q


## Tunnetut puutteet
- Siirtogeneraattori ei vielä kata kaikkia nappuloita ja sääntöjä
- Heuristiikka perustuu aluksi vain materiaalin määrään, sijoittumiset lisätään myöhemmin
- Ei aikarajallista hakua tei iteratiivista syvenemistä vielä
