from pydantic import BaseModel
from typing import List, Dict

class Usuario(BaseModel):
    nombre: str
    rol: str
    contrasena: str