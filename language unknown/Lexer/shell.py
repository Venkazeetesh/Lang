import Unknown

while True:    #Here we defined infinite loop that can read and write in shell
    text = input('Unknown:')
    output, error = Unknown.run('Now its self lexer introduced only for integers and float', text)

    if error: print(error.as_string()) #Here as_strings function changes those errors into readable strings on output
    else: print(output) #If there is no error meaning that we just created a integers tokens it will print output
#Here what lexer will do is break character by character and print list of tokens for further process...
#A token is nothing but a simple object has a type and value eg:For integer (123) ---> Shows [INT:123]
