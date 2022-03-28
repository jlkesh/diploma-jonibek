from fastapi import APIRouter

router = APIRouter(tags=['Users Router'], prefix="/users")


@router.post("/")
def create():
    pass


@router.get("/")
def get_all():
    pass


@router.get("/{id}")
def get(id: int):
    pass



@router.put("/{id}")
def update(id: int):
    pass


@router.delete("/{id}")
def delete(id: int):
    pass







