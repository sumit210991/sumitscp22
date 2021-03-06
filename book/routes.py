from flask import Blueprint, request, jsonify

from models import Book, db

book_blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/book')


@book_blueprint.route('/all', methods=['GET'])
def get_all_books():
    all_books = Book.query.all()
    result = [book.serialize() for book in all_books]
    response = {"result":result}
    return jsonify(response)


@book_blueprint.route('/create', methods=['POST'])
def create_books():
    try:
        #upload_file=Upload_File()
        #if(upload_file.create_bucket('elearningbucket')):
          #          isFileUploaded=upload_file.upload_file('elearningbucket',magazineContent,magzineName+'.pdf')
        book = Book()
        book.name = request.form['name']
        book.slug = request.form['slug']
        book.author_name = request.form['author_name']
        book.published_year = request.form['published_year']
        #file_content=request.FILES['upload']
        #if(upload_file.create_bucket('elearningbucket')):
         #   isFileUploaded=upload_file.upload_file('elearningbucket',file_content,book.name)
          #  print(isFileUploaded)
        db.session.add(book)
        db.session.commit()

        response = {'message': 'Book Create', 'result': book.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Book creation failed'}

    return jsonify(response)


@book_blueprint.route('/<slug>', methods=['GET'])
def book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        response = {"result":book.serialize()}
    else:
        response = {"message":"No books found"}

    return jsonify(response)

    

    
