from flask import jsonify
import logging
from app.services.book_service import (
    create_book,
    update_book_by_id,
    get_all_books,
    search_books_by_criteria,
)

class BookController:
    def add_book(self):
        """新增書籍"""
        logging.info("----BookController.add_book----")
        data = request.get_json()

        # 驗證必要欄位
        required_fields = ["書名", "ISBN", "作者", "版本", "出版年份", "書本類別", "價格", "書況"]
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f"'{field}' is required"}), 400

        try:
            new_book = create_book(data)
            return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            return jsonify({'error': 'Failed to add book', 'details': str(e)}), 500

    def update_book(self, book_id):
        """更新書籍"""
        logging.info(f"----BookController.update_book: book_id={book_id}----")
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        try:
            updated_book = update_book_by_id(book_id, data)
            if updated_book:
                return jsonify({'message': 'Book updated successfully', 'book': updated_book.to_dict()}), 200
            else:
                return jsonify({'error': 'Book not found'}), 404
        except Exception as e:
            logging.error(f"Error updating book: {e}")
            return jsonify({'error': 'Failed to update book', 'details': str(e)}), 500

    def list_books(self):
        """列出所有書籍"""
        logging.info("----BookController.list_books----")

        try:
            books = get_all_books()
            return jsonify({
                'message': 'Books retrieved successfully',
                'books': [book.to_dict() for book in books]
            }), 200
        except Exception as e:
            logging.error(f"Error retrieving books: {e}")
            return jsonify({'error': 'Failed to retrieve books', 'details': str(e)}), 500

    def search_books(self):
        """搜尋書籍"""
        logging.info("----BookController.search_books----")
        query = request.args.get('query', '')

        if not query:
            return jsonify({'error': 'Query parameter is required'}), 400

        try:
            books = search_books_by_criteria(query)
            return jsonify({
                'message': 'Books searched successfully',
                'books': [book.to_dict() for book in books]
            }), 200
        except Exception as e:
            logging.error(f"Error searching books: {e}")
            return jsonify({'error': 'Failed to search books', 'details': str(e)}), 500


# 實例化控制器以供使用
book_controller = BookController()