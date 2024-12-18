import logging
from datetime import datetime
from uuid import uuid4

# 模擬資料庫
books_db = {}

class BookService:
    def add_book(self, data):
        required_fields = ["書名", "ISBN", "作者", "版本", "出版年份", "書本類別", "價格", "書況"]
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")
        
        # 生成唯一 ID 和時間
        book_id = str(uuid4())
        posted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 新增書籍資料
        book_data = {
            "id": book_id,
            "書名": data["書名"],
            "ISBN": data["ISBN"],
            "作者": data["作者"],
            "版本": data["版本"],
            "出版年份": data["出版年份"],
            "書本類別": data["書本類別"],
            "價格": data["價格"],
            "書況": data["書況"],
            "posted_time": posted_time
        }
        books_db[book_id] = book_data
        return book_data

    def get_books(self):
        return list(books_db.values())

    def search_book_by_id(self, book_id):
        if book_id not in books_db:
            raise ValueError("Book not found")
        return books_db[book_id]
