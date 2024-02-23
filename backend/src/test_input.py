from bson import ObjectId
from datetime import datetime
import pymongo

categories = [
    {'_id': str(ObjectId()),
     'slug': 'Water Quality',
     'title': 'Water Quality',
     'image': '/water.jpg'},

    {'_id': str(ObjectId()),
     'slug': 'Ecology',
     'title': 'Ecology',
     'image': '/ecology.jpg'},

    {'_id': str(ObjectId()),
     'slug': 'Hydrology',
     'title': 'Hydrology',
     'image': '/hydrology.jpg'},

    {'_id': str(ObjectId()),
     'slug': 'Coding',
     'title': 'Coding',
     'image': '/coding.jpg'},

    {'_id': str(ObjectId()),
     'slug': 'Climate Change',
     'title': 'Climate Change',
     'image': '/climate.jpeg'},

    {'_id': str(ObjectId()),
     'slug': 'AI',
     'title': 'AI',
     'image': '/AI.jpeg'}]

posts = [{
    '_id': str(ObjectId()),
    'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
    'title': 'fake_title',
    'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                   'none of the above commands have actually performed any operations on the MongoDB server. '
                   'Collections and databases are created when the first document is inserted into them.',
    'image': '/tree2.png',
    'views': 5,
    'categories': 'AI',
    'user_name': 'Ahmad Saremi',
    'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created '
                       'lazily -'
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/2.jpg',
        'views': 5,
        'categories': 'Ecology',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/tree2.png',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/2.jpg',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/tree2.png',
        'views': 5,
        'categories': 'Hydrology',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/2.jpg',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/tree2.png',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/2.jpg',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},

    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'title': 'fake_title',
        'description': 'An important note about collections (and databases) in MongoDB is that they are created lazily - '
                       'none of the above commands have actually performed any operations on the MongoDB server. '
                       'Collections and databases are created when the first document is inserted into them.',
        'image': '/tree2.png',
        'views': 5,
        'categories': 'AI',
        'user_name': 'Ahmad Saremi',
        'user_id': 'clqvvjvzc000014eumd7oejwh'}]

comments = [{
    '_id': str(ObjectId()),
    'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
    'post_id': '659443d34980e109f29f57f0',
    'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                   'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                   'pariatur? Pariatur numquam accusantium eum nostrum!',
    'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f2',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'
    }
    , {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f4',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f0',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f2',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'
    }
    , {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f4',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f0',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f2',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'
    }
    , {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f4',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f0',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
    {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f2',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'
    }
    , {
        '_id': str(ObjectId()),
        'date': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'post_id': '659443d34980e109f29f57f4',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta cupiditate magni ducimus '
                       'inventore sequi perspiciatis, esse, nemo dolores, aut explicabo rerum facere adipisci omnis '
                       'pariatur? Pariatur numquam accusantium eum nostrum!',
        'user_id': 'clqvvjvzc000014eumd7oejwh'},
]


if __name__ == "__main__":
    client = pymongo.MongoClient(host='127.0.0.1', port=27017)
    db = client.test_database
    collection = db.Categories
    collection.insert_many(categories)