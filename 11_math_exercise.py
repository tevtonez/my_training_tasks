'''
Created on Feb 11, 2017
@author: kostya

TASK
Write a script that generates text file with math exercises that contain random numbers.
The exercises should contain addition, subtraction and multiplication.
The exercises should be put into txt file in 3 columns: first col - addition, second -
subtraction, third - multiplication.

The addition and subtraction exercises should look like:
[number from 1 to 99] + [number from 1 to 99] =
[number from 1 to 99] - [number from 1 to 99] =

The multiplication exercises should operate with numbers
[number from 1 to 99] * [number from 1 to 9] =
[number from 1 to 9] * [number from 1 to 99] =


EXTRAS:
1. generate a file with answers

'''
import random

if __name__ == '__main__':

    def gen_addition():
        '''Generates addition exercises'''
        exercise_addition = str( random.choice( range( 99 ) ) ) + " + " + str( random.choice( range( 99 ) ) ) + " ="
        return exercise_addition

    def gen_subtraction():
        '''Generates subtraction exercises'''
        exercise_subtraction = str( random.choice( range( 99 ) ) ) + " - " + str( random.choice( range( 99 ) ) ) + " ="
        return exercise_subtraction

    def gen_multiplicaction():
        '''Generates multiplication exercises'''

        while True:
            first_num = str( random.choice( range( 1, 99 ) ) )
            second_num = str( random.choice( range( 1, 99 ) ) )
            if int( first_num ) < 11 or int( second_num ) < 11:
                exercise_multiplicaction = first_num + " • " + second_num + " ="
                break
        return exercise_multiplicaction



    def gen_file( file_name = "math_exercises" ):
        '''Generates TXT file with math exercises'''

        file_name_answers = file_name + "_answers.txt"
        file_name += ".txt"

        # clearing answers file
        open( file_name_answers, 'w' ).close()


        print( "Generating ", file_name, "..." )
        with open( file_name, "w", encoding = "utf-8" ) as file:

            for _ in range( 25 ):

                addition = gen_addition()
                subtraction = gen_subtraction()
                multiplication = gen_multiplicaction()

                file.write( addition + "\t\t\t" + subtraction + "\t\t\t" + multiplication + "\n" )

                mult_list = multiplication[:-1].split( "•" )
                mult_res = int( mult_list[0] ) * int( mult_list[1] )

                # putting answers into txt file
                with open( file_name_answers, "a", encoding = "utf-8" ) as file_answers:
                    file_answers.write( str( eval( addition[:-1] ) ) + "\t\t\t" + str( eval( subtraction[:-1] ) ) + "\t\t\t" + str( mult_res ) + "\n" )







#===============================================================================
# EXECUTION
#===============================================================================

    gen_file()




#===============================================================================
# time spent: 34 min
#===============================================================================


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
