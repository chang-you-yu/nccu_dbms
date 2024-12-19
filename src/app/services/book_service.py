from ..models.book_model import db, Book

def create_book(data):
    """新增二手書資料"""
    # 驗證必要字段
    required_fields = ['書名', 'ISBN', '作者', '版本', '出版年份', '書本類別', '價格', '書況']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    try:
        # 構建書籍對象
        new_book = Book(
            書名=data['書名'],
            ISBN=data['ISBN'],
            作者=data['作者'],
            版本=data['版本'],
            出版年份=data['出版年份'],
            書本類別=data['書本類別'],
            價格=float(data['價格']),  # 確保價格為浮點數
            書況=data['書況']
        )
        # 將書籍添加到數據庫
        db.session.add(new_book)
        db.session.commit()
        return new_book
    except Exception as e:
        db.session.rollback()  # 回滾事務
        raise e

def update_book_by_id(book_id, data):
    """更新指定書籍的資料"""
    book = Book.query.get(book_id)
    if not book:
        return None  # 書籍未找到，返回 None

    try:
        # 更新書籍資料
        for key, value in data.items():
            if hasattr(book, key):  # 確保字段存在於模型中
                setattr(book, key, value)

        db.session.add(book)
        db.session.commit()
        return book
    except Exception as e:
        db.session.rollback()  # 回滾事務
        raise e
    
def get_all_books():
    """獲取所有書籍"""
    return Book.query.all()

def search_books_by_criteria(query):
    """根據查詢條件搜索書籍"""
    return Book.query.filter(
        (Book.書名.like(f"%{query}%")) |
        (Book.ISBN.like(f"%{query}%")) |
        (Book.作者.like(f"%{query}%")) |
        (Book.書本類別.like(f"%{query}%"))
    ).all()
