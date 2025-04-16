from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.movie_booking
movies = db.movies

# Remove all existing movies
movies.delete_many({})

# Insert your preferred movies
movies.insert_many([
    {
        "title": "Darling",
        "description": "A light-hearted romantic drama starring Prabhas and Kajal Aggarwal.",
        "poster_url": "https://i.pinimg.com/736x/a4/49/46/a44946c435466a9e4c3391f5b23513e7.jpg",
        "showtimes": ["11:00 AM", "2:00 PM", "6:00 PM"]
    },
    {
        "title": "Nuvvu Vasthanante Nenu Vaddantana",
        "description": "A heart-touching love story directed by Prabhu Deva, featuring Siddharth and Trisha.",
        "poster_url": "https://i.pinimg.com/736x/9b/da/56/9bda56f9995ab84e2e14da178889e6d1.jpg",
        "showtimes": ["12:00 PM", "3:30 PM", "7:00 PM"]
    },
    {
        "title": "Policodu",
        "description": "An action drama revolving around a mysterious police officer with a secret past.",
        "poster_url": "https://i.pinimg.com/736x/0e/28/62/0e286251b7e4b6a0283b31f3f432dab5.jpg",
        "showtimes": ["10:30 AM", "1:45 PM", "5:15 PM"]
    },
    {
        "title": "Remo",
        "description": "A fun romantic comedy with Sivakarthikeyan in a nurse disguise, trying to win his love.",
        "poster_url": "https://i.pinimg.com/736x/98/16/e7/9816e7b8c8b65a6e5e859899d212b9ba.jpg",
        "showtimes": ["11:15 AM", "2:45 PM", "6:15 PM"]
    },
    {
        "title": "Sanam Teri Kasam",
        "description": "A tragic romantic tale that will pull at your heartstrings with deep emotional moments.",
        "poster_url": "https://i.pinimg.com/736x/1c/ce/2d/1cce2d3c6549444c9935f2719c39a177.jpg",
        "showtimes": ["1:00 PM", "4:30 PM", "8:00 PM"]
    },
    {
        "title": "Tholi Prema",
        "description": "A sweet romantic journey of first love, starring Varun Tej and Raashi Khanna.",
        "poster_url": "https://i.pinimg.com/736x/30/e6/d3/30e6d3f3ac561203a6446a4d7cb1bd66.jpg",
        "showtimes": ["1:00 PM", "4:30 PM", "8:00 PM"]
    },
    {
        "title": "Geetha Govindam",
        "description": "A clean romantic entertainer with charming performances by Vijay Deverakonda and Rashmika Mandanna.",
        "poster_url": "https://i.pinimg.com/736x/2d/f4/aa/2df4aa255868e55b0dc0ae168ce4e046.jpg",
        "showtimes": ["11:00 AM", "2:30 PM", "6:00 PM"]
    },
    {
        "title": "Majili",
        "description": "A tale of heartbreak and healing, starring Naga Chaitanya and Samantha.",
        "poster_url": "https://i.pinimg.com/736x/76/a4/b1/76a4b17df3c7ae70c762e5d613018d60.jpg",
        "showtimes": ["12:15 PM", "3:45 PM", "7:15 PM"]
    },
    {
        "title": "Bommarillu",
        "description": "A feel-good family entertainer about love and individuality, starring Siddharth and Genelia.",
        "poster_url": "https://i.pinimg.com/736x/4d/2c/a0/4d2ca003ed9194d0319a3ed72d814659.jpg",
        "showtimes": ["10:00 AM", "1:30 PM", "5:00 PM"]
    }
])

print("Updated Telugu movies inserted successfully!")