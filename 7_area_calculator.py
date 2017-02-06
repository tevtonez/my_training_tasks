'''
Created on Nov 24, 2016
@author: kostya

TASK
Write area calculator function that takes number of arguments (1 arg. for circle, 2 for square
or rectangle, 3 for triangle, 4 for trapezoid), automatically detects which equation should it use
and then calculates and shows the surface area result.

Possible output:

=========================
| AREA CALCULATOR v.0.1 |
=========================

For CIRCLE area enter radius length and hit enter.
For SQUARE/RECTANGLE area enter high and length separated by comma.
For TRIANGLE area enter 3 lengths of its sides separated by commas.
For TRAPEZOID area enter 4 lengths of its sides separated by commas.

> Your input: 5, 4

The area of RECTANGLE is 20 square units.

'''

if __name__ == '__main__':

    import math

    def area_calc():

        figure = ''
        area = 0

        # asking user for an input
        userinput = input( '=========================\n|     AREA CALCULATOR v.0.1     | \n========================= \n\nFor CIRCLE area enter radius length and hit enter. \nFor SQUARE/RECTANGLE area enter high and length separated by comma. \nFor TRIANGLE area enter 3 lengths of its sides separated by commas. \nFor trapezoid area enter 4 lengths of its sides separated by commas. \n\nYour input: ' )

        # getting numbers from input
        numbers = [float( x ) for x in userinput.split( ',' )]

        if len( numbers ) == 1:

            # calculating circle area
            figure = 'circle'
            area = math.pi * numbers[0] ** 2

        elif len( numbers ) == 2:

            # checking is it a square or a rectangle
            if numbers[0] == numbers[1]:
                figure = 'square'
            else:
                figure = 'rectangle'

            # calculating area
            area = numbers[0] * numbers[1]


        elif len( numbers ) == 3:

            # calculating triangle area
            edge = 0
            for x in numbers:
                edge += x

            halfperimeter = edge / 2

            figure = 'triangle'
            area = math.sqrt( halfperimeter * ( halfperimeter - numbers[0] ) * ( halfperimeter - numbers[1] ) * ( halfperimeter - numbers[2] ) )

        elif len( numbers ) == 4:

            # calculating trapezoid area
            figure = 'trapezoid'

            a_plus_b = numbers[0] + numbers[1]
            b_minus_a = numbers[1] - numbers[0]
            c_pow = numbers[2] ** 2
            d_pow = numbers[3] ** 2

            big_part = c_pow - ( ( b_minus_a ** 2 + c_pow - d_pow ) / ( 2 * b_minus_a ) ) ** 2
            try:
                area = ( a_plus_b / 2 ) * math.sqrt( big_part )
            except ValueError:
                print( "No trapezoid with these dimensions." )

        else:
            print( 'Sorry, calculator cannot provide you the answer based on your input.' )


        # printing response
        print( 'The area of {} is {} square units.'.format( figure.upper(), round( area, 2 ) ) ) if area > 0 else print( 'Something went wrong...' )


    #===========================================================================
    # EXECUTION
    #===========================================================================
    area_calc()

# Copyright (c) 2016, Konstantin Chernukhin, All rights reserved.
# Created as a part of learning and practicing process.
#
# Author's url: http://octogear.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# IABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
