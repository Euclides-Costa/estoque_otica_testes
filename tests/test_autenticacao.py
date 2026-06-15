from unittest.mock import Mock, patch
from src.autenticacao import Usuario


@patch("src.autenticacao.Banco")
def test_login_sucesso_mock(
    banco_mock
):

    cursor_mock = Mock()

    cursor_mock.fetchone.return_value = (
        "$2b$12$SzT7V1eKq0u7rKqj6f3v3uF2X6QqY5VdQ6jv5S3aK7vT6xR0mT3dW",
    )

    banco_mock.return_value.cursor = cursor_mock

    usuario = Usuario()

    with patch(
        "bcrypt.checkpw",
        return_value=True
    ):
        assert usuario.login(
            "admin",
            "123"
        ) is True