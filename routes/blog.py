from fastapi import APIRouter
from controllers.blog import get_allBlogs,create_blog,delete_blog,update_blog
from schemas.blog import BlogResponse
router =APIRouter()

router.get("/all-blogs")(get_allBlogs)
router.post("/create-blog",response_model=BlogResponse)(create_blog)
router.delete("/delete-blog/{blog_id}")(delete_blog)
router.put("/update-blog/{blog_id}")(update_blog)

