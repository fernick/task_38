# Note - Version 2 - considers two
'''
For this version, 2 correctionas were made
* we take movie description as an argument
* We also return one most similar movie

'''


# Task description
'''
For this task we build a movie recommender
The system will recommend top movie given the similarity
We call this program: Hyperion Netflix!
'''

# import needed librari
import spacy
nlp = spacy.load('en_core_web_md')


# opening movie data
movie_list=[]
with open("movies.txt","r") as f:
    for line in f.readlines():
        line_stripped= line.strip('\n')
        movie_list.append(line_stripped)

# movie reference description to compare
hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
            Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
            planet where the Hulk can live in peace. Unfortunately, Hulk land on the
            planet Sakaar where he is sold into slavery and trained as a gladiator'''

to_compare = nlp(hulk)

# find similarity score


# defining a function to collect similarity score
similarity_score = []
def score_collector():
    
    for movie in movie_list:
        similarity = nlp(movie).similarity(to_compare)
        similarity_score.append(similarity)
    

# finding the top 4
def get_top(to_be_compared):
    score_collector()
    print("\nYou might like this movie as well.")
    print("=========================")
    for movie in movie_list:
        
        similarity = nlp(movie).similarity(to_be_compared)
        movie_split = movie.split(":")
        movie_title = movie_split[0]
        if similarity == max(similarity_score):
            print(movie_title + ":", similarity)
        else:
            pass

    print("\nThank you for using Hyperion Netflix!!\n")

# Start of the program to get the top movie
get_top(to_compare)






