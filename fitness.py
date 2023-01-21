# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat

# Kysytään käyttäjältä tiedot
pituus_teksti = input('Kuinka pitkä olet (cm): ')
paino_teksti = input('Kuinka paljon painat (kg): ')
ika_teksti = input('Kuinka vanha olet: ')
sukupuoli_teksti = input('Sukupuoli mies vastaa 1, nainen 0: ')

# Muutetaan vastaukset liukuluvuiksi
pituus = float(pituus_teksti)
paino = float(paino_teksti)
ika = float(ika_teksti)
sukupuoli = float(sukupuoli_teksti)


# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino float: paino (kg)
        pituus float: pituus (cm)

    Returns:
        float: painoindenksin desimaalin tarkkuudella 
    """
    pituus = pituus / 100  # muutetaan pituus metreiksi
    bmi = paino / pituus ** 2
    bmi = round(bmi, 1)
    return bmi


def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilöni ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosenttti (aikuinen)
    """
    rasvaprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5
    rasvaprosentti = round(rasvaprosentti)
    return rasvaprosentti

def lapsen_rasvaprosentti(bmi, ika, sukupuoli) :
    """_summary_

    Args:
        bmi float: painoindeksi
        ika float: ikä
        sukupuoli float: poika -> 1, tyttö -> 0

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    return rasvaprosentti


oma_bmi = laske_bmi(paino, pituus)
oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print('Painoindeksisi on', oma_bmi,
      'ja kehon rasvaprosentti on', oma_rasvaprosentti)
