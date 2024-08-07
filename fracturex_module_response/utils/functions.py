from typing import (
    Union, 
    Dict,
    List,
    Any
)
from fastapi.responses import JSONResponse

def get_json_response(status_code : int, success : bool, message : str, data : Union[Dict[str, Any], List], headers : Dict[str, str] = None) -> JSONResponse:
    """
    Método para retornar una respuesta en formato JSON
    
    Parameters
    ----------
    status_code : int
        Código de respuesta HTTP que devolverá la respuesta
    
    success : bool
        Indicativo de si la respuesta fue exitosa
    
    message : str
        Mensaje que devolverá en caso de que la respuesta no sea exitosa
    
    data : Union[Dict[str, Any], List]
        Información que devolverá
    
    headers : Dict[str, str] = None
        Pármetros de cabecera de la solicitud de retorno
    
    Returns
    -------
    fastapi.responses.JSONResponse Con la información suministrada
    """
    return JSONResponse(
        headers=headers,
        status_code=status_code,
        content={
            "success": success,
            "message": message if not success else "", 
            "data": data
        }
    )

def get_data_not_found(data_name : str) -> str:
    """
    Método para retornar un mensaje genérico para cuando una información no es encontrada
    
    Parameters
    ----------
    data_name : str
        Nombre del dato no encontrado
    
    Returns
    -------
    Valor data_name no encontrado
    """
    return f"Valor {data_name} no encontrado"

def get_data_already_exists(data_name : str) -> str:
    """
    Método para retornar un mensaje genérico para cuando una información ya existe
    
    Parameters
    ----------
    data_name : str
        Nombre del dato existente
    
    Returns
    -------
    Valor data_name ya existente
    """
    return f"Valor '{data_name}' ya existente"
