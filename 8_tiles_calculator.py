'''
Created on Nov 24, 2016
@author: kostya

TASK
Write area calculator function that ask a user to provide the size of an area that
should be covered with ceramic tiles and the size of a ceramic tile and then
calculate the number of tiles needed to cover the area.

Possible output:

=========================
| Tiles CALCULATOR v.0.1 |
=========================

> Enter the area size in square units:
userinput - 20

> Now provide the length of a tile sides in units comma separated:
userinput - 0.1, 0.1

You'll need 200 tiles to cover 20 square units area.

'''
import math

if __name__ == '__main__':

    def tilecalc( area, list ):

        a = float( list[0] )
        b = float( list[1] )

        tile_area = a * b
        tile_num = int( area ) / tile_area

        print( "You'll need {} tiles to cover {} square units area.".format( math.ceil( tile_num ), area ) )

    #===========================================================================
    # EXECUTION
    #===========================================================================
    print( "\n=========================\n|     Tiles CALCULATOR v.0.1      |\n=========================\n\n" )

    while True:
        area = input( 'Enter the area size in square units: ' )
        if area.isdigit():
            break

    while True:
        ab_raw = input( 'You need to provide the length of TWO comma separated sides of a tile in units: ' )
        ab_list = ab_raw.split( ',' )

        if len( ab_list ) == 2:
            if ab_list[0].isdigit() and ab_list[1].isdigit():
                break

    ab_list = ab_raw.split( ',' )
    tilecalc( area, ab_list )



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
