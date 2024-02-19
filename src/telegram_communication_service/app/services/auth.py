from typing import Set
from telegram import Update

allowed_user_ids: Set[int] = set()
allowed_user_ids.add(413074613)     # Albert


async def validate_user_id(user_id: int) -> bool:
    if user_id in allowed_user_ids:
        return True

    return False


async def auth_update(update: Update) -> bool:
    is_user_valid = await validate_user_id(update.effective_user.id)
    if is_user_valid:
        return True
    else:
        return False
