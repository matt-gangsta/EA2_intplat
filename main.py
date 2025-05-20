import httpx
from fastapi import FastAPI, Depends, HTTPException, status, Header, Path

app = FastAPI()
EXTERNAL_API_URL = "https://ea2p2assets-production.up.railway.app/"

@app.get("/catalogo_productos")
def obtener_productos(x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(EXTERNAL_API_URL + "data/articulos", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@app.get("/catalogo_productos/{producto_id}")
def obtener_productos(
    producto_id: str = Path(..., description="ID del producto"),
    x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(f"{EXTERNAL_API_URL}data/articulos/{producto_id}", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@app.get("/sucursales")
def obtener_sucursales(x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(EXTERNAL_API_URL + "data/sucursales", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@app.get("/sucursales/{sucursal_id}")
def obtener_sucursal(
    sucursal_id: str = Path(..., description="ID de la sucursal"),
    x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(f"{EXTERNAL_API_URL}data/sucursales/{sucursal_id}", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@app.get("/vendedores")
def obtener_sucursales(x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(EXTERNAL_API_URL + "data/vendedores", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

@app.get("/vendedores/{vendedor_id}")
def obtener_sucursal(
    vendedor_id: str = Path(..., description="ID del vendedor"),
    x_authentication: str = Header(...)):
    headers = {"x-authentication": x_authentication}
    
    try:
        response = httpx.get(f"{EXTERNAL_API_URL}data/vendedores/{vendedor_id}", headers=headers)
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la API externa: {str(e)}")
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()
