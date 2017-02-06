'''
Created on Nov 24, 2016
@author: kostya

TASK
Create a function that takes three arguments 'x' (int), 'y' (int) and 'char' (str) and prints
a play field 'x'-width, 'y'-high filled with 'char's

EXAMPLE
x = 4
y = 3
char = *

output:
****
****
****


'''

if __name__ == '__main__':

    def Matrix( x, y, char ):

        line = x * char
        matrix = [line for i in range( y )]

        for l in matrix:
            print ( l, end = "\n" )

    #===========================================================================
    # EXECUTION
    #===========================================================================

    Matrix( 19, 14, 'x' )

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
