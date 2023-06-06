from claseLista import Lista
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseDocente import Docente
from clasePersonalApoyo import PersonalApoyo

def crear_agente():
    print("Seleccione el tipo de agente que desea crear:")
    print("1. Docente")
    print("2. Investigador")
    print("3. Docente Investigador")
    print("4. Personal de Apoyo")
    
    tipo_agente = int(input("Ingrese el número correspondiente al tipo de agente: "))
    
    cuil = input("Ingrese el CUIL del agente: ")
    nombre = input("Ingrese el nombre del agente: ")
    apellido = input("Ingrese el apellido del agente: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
    antiguedad = int(input("Ingrese la antigüedad del agente: "))

    if tipo_agente == 1:
        carrera = input("Ingrese la carrera del docente: ")
        cargo = input("Ingrese el cargo del docente: ")
        catedra = input("Ingrese la cátedra del docente: ")
        docente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        objeto=docente
    elif tipo_agente == 2:
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        investigador = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        objeto=investigador
    elif tipo_agente == 3:
        carrera = input("Ingrese la carrera del docente investigador: ")
        cargo = input("Ingrese el cargo del docente investigador: ")
        catedra = input("Ingrese la cátedra del docente investigador: ")
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        categoria_incentivos = input("Ingrese la categoría en el programa de incentivos de investigación: ")
        importe_extra = float(input("Ingrese el importe extra por docencia e investigación: "))
        docente_investigador = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        objeto=docente_investigador
    elif tipo_agente == 4:
        categoria = input("Ingrese la categoría del personal de apoyo: ")
        personal_apoyo = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
        objeto=personal_apoyo
    else:
        print("Opción no válida.")
    return objeto

def menu(lista_agentes):
    lista_agentes.cargar_desde_archivo("personal.json")
    while True:
        print("1. Insertar a agentes a la colección")
        print("2. Agregar agentes a la colección")
        print("3. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print("4. Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("5. Dada un área de investigación, contar la cantidad de agentes que son docente_investigador, y la cantidad de investigadores que trabajen en ese área.")
        print("6. Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7. Listar docentes investigadores por categoría")
        print("8. Almacenar los datos de todos los agentes en el archivo personal.json")
        print("9. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agente = crear_agente()
            posicion = int(input("Ingrese la posición en la que desea insertar el agente: "))
            try:
                lista_agentes.insertar_agente(posicion, agente)
                print(f"Agente {agente.get_nombre()} {agente.get_apellido()} insertado en la posición {posicion}.")
            except ValueError as e:
                print(str(e))
        elif opcion == 99:
            lista_agentes.mostrarTodo()

        elif opcion == 2:
            agente = crear_agente()
            lista_agentes.agregar_agente(agente)
            print(f"Agente {agente.get_nombre()} {agente.get_apellido()} agregado a la colección.")

        elif opcion == 3:
            posicion = int(input("Ingrese la posición: "))
            try:
                agente = lista_agentes.obtener_agente(posicion)
                print(f"Tipo de Agente: {type(agente).__name__}")
            except IndexError as e:
                print(str(e))

        elif opcion == 4:
            carrera = input("Ingrese el nombre de una carrera: ")
            lista_agentes.listado_ordenado(carrera)


        elif opcion == 5:
            area_investigacion = input("Ingrese el nombre de un area de investigación: ")
            lista_agentes.contar_agentes_por_area_investigacion(area_investigacion)
        
        elif opcion == 6:
            lista=lista_agentes.generar_listado_agentes()
            for nombre, apellido, tipo, sueldo in lista:
                print(f"Nombre: {nombre}, Apelldio: {apellido}, Tipo: {tipo}, Sueldo: {sueldo}")
            
            
        elif opcion == 7:
            categoria_investigacion = input("Ingrese la categoría de investigación: ")
            lista_agentes.listar_importe_extra_por_categoria(categoria_investigacion)
            
        elif opcion == 8:
                lista_agentes.guardar_en_archivo("personal.json")
        
        elif opcion == 9:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    lista_agentes = Lista()
    menu(lista_agentes)