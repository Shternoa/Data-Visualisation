from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Возвращает код страны состоящий из 2-х букв"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Если у страны нет кода
    return None


# print(get_country_code('Ukraine'))
# print(get_country_code('Russian Federation'))
# print(get_country_code('Japan'))
