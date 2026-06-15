import pytest
from src.utils import converter_data


@pytest.mark.parametrize(
    "texto,dia,mes,ano",
    [
        ("01/01/2026",1,1,2026),
        ("15/06/2026",15,6,2026),
        ("31/12/2026",31,12,2026)
    ]
)
def test_converter_data_parametrizado(
    texto,
    dia,
    mes,
    ano
):
    data = converter_data(texto)

    assert data.day == dia
    assert data.month == mes
    assert data.year == ano