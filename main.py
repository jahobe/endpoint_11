from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
import os

app = FastAPI(title="MasterDAO MCP Server")

# ==========================================
# 1. WEB UI SEDERHANA UNTUK HALAMAN DEPAN
# ==========================================
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MasterDAO | MCP Server</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #0B0E14; /* Warna latar gelap ala Web3 */
                color: #E2E8F0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #1E293B;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
                text-align: center;
                border: 1px solid #334155;
                max-width: 400px;
                width: 100%;
            }
            .logo {
                font-size: 3rem;
                margin-bottom: 10px;
            }
            h1 {
                color: #38BDF8;
                margin: 10px 0;
                font-size: 1.8rem;
            }
            .status-badge {
                display: inline-block;
                background-color: rgba(34, 197, 94, 0.2);
                color: #4ADE80;
                padding: 8px 16px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.9rem;
                margin-top: 15px;
                border: 1px solid rgba(34, 197, 94, 0.5);
            }
            .footer {
                margin-top: 25px;
                font-size: 0.8rem;
                color: #94A3B8;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="logo">🚀</div>
            <h1>MasterDAO</h1>
            <p>Model Context Protocol (MCP) Server</p>
            <div class="status-badge">
                🟢 SERVER ONLINE & HEALTHY
            </div>
            <div class="footer">
                Sistem aktif melayani agen ERC-8004 di jaringan Base.
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


# ==========================================
# 2. ENDPOINT RAHASIA UNTUK BOT 8004SCAN (TETAP JSON)
# ==========================================
@app.get("/mcp/{agent_id}")
def mcp_health_check(agent_id: str):
    print(f"[*] Ping diterima untuk agen: {agent_id}")
    return JSONResponse(
        status_code=200,
        content={
            "status": "Healthy", 
            "agent_name": agent_id,
            "message": f"Server siap melayani agen {agent_id}"
        }
    )

@app.post("/mcp/{agent_id}")
async def mcp_receive_command(agent_id: str, request: Request):
    try:
        data = await request.json()
        print(f"[*] Agen {agent_id} menerima data: {data}")
    except:
        pass
    
    return JSONResponse(
        status_code=200, 
        content={"status": "success", "agent_name": agent_id}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
