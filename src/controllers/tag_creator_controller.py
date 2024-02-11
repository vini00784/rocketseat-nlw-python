from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
        Responsible for implementing business rules
    '''
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_barcode(product_code)
        return self.__format_response(path_from_tag)

    def __create_barcode(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)

        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }