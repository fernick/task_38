'''
For this task we build a movie recommender
The system will recommend top 4 movies based on their similarity
The program returns the titles of top 4 movies
'''
#import needed librari
import spacy
nlp = spacy.load('en_core_web_md')


#opening movie data
movie_list=[]
with open("movies.txt","r") as f:
    for line in f.readlines():
        line_stripped= line.strip('\n')
        movie_list.append(line_stripped)

#movie reference description to compare
hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
            Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
            planet where the Hulk can live in peace. Unfortunately, Hulk land on the
            planet Sakaar where he is sold into slavery and trained as a gladiator'''

to_compare = nlp(hulk)

#find similarity score


#defining a function to collect similarity score
def score_collector():
    for movie in movie_list:
        similarity = nlp(movie).similarity(to_compare)
        similarity_score.append(similarity)
    

#finding the top 4
def get_top_4():
    print("\nYou might like these 4 movies as well.")
    print("=========================")
    for movie in movie_list:
        
        similarity = nlp(movie).similarity(to_compare)
        movie_split = movie.split(":")
        movie_title = movie_split[0]
        if similarity in top_4_score:
            print(movie_title + ":", similarity)
        else:
            pass

    print("\nThank you for using Hyperion Netflix!!\n")



#Start of the program

#collect score
similarity_score = []
score_collector()

#perform ranking
top_4_score = sorted((similarity_score)[-4:],reverse=True)
top_4_movie=[]
get_top_4()





