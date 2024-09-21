# Funciones para manejar los gastos
# Este archivo deve contener leerGastosH, mostrarTotalGastosH
# añadirGastoH, sumarAhorro, restarAhorro, editar_AhorroH, sumarGastosH
#Recuerde nombrar las funciones exactamente como se menciono anteriormente para que el programa funcione correctamente
#Recuerde que las funciones deben retornar y recibir los parametros mencionados en cada espacio.
#No olvide que en los diccionarios las categoria siempre deben empezar con mayuscula y sin tilde
#esto es para que el programa no tenga problemas al las categorias

#funcion para leer los gastos de Hogar (leerGastosH)
# La siguiente funcion recibe el nombre del usuario
# y retorna un diccionario con las categorias de gastos y los valores de cada categoria
# si el usuario no tiene gastos registrados se retorna un diccionario con los valores en 0




#funcion para mostrar el total de lo gastado en hogar (mostrarTotalGastosH)
#La siguiente funcion recibe un diccionario con las categorias de gastos y los valores de cada categoria
#este diccionario sera dado por la funcion leerGastosH
#y retorna la suma de los valores de cada categoria sin contar el ahorro ya que este no es un gasto a pesar de encontrarse en el mismo archivo txt




#funcion para añadir gastos por categorias (añadirGastoH)
#La siguiente funcion recibe el nombre del usuario, la categoria del gasto y el valor del gasto a añadir
#se busca que la funcion añada a la lista de gastos de la categoria correspondiente el valor del gasto
#debe retornar True si el gasto fue añadido correctamente y False si hubo algun error, en cada caso se debe retornar un mensaje
#Si la respuesta es true retorne un mensaje vacio




#funciones para el manejo del ahorro (editar_AhorroH)
#Se debe tener una funcion para editar el ahorro que reciba el nombre del usuario, la opcion de Añadir o retirar y el valor a añadir o retirar
#La opcion se pasara como un string, si la opcion es "Añadir" se sumara el valor al ahorro y si la opcion es "retirar" se restara el valor al ahorro
#Tome en cuenta que los valores que se pasan a la funcion son exactamente estos 2, como estan escritos anteriormente, puede que si intenta compararlos sin escribirlos asi el programa le genere un error
#se debe retornar True si el ahorro fue editado correctamente y False si hubo algun error, en cada caso se debe retornar un mensaje
#Si la respuesta es true retorne un mensaje vacio
#Tenga en cuenta que el valor de ahorro enviado a la funcion es de tipo str y debe ser convertido antes de ser sumado o restado
#Reto: no deje que el ahorro sea negativo ni 0 y retorne un mensaje con esta opcion





#Funcion para sumar gastos por categorias( sumarGastosH)
#La siguiente funcion recibe el nombre del usuario y retorna un diccionario con las categorias de gastos y los valores de cada categoria
# Recuerde que Ahorro no es una lista de gastos, por lo que no se debe sumar solo se debe retornar el valor del ahorro
#si el usuario no tiene gastos registrados se retorna un mensaje de error




