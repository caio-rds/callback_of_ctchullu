from fastapi import APIRouter
import app.api.v1.entities as entities
import app.api.v1.locations as locations
import app.api.v1.authors as authors
import app.api.v1.books as books
import app.api.v1.grimmories as grimmories
router = APIRouter()

router.include_router(entities.router)
router.include_router(locations.router)
router.include_router(authors.router)
router.include_router(books.router)
router.include_router(grimmories.router)
