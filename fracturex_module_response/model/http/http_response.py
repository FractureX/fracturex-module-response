from pydantic import (
    BaseModel,
    PositiveInt
)
from typing import (
    Dict,
    List,
    Any
)

class __Base_Http_Response(BaseModel):
    status_code: PositiveInt
    success : bool
    message : str

class HTTP_Response(__Base_Http_Response):
    data : Dict[str, Any]

class HTTP_Responses(__Base_Http_Response):
    data : List[Dict[str, Any]]
