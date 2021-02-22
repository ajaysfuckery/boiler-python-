# created by ajay!

import time

def Main():
    print('\n')
    print('            + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +')
    print("            |                               WELCOME TO BOILER!                          |")
    print("            |    THIS PROGRAM IS USED FOR GENERATION OF BOILERPLATE HTML AND C FILES    |")
    print("            |  UPDATES MAY OR MAY NOT BE RELEASED FOR THIS TOOL! I'LL SEE WHAT HAPPENS  |")
    print("            |                                  VERSION 1.0                              |")
    print('            + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +')
    print('\n')

    a = input('Would you like to generate a boilerplate file for HTML or C? (h or c): ')

    if a == 'h':
        print('\n')
        print('                             + - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('                             | HTML FILE HAS BEEN GENERATED! |')
        time.sleep(0.05)
        print('                             + - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('\n')
        output = open('output.html', 'w')
        output.write('<!-- The boilerplate code in this file was generated by Boiler! -->\n\n')
        output.write('<!DOCTYPE html>\n')
        output.write('<html>\n')
        output.write('  <head>\n\n')
        output.write('  </head>\n')
        output.write('  <body>\n\n')
        output.write('  </body>\n')
        output.write('</html>')
        output.close()

    elif a == "c":
        print('\n')
        print('                             + - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('                             |   C FILE HAS BEEN GENERATED   |')
        time.sleep(0.05)
        print('                             + - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('\n')
        output = open("output.c", "w")
        output.write('// Boilerlpate code in this file was generated by Boiler!\n\n')
        output.write('#include <stdio.h>\n')
        output.write('#include <stdlib.h>\n\n')
        output.write('int main(){\n\n\n\n\n')
        output.write('  return 0;\n')
        output.write('}\n')

    else:
        print('\n')
        print('            + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('            |    WRONG LETTER USED! PLEASE RE-RUN THE SCRIPT AND TRY AGAIN!   |')
        time.sleep(0.05)
        print('            |    LETTERS TO CHOOSE FROM: h FOR HTML FILE AND c FOR C FILE     |')
        time.sleep(0.05)
        print('            + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +')
        time.sleep(0.05)
        print('\n')
Main()
