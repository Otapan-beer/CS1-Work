# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:04:00 2024

@author: otaka
"""

import json

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    #input
    min_year = int(input("Min year => ").strip())
    print(min_year)
    max_year = int(input("Max year => ").strip())
    print(max_year)
    w1 = float(input("Weight for IMDB => ").strip())
    w1_s = str(w1)
    if w1_s == "0.0":
        w1_s = "0"
    elif w1_s == "-0.0":
        w1_s == "-0.0"
    print(w1_s)
    w2 = float(input("Weight for Twitter => ").strip())
    w2_s = str(w2)
    if w2_s == "0.0":
        w2_s = "0"
    elif w2 == "-0.0":
        w2 == "-0.0"
    print(w2_s)
    w1 = float(w1)
    w2 = float(w2)
    
    #setup and spacing
    genre = "beginning"
    while genre != "Stop":
        
        print() # spacing
        genre = str(input("What genre do you want to see? ").strip())
        print(genre)
        
        genre = genre.capitalize()
        
        if genre == "Stop":
            break
                
        if genre == "Sci-fi":
            genre = "Sci-Fi"
        
        print() #spacing
        
        #setup values
        min_rating = 11
        max_rating = -1
        worst_year = None
        worst_movie = None
        best_year = None
        best_movie = None
        
        
        #the actual search
        for i in movies.keys():
            year = movies[i]["movie_year"]
            movie_genre = movies[i]["genre"]
            if min_year <= year <= max_year and genre in movie_genre and i in ratings.keys():
                if(len(ratings[i]) >= 3):#filtering
                    movie_name = movies[i]["name"]
                    imbd_rating = (movies[i]["rating"]) * w1
                    twitter_rating = (sum(ratings[i])/len(ratings[i])) * w2
                    total_rating = (imbd_rating + twitter_rating) # the resulting rating
                    
                    if total_rating < 1:
                        total_rating *= 10
                    
                    #formatting the ifffs
                    if total_rating == min_rating:
                        worst_test = [(movie_name, year), (worst_movie, worst_year)]
                        worst_test.sort()
                        worst_movie = worst_test[0][0]
                        worst_year = worst_test[0][1]
                    if total_rating == max_rating:
                        best_test = [(movie_name, year), (best_movie, best_year)]
                        best_test.sort(reverse = True)
                        best_movie = best_test[0][0]
                        best_year = best_test[0][1]
                    if total_rating < min_rating:
                        worst_year = year
                        worst_movie = movie_name
                        min_rating = total_rating
                    if total_rating > max_rating:
                        best_year = year
                        best_movie = movie_name
                        max_rating = total_rating
        
        #Output
        if worst_year == None or best_year == None or min_rating == -1 or max_rating == 11:
            print("No", genre, "movie found in", min_year, "through", max_year)
        else:
            print("Best:")
            print(" "*8 + "Released in ", best_year, ", ", best_movie, " has a rating of {:.2f}".format(max_rating), sep = "")
            
            print()
            
            print("Worst:")
            print(" "*8 + "Released in ", worst_year, ", ", worst_movie, " has a rating of {:.2f}".format(min_rating), sep = "")
            
                
        
                
                
            