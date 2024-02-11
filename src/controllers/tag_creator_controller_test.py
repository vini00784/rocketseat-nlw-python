from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

# Para não gerar o barcode de fato, abaixo eu crio um "espelho" da função create_barcode, fazendo
# ele retornar de forma mockada o valor que precisamos

# Ou seja, ele mocka um retorno para a função, sem acessar ela diretamente

@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'
