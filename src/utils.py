from datetime import datetime

def converter_data(data_texto):
    return datetime.strptime(
        data_texto,
        "%d/%m/%Y"
    ).date()