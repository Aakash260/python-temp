from fastapi import APIRouter
from controllers.user import user_root

router =APIRouter()

router.get("")(user_root)

