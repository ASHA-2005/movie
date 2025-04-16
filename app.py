from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.movie_booking
movies = db.movies
bookings = db.bookings

# Homepage
@app.route('/')
def index():
    movie_list = movies.find()
    return render_template('index.html', movies=movie_list)

# Movie Detail Page
@app.route('/movie/<movie_id>')
def movie_detail(movie_id):
    movie = movies.find_one({'_id': ObjectId(movie_id)})
    return render_template('movie_detail.html', movie=movie)

# Booking Handler
@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    name = request.form['name']
    email = request.form['email']
    tickets = int(request.form['tickets'])  # convert to int for calculation
    showtime = request.form['showtime']
    movie_title = request.form['movie_title']
    seats = request.form['seats']
    payment_method = request.form.get('payment_method', 'Not Provided')

    # 🔍 Fetch movie details from DB
    movie = movies.find_one({'title': movie_title})
    price = movie.get('price', 150)  # fallback if no price field in DB
    total_amount = price * tickets

    # 💾 Save to MongoDB
    booking = {
        'name': name,
        'email': email,
        'tickets': tickets,
        'showtime': showtime,
        'movie_title': movie_title,
        'seats': seats,
        'payment_method': payment_method,
        'total_amount': total_amount
    }
    bookings.insert_one(booking)

    # ✅ Render confirmation page
    return render_template(
        'booking_confirmation.html',
        name=name,
        movie=movie_title,
        tickets=tickets,
        showtime=showtime,
        seats=seats,
        total_amount=total_amount
    )

    # Save to DB if needed

    return render_template(
        'booking_confirmation.html',
        name=name,
        movie=movie_title,
        tickets=tickets,
        showtime=showtime,
        seats=seats
    )


# Confirmation Page
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html',
                           name=request.args.get('name'),
                           movie=request.args.get('movie'),
                           showtime=request.args.get('showtime'),
                           tickets=request.args.get('tickets'),
                           seats=request.args.get('seats'))

# Now Showing Page
@app.route('/now_showing')
def now_showing():
    movie_list = movies.find()
    return render_template('now_showing.html', movies=movie_list)

# Static Pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
