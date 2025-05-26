while True:
    numero1=float(input("Ingrese numero1: "))
    numero2=float(input("ingrese numero2: "))
    print("1. Sumar")
    print("2.restar")
    print("3.dividir")
    print("4.multiplicar")
    print("5.Salir")
    opcion=input("ingrese opcion: ")


    match opcion:
        case "1":
            resultado=numero1+numero2
            
            
        case "2":
            resultado=numero1-numero2
            
        case "3":
            if  numero2==0:
                print("ERROR NO SE PUEDE DIVIDIR POR CERO!!")
            else:
                resultado=numero1/numero2
                
        case "4":
            resultado=numero1*numero2
        case "5":
            break
    print(f"Resultado: {resultado}")       
    salir=input("Deseas Salir?(Si)")
    if salir.capitalize()=="Si":
        break
   
        
                    
    
    
