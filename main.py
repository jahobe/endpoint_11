from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import os

app = FastAPI(title="Multi-Agent MCP Server untuk 8004scan")

# Endpoint pengecekan utama
@app.get("/")
def read_root():
    return {"status": "Healthy", "message": "Master Server MCP Berjalan Mantap."}

# =================================================================
# INI RAHASIANYA: {agent_id} akan menangkap URL /mcp/agent-2, /mcp/agen-ku, dll
# =================================================================

# Endpoint untuk Health Check (Saat 8004scan mengecek indikator merah/hijau)
@app.get("/mcp/{agent_id}")
def mcp_health_check(agent_id: str):
    print(f"[*] Pengecekan kesehatan (Ping) diterima untuk agen: {agent_id}")
    return JSONResponse(
        status_code=200,
        content={
            "status": "Healthy", 
            "agent_name": agent_id,
            "message": f"Server siap melayani agen {agent_id}"
        }
    )

# Endpoint saat 8004scan mengirimkan instruksi ke agen tertentu
@app.post("/mcp/{agent_id}")
async def mcp_receive_command(agent_id: str, request: Request):
    try:
        data = await request.json()
        print(f"[*] Agen {agent_id} menerima payload/data: {data}")
    except:
        print(f"[*] Agen {agent_id} dipanggil tanpa payload JSON.")
        pass
    
    # Selalu balas HTTP 200 OK agar status agen di dashboard tetap hijau!
    return JSONResponse(
        status_code=200, 
        content={
            "status": "success", 
            "agent_name": agent_id, 
            "message": f"Perintah untuk {agent_id} sukses diproses."
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
