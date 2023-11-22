from fastapi import HTTPException


class ValidationError:
    @staticmethod
    def entity_validation(entity, error_message: str):
        if not entity:
            raise HTTPException(status_code=404, detail=error_message)

    @staticmethod
    def check_input_data(*args):
        for arg in args:
            if not arg:
                raise HTTPException(status_code=400, detail="Bad request")
