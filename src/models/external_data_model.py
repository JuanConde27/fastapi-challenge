from pydantic import BaseModel

class Post(BaseModel):
    """Represents a post retrieved from the external API.

    Attributes:
        userId (int): The ID of the user who created the post.
        id (int): The unique identifier of the post.
        title (str): The title of the post.
        body (str): The content of the post.
    """
    
    userId: int
    id: int
    title: str
    body: str
