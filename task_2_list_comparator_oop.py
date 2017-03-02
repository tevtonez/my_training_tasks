'''
Created on Nov 18, 2016
@author: kostya

TASK
Create a function that takes one argument 'litsts_length' which is equals
10 by default, creates 2 list with length = 'litsts_length', then shuffles list
items in both lists and then compares list items one by one finding matching numbers
and then prints number of occurred coincidences and numbers that matched.

USE OOP this time!
Make sure it works for uneven lists!

EXAMPLE
For lists
a = [2, 0, 3, 4, 1, 7, 5, 6, 9, 8]
b = [7, 5, 2, 9, 1, 0, 3, 6, 4, 8]

output should be:
3 coincidence(s) for number(s) 1, 6, 8

'''

if __name__ == '__main__':

    import random

    class MyList:
        """Class that defines shuffled list object with default length 10

        Parameters:
            listlenght (int): A parameter with default argument value 10 that specifies a
                              length off the list.

        Attributes:
            itemslist (list): Contains shuffled list.
        """

        def __init__( self, listlenght = 10 ):
            self.listlenght = listlenght
            self.itemslist = [i for i in range( self.listlenght )]

            random.shuffle( self.itemslist )



    def Comparator( list1, list2 ):
        """ This takes two lists with integers as arguments then compares each element
        of the lists and returns a list of the numbers which indices matched

        Parameters:
            list1, list2 (list): Parameters that can take values of list of integers.
        """
        matches_list = []
        matches_count = 0
        for i in list1:
            if list1[i] == list2[i]:
                matches_count += 1
                matches_list.append( list1[i] )

        return matches_list


    #===========================================================================
    # EXECUTION
    #===========================================================================

    # Creating lists objects
    l1 = MyList( 21 )
    l2 = MyList( 12 )

    # printing lists
    print( 'Created lists:\nlist 1 = {}\nlist 2 = {}\n'.format( l1.itemslist, l2.itemslist ) )

    # Running comparator
    if len( l1.itemslist ) < len( l2.itemslist ):
        resulting_list = Comparator( l1.itemslist, l2.itemslist )
    else:
        resulting_list = Comparator( l2.itemslist, l1.itemslist )

    # printing comparison results
    if len( resulting_list ) != 0:
        equals_str = ', '.join( str( e ) for e in resulting_list )
        print( '{} coincidence(s) for number(s) {} found! YAY!'.format( len( resulting_list ), equals_str ) )

    else:
        print ( 'There are no coincidences in numbers, sadly.' )


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
