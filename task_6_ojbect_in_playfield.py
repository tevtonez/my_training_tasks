'''
Created on Nov 24, 2016
@author: kostya

TASK
Using function from the task 5 create a play field. Then create a function that places a
"player" (any character that is different from the field's background) in a x, y position.
Note: the top left matrix cell has (1, 1) coordinates.

EXAMPLE
x = 2
y = 2
char = x

Possible output:
****
*x**
****


'''

if __name__ == '__main__':

    def Matrix( x, y, char ):

        # forming line
        line = x * char

        # forming matrix
        matrix = [line for i in range( y )]
        return matrix

    def Player( matrix, x, y, char ):

        y -= 1
        x -= 1

        # replacing matrix's background symbol with char
        temp_line = [i for i in matrix[y]]
        temp_line[x] = char

        # putting matrix back together
        temp_str = ''.join( temp_line )
        matrix[y] = temp_str

        for l in matrix:
            print ( l, end = '\n' )



    #===========================================================================
    # EXECUTION
    #===========================================================================
    matrix = Matrix( 5, 5, '.' )
    Player( matrix, 4, 3, 'x' )

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
