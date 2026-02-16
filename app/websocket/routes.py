# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from .manager import manager

# router = APIRouter()

# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await manager.connect(websocket)

#     try:
#         while True:
#             message = await websocket.receive_text()
#             await manager.broadcast(f"Message: {message}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)


from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from uuid import UUID
from app import auth
from .manager import manager

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    # Get token from query params
    token = websocket.query_params.get("token")

    if not token:
        await websocket.close()
        return

    payload = auth.verify_token(token)

    if not payload:
        await websocket.close()
        return

    user_id = UUID(payload["sub"])

    await manager.connect(user_id, websocket)

    try:
        while True:
            data = await websocket.receive_json()

            # expected:
            # {
            #   "to_user_id": "...",
            #   "message": "Hello"
            # }

            to_user_id = UUID(data["to_user_id"])
            message = data["message"]

            await manager.send_personal_message(
                to_user_id,
                f"Message from {user_id}: {message}"
            )

    except WebSocketDisconnect:
        manager.disconnect(user_id)
