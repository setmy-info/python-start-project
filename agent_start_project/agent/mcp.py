import requests


def load_mcp(url: str):
    """
    Load MCP JSON from API.
    """
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        mcp_json = resp.json()
        print(f"MCP JSON loaded: service={mcp_json.get('serviceName')}")
        return mcp_json
    except requests.RequestException as e:
        print(f"MCP request fail: {e}")
        return None
