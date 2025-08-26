from bson import ObjectId

from app.models.authors import ResponseAuthors
from app.repositories.authors import AuthorsRepository
repository = AuthorsRepository()

class AuthorsService:

    @staticmethod
    async def get_authors() -> list[ResponseAuthors]:
        authors = []
        if consult := await repository.get_all_authors():
            for author in consult:
                authors.append(ResponseAuthors(
                    id=str(author['_id']),
                    name=author['name'],
                    birth_year=author['birth_year'],
                    death_year=author.get('death_year'),
                    nationality=author.get('nationality'),
                    description=author.get('description'),
                    works=author.get('works', None)
                ))
        return authors

    @staticmethod
    async def get_author_by_id(author_id: str) -> ResponseAuthors | None:
        if consult := await repository.get_author_by_id(ObjectId(author_id)):
            return ResponseAuthors(
                id=str(consult['_id']),
                name=consult['name'],
                birth_year=consult['birth_year'],
                death_year=consult.get('death_year'),
                nationality=consult.get('nationality'),
                description=consult.get('description'),
                works=consult.get('works', None)
            )
        return None
