
from fastapi import FastAPI, Depends
import uvicorn

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from sqlmodel import Session, select
from .database import get_session, create_db_and_tables
from .models import Book, BookCreate, BookRead

templates = Jinja2Templates('app/templates')

app = FastAPI()


def configure():
    app.mount('/static', StaticFiles(directory='app/static'), name='static')
    # new ---
    create_db_and_tables()
    # -------


# changed
@app.get("/")
def home_page(*, session: Session = Depends(get_session), request: Request):
    books = session.exec(select(Book)).all()
    return templates.TemplateResponse('index.html', {'request': request, 'books': books})
# -------

# new
@app.post("/book")
def add_book(*, session: Session = Depends(get_session), book: BookCreate) -> BookRead:
    db_book = Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book
# -------


if __name__=="__main__":
    configure()
    uvicorn.run('app.main:app', reload=True)
else:
    configure()