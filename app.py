from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Your time is limited, so don’t waste it living someone else’s life.", "author": "Steve Jobs"},
    {"quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
    {"quote": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
    {"quote": "If you can dream it, you can do it.", "author": "Walt Disney"},
    {"quote": "Happiness depends upon ourselves.", "author": "Aristotle"},
    {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
    {"quote": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair"},
    {"quote": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"quote": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
    {"quote": "Turn your wounds into wisdom.", "author": "Oprah Winfrey"},
    {"quote": "Your limitation—it’s only your imagination.", "author": "Unknown"},
    {"quote": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"quote": "Great things never come from comfort zones.", "author": "Unknown"},
    {"quote": "Dream it. Wish it. Do it.", "author": "Unknown"},
    {"quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"quote": "Act as if what you do makes a difference. It does.", "author": "William James"},
    {"quote": "Success is getting what you want. Happiness is wanting what you get.", "author": "Dale Carnegie"},
    {"quote": "When you have a dream, you've got to grab it and never let go.", "author": "Carol Burnett"},
    {"quote": "With the new day comes new strength and new thoughts.", "author": "Eleanor Roosevelt"},
    {"quote": "Failure is not the opposite of success; it’s part of success.", "author": "Arianna Huffington"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
    {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"quote": "Doubt kills more dreams than failure ever will.", "author": "Suzy Kassem"},
    {"quote": "You must be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"quote": "Don’t count the days, make the days count.", "author": "Muhammad Ali"},
    {"quote": "Opportunities don’t happen. You create them.", "author": "Chris Grosser"},
    {"quote": "I never dreamed about success. I worked for it.", "author": "Estée Lauder"},
    {"quote": "Life isn’t about finding yourself. It’s about creating yourself.", "author": "George Bernard Shaw"},
    {"quote": "Don’t wait for opportunity. Create it.", "author": "Unknown"},
    {"quote": "Go confidently in the direction of your dreams.", "author": "Henry David Thoreau"},
    {"quote": "Keep going. Everything you need will come to you at the perfect time.", "author": "Unknown"},
    {"quote": "Difficulties in life are intended to make us better, not bitter.", "author": "Dan Reeves"},
    {"quote": "You don’t need to see the whole staircase, just take the first step.", "author": "Martin Luther King Jr."},
    {"quote": "If opportunity doesn’t knock, build a door.", "author": "Milton Berle"},
    {"quote": "We have on this land what makes life worth living.", "author": "Mahmoud Darwish"},
    {"quote": "I have learned and dismantled all the words in order to draw from them a single word: Home.", "author": "Mahmoud Darwish"},
    {"quote": "Standing here, staying here, permanent here, eternal here, and we have one goal, one, one: to be.", "author": "Mahmoud Darwish"},
      {"quote": "A person can only be born in one place. However, he may die several times elsewhere: in exile, in prison, in a homeland that has become a grave.", "author": "Mahmoud Darwish"},
    {"quote": "Poetry and beauty are always making peace. When you read something beautiful you find coexistence; it breaks walls down.", "author": "Mahmoud Darwish"},
    {"quote": "To be under occupation is not a choice, but to resist is.", "author": "Mahmoud Darwish"},
    {"quote": "Nothing is harder on the soul than the smell of dreams while they are evaporating.", "author": "Mahmoud Darwish"},
    
    # William Shakespeare
    {"quote": "All the world’s a stage, and all the men and women merely players.", "author": "William Shakespeare"},
    {"quote": "There is nothing either good or bad, but thinking makes it so.", "author": "William Shakespeare"},
    {"quote": "Some are born great, some achieve greatness, and some have greatness thrust upon them.", "author": "William Shakespeare"},
    
    # Famous Artists
    {"quote": "Every child is an artist. The problem is how to remain an artist once we grow up.", "author": "Pablo Picasso"},
    {"quote": "I dream my painting and I paint my dream.", "author": "Vincent van Gogh"},
    {"quote": "Art is not what you see, but what you make others see.", "author": "Edgar Degas"},
    {"quote": "Creativity takes courage.", "author": "Henri Matisse"},
    {"quote": "The principles of true art is not to portray, but to evoke.", "author": "Jerzy Kosiński"},
    {"quote": "A true artist is not one who is inspired, but one who inspires others.", "author": "Salvador Dalí"},
    {"quote": "Every painting is a voyage into a sacred harbour.", "author": "Giotto di Bondone"},
    {"quote": "An artist cannot fail; it is a success to be one.", "author": "Charles Horton Cooley"},
    {"quote": "To create one’s own world takes courage.", "author": "Georgia O’Keeffe"},
    {"quote": "You use a glass mirror to see your face; you use works of art to see your soul.", "author": "George Bernard Shaw"},
    {"quote": "The object of art is not to reproduce reality, but to create a reality of the same intensity.", "author": "Alberto Giacometti"},
    {"quote": "What would life be if we had no courage to attempt anything?", "author": "Vincent van Gogh"},
    {"quote": "The artist must train not only his eye but also his soul.", "author": "Wassily Kandinsky"},
]

@app.route('/', methods=['GET'])
def get_random_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
