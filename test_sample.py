from main import greet
def test_greet():
 black_list = ['Petya', 'Vanya', 'Masha']
 assert greet("world", black_list) == "Hello, world!"
