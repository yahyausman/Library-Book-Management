from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yahya123",  
        database="library_db"
    )

@app.route('/')
def home():
    return render_template('library.html')

@app.route('/get_books')
def get_books():
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books ORDER BY book_id")
        return jsonify({'success': True, 'books': cursor.fetchall()})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/add_book', methods=['POST'])
def add_book():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, category, isbn, publisher, year, quantity, available) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (request.form['title'], request.form['author'],
             request.form.get('category',''), request.form.get('isbn',''),
             request.form.get('publisher',''), request.form.get('year') or None,
             int(request.form.get('quantity',0)), int(request.form.get('available',0)))
        )
        db.commit()
        return jsonify({'success': True, 'book_id': cursor.lastrowid})
    except mysql.connector.IntegrityError:
        return jsonify({'success': False, 'error': 'ISBN already exists'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/update_book', methods=['POST'])
def update_book():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE books SET title=%s, author=%s, category=%s, isbn=%s, publisher=%s, year=%s, quantity=%s, available=%s WHERE book_id=%s",
            (request.form['title'], request.form['author'],
             request.form.get('category',''), request.form.get('isbn',''),
             request.form.get('publisher',''), request.form.get('year') or None,
             int(request.form.get('quantity',0)), int(request.form.get('available',0)),
             int(request.form['book_id']))
        )
        db.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE book_id=%s", (int(request.form['book_id']),))
        db.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/search_books')
def search_books():
    try:
        q = '%' + request.args.get('q','') + '%'
        field = request.args.get('field','all')
        db = get_db()
        cursor = db.cursor(dictionary=True)
        if field == 'title':
            cursor.execute("SELECT * FROM books WHERE title LIKE %s", (q,))
        elif field == 'author':
            cursor.execute("SELECT * FROM books WHERE author LIKE %s", (q,))
        elif field == 'category':
            cursor.execute("SELECT * FROM books WHERE category LIKE %s", (q,))
        elif field == 'isbn':
            cursor.execute("SELECT * FROM books WHERE isbn LIKE %s", (q,))
        else:
            cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR category LIKE %s OR isbn LIKE %s", (q,q,q,q))
        return jsonify({'success': True, 'books': cursor.fetchall()})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
