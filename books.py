from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()


BOOKS = {
    'book_1' : {'title':'Title One', 'author':'Author One'},
    'book_2' : {'title':'Title Two', 'author':'Author Two'},
    'book_3' : {'title':'Title Three', 'author':'Author Three'},
    'book_4' : {'title':'Title Four', 'author':'Author Four'},
    'book_5' : {'title':'Title Five', 'author':'Author Five'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title" : "My favorite book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_title": book_id }


@app.get("/directions/{direction_name}")
async def get_direction(direction_name : DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction":direction_name, "sub":'Up'}
    if direction_name == DirectionName.south:
        return {"Direction":direction_name, "sub":'Down'}
    if direction_name == DirectionName.west:
        return {"Direction":direction_name, "sub":'Left'}
    if direction_name == DirectionName.east:
        return {"Direction":direction_name, "sub":'Right'}


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
                
    BOOKS['book_{id}'.format(id=current_book_id + 1)] = {
        'title': book_title,
        'author': book_author
    }
    
    return BOOKS['book_{id}'.format(id=current_book_id + 1)]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_infomation = {
        'title': book_title,
        'author': book_author,
    }
    BOOKS[book_name] = book_infomation
    
    return book_infomation