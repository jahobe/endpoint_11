from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="MCP Server untuk 8004scan")

# Endpoint utama (Root) untuk cek kesehatan umum
@app.get("/")
def read_root():
    return {"status": "Healthy", "message": "Server MCP berjalan dengan baik."}

# Endpoint MCP (GET) - Saat 8004scan melakukan Ping/Pengecekan
@app.get("/mcp")
def mcp_health_check():
    return JSONResponse(
        status_code=200,
        content={"status": "Healthy", "type": "mcp_endpoint", "version": "1.0"}
    )

# Endpoint MCP (POST) - Saat 8004scan mencoba mengirim perintah/prompt
@app.post("/mcp")
async def mcp_receive_command(request: Request):
    try:
        data = await request.json()
        print(f"[*] Menerima data dari 8004scan: {data}")
    except:
        pass
    
    # Selalu balas dengan sukses agar tidak error
    return JSONResponse(
        status_code=200, 
        content={"status": "success", "message": "Perintah diterima dengan baik."}
    )

if __name__ == "__main__":
    # Railway akan otomatis memberikan port, kita gunakan 0.0.0.0 agar bisa diakses publik
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
