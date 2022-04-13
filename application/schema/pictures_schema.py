from application.schema import GenericDto, Dto


class PictureCreateDTO(Dto):
    filename: str
    description: str

    class Config:
        orm_mode = True


class PictureDTO(GenericDto, PictureCreateDTO):
    pass
