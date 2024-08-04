def decode(message_file):
    limit = 300 # limit is set to 300 as we can see our file has 300 lines or you may set it programatically and 299 is largest in our file data 
    #like by retrieving largest number in file and then making pyramid numbers structure upto to retrieved largest number
    # For example if file has 10 lines but largest number is 15 then our pyramid will be like that below
    # 1 , 2 3, 4 5 6 , 7 8 9 10, 11 12 13 14 15.. 15 is our limit as we don't have more numbers greater than 15 in our file
     #Like user say 6 then pyramid_numbers will have 1,3,6, See Below for pyramid structure with limit 6
    # 1,    2 3,    4 5 6.. Picking 1,3,6 as last number formed
    pyramid_numbers = [] # List to last numbers of pyramid strucute like 1,3,6,10,15 so on 

    n = 1 # This is to indicate level of pyramid, its value will change after each iteration

    '''Using n multiply by ( n + 1) and then divided by 2 formula is logic for finding last number
    Above Formula is used to find sum of natural numbers in maths as well'''
    ''' For Example, I want sum of first 6 natural numbers, it would be 1+2+3+4+5+6 equal to 21'''

    while True: # Setting Loop Condition as True mean loop will stop only inside body by any keyword like break 
        number = n * (n + 1) // 2 # Value retrieved by formula will be stored in number 

        # number value will change at each iteration as its scope is inside loop

        ''' Scenario you can think like 
        Condition to break loop is defined as I already told that if all ending numbers lik 1,3,6 are obtained our condition will be true like given below:
        For example, limit was 6 and number at value of n equals to 3, 6 > 6 false then again appending 6 into list
        Value of n Equals to 4 then number will be 10 as 4 * (4+1) / 2, 4 * (5) / 2, 20 /2, 10
        10>4, true so it will return pyramid_numbers list 
        '''
        if number > limit: # Let say your file greatest number is 300, it will stop if number becomes above than parameter passed
            break # break is a keyword that is used to stop execution of loops

        pyramid_numbers.append(number)  # Adding a number to list
        
        n += 1 # incrementing n value by 1 after each iteration
    # message_file is our file name and pyramid_numbers is list of last picked numbers from pyramid
    with open(message_file, 'r') as file:
        lines = file.readlines() # Reading all lines from file and store it in lines
    ''' Data in lines will be like that
    ['133 land\n', '160 sun\n', '88 too\n', '213 huge\n', '47 dont\n', '1 such\n', '156 noun\n', '155 student\n', '237 brown\n', '298 complete\n', '3 play\n', '233 cook\n', '278 yard\n', '259 clock\n', '137 would\n', '211 plain\n', '299 excite\n', '264 fire\n', '37 wish\n', '81 cool\n', '36 child\n', '129 past\n', '234 colony\n', '151 oil\n', '284 dog\n', '270 back\n', '254 money\n', '241 kind\n', '111 open\n', '221 finger\n', '63 touch\n', '271 are\n', '217 dad\n', '58 am\n', '187 modern\n', '82 meant\n', 
'93 ocean\n', '231 pitch\n', so on ]'''

    decoded_words = [] # List to store words retrieved after decoding
    
    '''line is variable to iterate over all items stored in lines like first getting value from 0 
    index that is '133 land\n', then so on upto all elements fetched from list'''

    for line in lines: 

        '''split function is builtin function that splits our line data on basis of space
        Like our data is '133 land\n', it will make it like ['133', 'land']
        So, you can say in our case it is making list having numerical value as first word and string value that 
        is alphabetical like land,sun,huge as second word'''

        '''For each line, it will split data like numerical value at first index of list and 
        word that is to be decoded at second index
        ''' 
        
        words = line.split() # This is builtin function
        # Split function split words on basis of space by default like ' ' is a space and
        # you may split words by , too but in our case words are separated by space like 124 word not by comma like 123,law 
        #print(words)
        # Our concern is with numbers only as pyramid numbers
        '''words[0] -> number like 28,299,1,3  , words[1] -> word like sun,land,too,huge'''
        number = int(words[0]) # Integer is used here because in words it is stored as string,
    # int(words[0]) will convert dataype of a number from string to integer in this case
        if number in pyramid_numbers: # check if number is in given pyramid_numbers that is actually pyramid list

            # IF condition is true, number with relevant decoded is added as a tuple in list
            # Tuple is usually like that t = (), it
            # We used tuples data structure here as we need to sort our words based on numbers later
            # We may have used dictionary as well, but dictionary is mutable whose elements can be updated
            # But, tuples are immutable as when we decoded words, we will not update them further
            decoded_words.append((number, words[1]))  

   # print(decoded_words)    
    ''' Before sorting our list of tuples, 
    [(1, 'such'), (3, 'play'), (36, 'child'), (231, 'pitch'), (91, 'suit'), (78, 'especially'), 
    (120, 'where'), (136, 'history'), (66, 'quotient'), (10, 'he'), (55, 'milk'), 
    (190, 'select'), (300, 'work'), (45, 'stay'), (153, 'solve'), (6, 'come'), 
    (28, 'it'), (105, 'each'), (276, 'wild'), (21, 'check'), 
    (253, 'people'), (210, 'select'), (15, 'paragraph'), (171, 'fact')]'''
    # Sorting our list based on number of decoded word
    decoded_words.sort()  # Sort the list based on numbers

    ''' After sorting our list of tuples, 
    [(1, 'such'), (3, 'play'), (6, 'come'), (10, 'he'), (15, 'paragraph'), 
    (21, 'check'), (28, 'it'), (36, 'child'), (45, 'stay'), 
    (55, 'milk'), (66, 'quotient'), (78, 'especially'), (91, 'suit'), 
    (105, 'each'), (120, 'where'), (136, 'history'), (153, 'solve'), 
    (171, 'fact'), (190, 'select'), (210, 'select'), (231, 'pitch'), 
    (253, 'people'), (276, 'wild'), (300, 'work')]'''

    decoded_message = ' '.join(word[1] for word in decoded_words)  # Extract words from sorted list
    ''' The purpose of above line decoded_message = ' '.join(word[1] for word in decoded_words) is to concatenate the decoded words stored in 
    the decoded_words list into a single string, separated by spaces.
    We we can use inside some functions as well like in join as python is flexible,
    word[1] will give as decoded word and space will be added after that word to join next word and finally
    forming a sentence'''

    return decoded_message # decoded_message type is string returned by function


# pass file name and pyramid_numbers of pyramid that contains numbers retrieved like 1,3,6,10,15
# decoded_message is a string holding sentence of words decoded from file
#print function will print string returned by decode function
print(decode("encoded_message.txt")) 


''' You work at a customer service center for a popular electronics company, handling technical support calls. Your workspace represents the function, and the tools and resources available to you represent variables.

Variables Defined in the Function (Outer Scope):
At your desk, you have access to various resources like a computer, a phone, a knowledge base, and troubleshooting guides. These resources are available throughout your shift and are like variables defined in the function but outside any loops. They provide you with the necessary tools to assist customers efficiently.

Variables Defined Inside a Loop (Inner Scope):
As calls come in, you engage with customers to address their technical issues. Each call you handle represents a loop iteration. Within each call, you have access to specific tools and information relevant to that customer's problem. For example, you might reference the customer's account details, review their purchase history, or check for known issues with their product model. These variables are specific to each call and are like variables defined inside a loop.

However, once the call ends (loop iteration completes), you no longer have access to the specific information related to that customer's issue. You move on to the next call, and the process repeats. The tools and resources available to you at your desk (defined in the outer scope) remain constant and can be used across multiple calls.'''
