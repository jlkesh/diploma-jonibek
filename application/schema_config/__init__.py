from application.schema import Dto


class ArticleCreateConfig(Dto):
    class Config:
        schema_extra = {
            "example": {
                "title": "Russia's war has cost Ukraine $564.9bn so far - Ukraine",
                "short": """Russia's war on Ukraine has cost Ukraine $564.9bn (£429.3bn) so far in terms of damage to infrastructure""",
                "body": """Russian officials deny there is censorship in Russia. Only laws that need to be obeyed.In fact, under the country’s constitution, censorship is forbidden.""",
                "published": True
            }
        }
        orm_mode = True


class BookCreateConfig(Dto):
    class Config:
        schema_extra = {
            "example": {
                "name": "Boy ota va kambag'al ota",
                "author": """Robert Higasaki""",
                "short_info": """Russian officials deny there is censorship in Russia""",
                "page_count": 500,
                "file_id": 1
            }
        }
        orm_mode = True


class CommentCreateConfig(Dto):
    class Config:
        schema_extra = {
            "example":
                {
                    "message": "Very Nice"
                }
        }
        orm_mode = True


class LikeCreateConfig(Dto):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "is_like": True,
                "article_id": 1
            }
        }


class NewsCreateConfig(Dto):
    class Config:
        allow_reuse = False
        schema_extra = {
            'example': {
                'title': "DeSantis broaches repeal of Disney World's special self-governing status in Florida",
                'body': 'Florida’s Republican Gov. Ron DeSantis addressed on Thursday the suggestion of repealing a 55-year-old state law that allows Disney to effectively govern itself on the grounds of Walt Disney World, following the company’s public opposition to a controversial parental rights law in Florida.'
            }
        }
        orm_mode = True


class UniversityCreateConfig(Dto):
    class Config:
        schema_extra = {
            'example': {
                'name': "National University of Uzbekistan",
                'abbr': 'Higher educational institutions originated in eastern Iran in the 10th century CE and spread to major urban centers throughout the Middle East by the late 11th century. Simultaneously, universities were established in the West.',
                'description': 'In the beginning of the 20th century, jadids tried to establish universities with the collaboration of Russian democrats. Muslim People University was headed by a council consisting of 45 people. It aimed to offer higher, secondary and primary education. In autumn, Muslim People University and its founders were the first victims of repression from communists.'
            }
        }
        orm_mode = True
