print("----- CONVERSOR DE DIVISAS -----")


while(True):

    eleccion = input("DOP A DOLAR(USD) [1] -- YEN A EURO [2] -- COP A DOP [3]: \n" )   

    if(eleccion == "1"): 
        print("----- DOP A DOLAR -----")
        #DOP A DOLAR
        def exchange_money(budget,exchange_rate):

            return budget * exchange_rate
    
        resultado = exchange_money(float(input("INGRESE CANTIDAD DE PESOS A CONVERTIR: ")),0.017)               
        print(str(resultado) + " DOLARES")  
        
        print("-------------------------------------\n\n")

            

    if(eleccion == "2"):
        print("----- YEN A EURO -----")
        #YEN A EURO
        def exchange_money(budget,exchange_rate):

            return budget * exchange_rate
                       
        resultado = exchange_money(float(input("INGRESE CANTIDAD DE YENES A CONVERTIR: ")),0.0062)               
        print(str(resultado) + " EUROS")        
        
    print("-------------------------------------\n\n")
  


    if(eleccion == "3"):
        print("----- COP A DOP -----")
        #COP A DOP
        def exchange_money(budget,exchange_rate):

            return budget * exchange_rate
        
        resultado = exchange_money(float(input("INGRESE CANTIDAD DE PESOS A CONVERTIR: ")),0.014)               
        print(str(resultado) + " DOP")
        
        print("-------------------------------------\n\n")




    
        

    


