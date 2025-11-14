import os
import httpx
import pytest
from dotenv import load_dotenv

@pytest.fixture
def client():
    load_dotenv("config/.env.qa")
    api_base_url = os.environ.get("BASE_URL")
    print("api_base_url", api_base_url)
    return httpx.AsyncClient(base_url=api_base_url)

async def send_request(request, url, request_type, payload=''):
    send_api_request = request.getfixturevalue("client")

    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': f'Bearer {auth_token}'
    }

    match request_type.lower():
        case 'get':
            response = await send_api_request.get(url, headers=headers)
            return response
        case 'post':
            response = await send_api_request.post(url, json=payload, headers=headers) if payload != '' else await send_api_request.post(url, headers=headers)
            return response
        case 'put':
            response = await send_api_request.put(url, json=payload, headers=headers) if payload != '' else await send_api_request.put(url, headers=headers)
            return response
        case 'delete':
            response = await send_api_request.delete(url, headers=headers)
            return response
        case _:
            raise ValueError("Invalid request type. Use 'get', 'post', 'put', or 'delete'.")
