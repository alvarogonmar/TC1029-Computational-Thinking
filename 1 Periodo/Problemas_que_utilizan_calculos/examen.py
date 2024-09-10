import math

print('El siguiente programa te ayuda a saber cuantas horas estudiaste en la semana')
lunes = int(input('Cuantos minutos estudiaste el lunes\r\n'))
cont = input('Desea continuar?:\r\n')
if cont == 'n':
    hor = round(lunes/60, 0)
    mins = lunes % 60
    print(f'Esta vez estudiaste {hor} horas y {mins} minutos')
elif cont == 's':
    martes = int(input('Cuantos minutos estudiaste el martes\r\n'))
    cont = input('Desea continuar?:\r\n')
    if cont == 'n':
        hor = round((lunes+martes)/60, 0)
        mins = (lunes+martes )% 60
        print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a martes')
    elif cont == 's':
        mier = int(input('Cuantos minutos estudiaste el miercoles\r\n'))
        cont = input('Desea continuar?:\r\n')
        if cont == 'n':
            hor = round((lunes+martes+mier)/60, 0)
            mins = (lunes+martes+mier)% 60
            print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a miercoles')
        elif cont == 's':
            jue = int(input('Cuantos minutos estudiaste el jueves\r\n'))
            cont = input('Desea continuar?:\r\n')
            if cont == 'n':
                hor = math.floor((lunes+martes+mier+jue)/60)
                mins = (lunes+martes+mier+jue)% 60
                print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a jueves')
            elif cont == 's':
                vier = int(input('Cuantos minutos estudiaste el viernes\r\n'))
                cont = input('Desea continuar?:\r\n')
                if cont == 'n':
                    hor = round((lunes+martes+mier+jue+vier)/60, 0)
                    mins = (lunes+martes+mier+jue+vier)% 60
                    print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a viernes')
                elif cont == 's':
                    sab = int(input('Cuantos minutos estudiaste el sabado\r\n'))
                    cont = input('Desea continuar?:\r\n')
                    if cont == 'n':
                        hor = round((lunes+martes+mier+jue+vier+sab)/60, 0)
                        mins = (lunes+martes+mier+jue+vier+sab)% 60
                        print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a sabado')
                    elif cont == 's':
                        dom = int(input('Cuantos minutos estudiaste el domingo\r\n'))
                        hor = round((lunes+martes+mier+jue+vier+sab+dom)/60, 0)
                        mins = (lunes+martes+mier+jue+vier+sab+dom)% 60
                        print(f'Esta vez estudiaste {hor} horas y {mins} minutos de lunes a domingo')

