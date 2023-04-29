class AqsiFunctions:
    def __init__(self):
        ...
        
    @classmethod
    def body_filter(self, pre_body: dict):
        try:
            body = {key: value for key, value in pre_body.items() if
                    value is not None}
        except Exception as e:
            body = {}
            raise e
        finally:
            return body