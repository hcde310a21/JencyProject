# JencyProject
Final 310 Project
For this project, I ended with a final product slightly different from what I had expected. Initially, I planned on using the Google Books API to sort through different categories and find a final initial project. However, I ended up realizing that the Google Books API was extremely difficult to sort through by genre (a call for "fiction" books would return a list with "Genesis" on it, which is highly contraversial). Thus, I ended up switching APIs to the New York Books API, which had booklists based on categories. 


With the New York Books API, I returned 5 books based on the weather type. One of the challenges with this was figuring out how to randomize my list. I initally had used the random.choice command, but that would return repeat books. I had to use the random.sample command so that the program would return a list that did not include two of one book.  
