from fastapi import APIRouter


# item 관련 API 호출
router = APIRouter()

@router.get( 
        '/api/v1/items/{item_id}',
        status_code=200,
        # swagger-ui 에서 태그 설정
        tags=['items', 'payment'],
        # swagger-ui 에서 보여주는거
        summary='특정 아이템 가져오기',
        description='Item 모델의 item_id 값을 가지고 하나의 item 데이터 정보를 가져옵니다.',
        response_description='item 세부 정보 반환'
)
def get_item(item_id: int) -> dict:
    return {"items": "item"}

