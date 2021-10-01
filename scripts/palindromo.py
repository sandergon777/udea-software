def main():
    word=input("ingrese la palabra: ")
    minus=word.lower()
    witho_space=minus.replace(" ","")
    print (witho_space)
    inv_word=witho_space[::-1]
    print (inv_word)
    if witho_space==inv_word:
        print (f" {word} es un palindromo")
    else:
        print (f" {word} NO es un palindromo")
    opc=input("desea buscar otra palabra? (s/n): ")
    if opc=="s":
        main()
    else:
        print("Bye")    
print("encuentra un palindromo")
main()
