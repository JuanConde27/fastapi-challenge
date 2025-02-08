import requests
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")

def fetch_posts() -> List[Dict]:
    """Fetches all posts from the external API.

    Returns:
        List[Dict]: A list of posts, where each post is represented as a dictionary.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    try:
        response = requests.get(f"{EXTERNAL_API_URL}/posts")
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error to fetch posts: {e}")
        return []


def fetch_post_by_id(post_id: int) -> Dict:
    """Fetches a specific post by its ID from the external API.

    Args:
        post_id (int): The unique identifier of the post.

    Returns:
        Dict: A dictionary representing the post, or an empty dictionary if not found.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the request.
    """
    try:
        response = requests.get(f"{EXTERNAL_API_URL}/posts/{post_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error to fetch post by ID: {e}")
        return {}
