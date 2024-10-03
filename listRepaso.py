

list = [10,2]
print(list)

#optener  un valor de lista
print (list[1])

#como modifico el valor en la lista
list[1]=1
print(list)

#metodo para agregar elemento al final de la lista
list.append(3)
print(list)

#con la funcion len optenemos el numero de 
#elemnetos que coontienen : (la lista, tamaño de la lista)
print(len(list))

newlist=[4,6]
#metodo para insertarr en cualquier posicion 
#de la lista en un nuevo elemento
#posiscion y elemnto agregar
newlist.insert(1,5)
print(newlist)

#metodo para agregar al final de los elemnetos 
# de la otra lista o una tupla
list.extend(newlist)
print(list)

#metodo para eliminar un elemento de la lista
#que conincide con el valor dado
list.remove(1)
print(list)

#merodo para eliminar un elemnto de la lista
#en la posicion de la lista dada
list.pop(4)
print(list)

#metodo que cuenta cuantas veces aparece un valor en la lista
list.append(3)
print(list.count(3))

#metodo que ordena la lista de forma ascendente
list.sort()
print(list)

#metodo que invierte el orden de la lista
list.reverse()
print(list)


#metodo que copia superficialmente una lista
#( crear un nuevo espacio en memoria.cada
# lista es independiente a la otra)
newlist= list.copy()
newlist.append(10)
print(list,newlist)

#copiar una lista(se crea una referncia
# al mismo espacio de memoria, si cambia una lista la otra tambien)
newlist=list
newlist.append(20)
print(list,newlist)

#anidacion de listas
list= [1,2,3,[4,5,6]]
list2 = ["manzana", list]
print(list2)

#limpiar la lista
list2.clear()
print(list2)


list1=[1,2,3]
list2=list1
print(list2)

list1.clear()
print(list1)




