from fastapi import APIRouter, HTTPException
from typing import List, Dict
from models.external_data_model import Post
from services.external_api_service import fetch_posts, fetch_post_by_id

router = APIRouter()

@router.get("/external-data", response_model=List[Post])
def get_external_data():
    """Fetches all posts from the external API.

    Returns:
        List[Post]: A list of posts retrieved from the external API.
    
    Raises:
        HTTPException: If there is an error fetching the posts.
    """
    posts = fetch_posts()
    if not posts:
        raise HTTPException(status_code=500, detail="Error to fetch posts")
    return posts


@router.post("/external-data/filter", response_model=List[Post])
def filter_external_data(user_id: int = None):
    """Filters posts by user ID.

    Args:
        user_id (int, optional): The ID of the user whose posts should be retrieved.

    Returns:
        List[Post]: A list of filtered posts based on the user ID.
    """
    posts = fetch_posts()
    if user_id is not None:
        posts = [post for post in posts if post["userId"] == user_id]
    return posts


@router.get("/external-data/sorted", response_model=List[Post])
def get_sorted_posts():
    """Fetches and returns posts sorted alphabetically by title.

    Returns:
        List[Post]: A list of posts sorted by title.
    """
    posts = fetch_posts()
    sorted_posts = sorted([Post(**post) for post in posts], key=lambda post: post.title)
    return sorted_posts


@router.get("/external-data/user-post-count", response_model=Dict[int, int])
def get_posts_count_per_user():
    """Counts the number of posts per user.

    Returns:
        Dict[int, int]: A dictionary where keys are user IDs and values are the number of posts.
    """
    posts = fetch_posts()
    post_count = {}
    for post in posts:
        user_id = post["userId"]
        post_count[user_id] = post_count.get(user_id, 0) + 1
    return post_count


@router.get("/external-data/search", response_model=List[Post])
def search_posts_by_title(keyword: str):
    """Searches for posts that contain a specific keyword in their title.

    Args:
        keyword (str): The keyword to search for in post titles.

    Returns:
        List[Post]: A list of posts that contain the keyword in their title.
    
    Raises:
        HTTPException: If no posts are found with the given keyword.
    """
    posts = fetch_posts()
    filtered_posts = [post for post in posts if keyword.lower() in post["title"].lower()]
    if not filtered_posts:
        raise HTTPException(status_code=404, detail="Don't found any post with that keyword")
    return filtered_posts


@router.get("/external-data/{post_id}", response_model=Post)
def get_post_by_id(post_id: int):
    """Fetches a specific post by its ID.

    Args:
        post_id (int): The ID of the post to retrieve.

    Returns:
        Post: The post corresponding to the given ID.
    
    Raises:
        HTTPException: If the post is not found.
    """
    post = fetch_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
