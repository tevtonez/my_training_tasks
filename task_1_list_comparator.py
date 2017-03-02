'''
Created on Nov 18, 2016
@author: kostya

TASK
Create a function that takes one argument 'lists_length' which is equals
10 by default, creates 2 lists with length = 'lists_length', then shuffles list
items in both lists and then compares list items one by one finding matching numbers
and then prints number of occurred coincidences and numbers that matched.

EXAMPLE
For lists
a = [2, 0, 3, 4, 1, 7, 5, 6, 9, 8]
b = [7, 5, 2, 9, 1, 0, 3, 6, 4, 8]

output should be:
3 match(es) for number(s) 1, 6, 8

'''

if __name__ == '__main__':

    import random
    def Comparator( lists_length = 10 ):
        """this finds coincidences in 2 even randomized lists 'l1' and 'l2' and prints
        out comparison for every element in the lists and summary in the end"""

        equals_count = 0
        equals_list = []
        equals_str = ''

        # creating the lists
        l1 = [item for item in range( lists_length )]
        l2 = [item for item in range( lists_length )]

        # shuffling list items
        random.shuffle( l1 )
        random.shuffle( l2 )

        # iterating through lists
        for i in range( len( l1 ) ):

            if l1[i] == l2[i]:
                equals_count += 1
                equals_list.append( l1[i] )

        # printing lists
        print( 'Created lists:\nlist 1 = {}\nlist 2 = {}\n'.format( l1, l2 ) )

        # printing comparison results
        if equals_count != 0:
            equals_str = ', '.join( str( e ) for e in equals_list )
            print( '{} coincidence(s) for number(s) {} found! YAY!'.format( equals_count, equals_str ) )

        else:
            print ( 'There are no coincidences in numbers, sadly.' )

    #===========================================================================
    # EXECUTION
    #===========================================================================
    Comparator()


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
