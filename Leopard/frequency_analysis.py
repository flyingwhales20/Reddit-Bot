#### Count Words ####
# We take the content of leopard.txt and count the unique words.
# The word count data is stored in word_count.txt and
#
# @param dead_leopard = the file the words will be counted
def count_whiskers(dead_leopard):
    # Open up leopard.txt
    leopard_txt = open(dead_leopard,"r")
    whiskers = [];
    
    for snout in leopard_txt: # Navigate line by line through the file
        snout = snout.upper() # Make all characters UPPERCASE
        whiskers += snout.split(" ")    

    print(whiskers)
    leopard_txt.close()
#end def count_whiskers
