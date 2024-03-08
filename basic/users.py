from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users'],
    responses={
        200: {'msg': 'Success get users data'},
        404: {'msg': '404 Not Found'}
    }
)

@router.get('/{user_id}')
def get_user(user_id: int):
    return {"message": f"{user_id}번 유저데이터"}