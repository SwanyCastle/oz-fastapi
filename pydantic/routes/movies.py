from fastapi import APIRouter, HTTPException
from models.movie import Movie, CreateMovie, SearchMovie
from typing import Optional, List
from uuid import uuid4, UUID

router = APIRouter()

movie_db: List[Movie] = []

@router.get("/search", response_model=SearchMovie)
def get_movie(keyword: Optional[str] = None, max_results: int = 10 ) -> SearchMovie:
    result = [movie for movie in movie_db if keyword.lower() in movie.name.lower()] if keyword else movie_db
    return SearchMovie(results=result[:max_results])

@router.post("/")
def create_movie(movie_data: CreateMovie) -> Movie:
    # model_dump() 라는 함수가 django 의 serializer 역할을 해준다.
    movie = Movie(id=uuid4(), **movie_data.model_dump())
    movie_db.append(movie)
    return movie

@router.put("/{movie_id}")
def update_movie(movie_id: UUID, update_data: CreateMovie) -> Movie:
    # update_movie = update_data.model_dump()
    # print(update_data)
    # for movie in movie_db:
    #     if movie.id == movie_id:
    #         movie = update_movie
    # return update_movie
    movie = next((movie for movie in movie_db if movie.id == movie_id), None)
    if movie:
        movie.name = update_data.name
        movie.plot = update_data.plot
        movie.genres = update_data.genres
        movie.casts = update_data.casts
        return movie
    return HTTPException(status_code=404)

@router.delete("/{movie_id}")
def update_movie(movie_id: UUID) -> Movie:
    del_movie = next((movie for movie in movie_db if movie.id == movie_id), None)
    if del_movie:
        del_movie = movie_db.pop(movie_db.index(del_movie))
        return del_movie
    return HTTPException(status_code=404)

# {
#     "name": "Star Wars: Episode IX - The Rise of Skywalker",
#     "plot": "The surviving members of the resistance face the First Order once again.",
#     "genres": ["Action", "Adventure", "Fantasy"],
#     "casts": ["Daisy Ridley", "Adam Driver"]
# }
# {
#     "name": "파묘",
#     "plot": "미국 LA, 거액의 의뢰를 받은 무당 ‘화림’(김고은)과 ‘봉길’(이도현)은 기이한 병이 대물림되는 집안의 장손을 만난다. 조상의 묫자리가 화근임을 알아챈 ‘화림’은 이장을 권하고, 돈 냄새를 맡은 최고의 풍수사 ‘상덕’(최민식)과 장의사 ‘영근’(유해진)이 합류한다. “전부 잘 알 거야… 묘 하나 잘못 건들면 어떻게 되는지” 절대 사람이 묻힐 수 없는 악지에 자리한 기이한 묘. ‘상덕’은 불길한 기운을 느끼고 제안을 거절하지만, ‘화림’의 설득으로 결국 파묘가 시작되고… 나와서는 안될 것이 나왔다.",
#     "genres": ["호러", "스릴러", "오컬트"],
#     "casts": ["최민식", "유해진", "김고은"]
# }
# {
#     "name": "서울의봄",
#     "plot": "1979년 12월 12일, 수도 서울 군사반란 발생 그날, 대한민국의 운명이 바뀌었다 대한민국을 뒤흔든 10월 26일 이후, 서울에 새로운 바람이 불어온 것도 잠시 12월 12일, 보안사령관 전두광이 반란을 일으키고 군 내 사조직을 총동원하여 최전선의 전방부대까지 서울로 불러들인다. 권력에 눈이 먼 전두광의 반란군과 이에 맞선 수도경비사령관 이태신을 비롯한 진압군 사이, 일촉즉발의 9시간이 흘러가는데… 목숨을 건 두 세력의 팽팽한 대립 오늘 밤, 대한민국 수도에서 가장 치열한 전쟁이 펼쳐진다!",
#     "genres": ["전쟁", "역사"],
#     "casts": ["황정민", "정우성", "정해인"]
# }