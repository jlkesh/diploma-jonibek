from fastapi import APIRouter

router = APIRouter(tags=['Picture Router'], prefix="/pictures")


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
def get(id: int):
    pass


@router.delete("/{id}")
def get(id: int):
    pass







