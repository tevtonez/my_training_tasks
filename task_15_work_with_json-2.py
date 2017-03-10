'''
Created on Mar 8, 2017
@author: kostya

TASK 15
Update the code from TASK 13 so user would be able to add new pair 'Name' : 'birthday date'
and add it to existing JSON file.

Bonus for adding new pair without loading full JSON file!

'''

import json

def save_to_json( dictionary ):
    with open( 'task_14_bd_dictionary.json', 'w' ) as json_file:
        json.dump( dictionary, json_file )

    print( 'File saved!' )

def read_from_json( file ):
    '''reads from JSON file to screen'''
    with open( file, 'r' ) as json_file:
        load_from_json = json.load( json_file )
        for k, v in load_from_json.items():
            print( k, '-', v )

def add_to_json( name, bd_date, file ):
  '''adds new name:bd pair to JSON file'''

  with open( file, 'r+' ) as js_file:
    js_file.seek( 0, 2 )  # put cursor to the end of the file
    js_file.seek( js_file.tell() - 1, 0 )  # shifting cursor to one position left
    js_file.write( ', "' + name + '": "' + bd_date + '"}' )



if __name__ == '__main__':


    file = "task_14_bd_dictionary.json"
    print( 'The current JSON file contains next data:\n' )
    read_from_json ( file )

    while True:

      user_input = input( "\n\nType 'add' if you want to add a new Birthday Date to the file\nType 'quit' to quit the program.\n\n" )

      if user_input == 'add':

        name = input( "Enter a name: " )
        bd_date = input( "Enter birthday date: " )

        # adding a new birthday date
        add_to_json( name, bd_date, file )

        # read from file again to show the results
        print( "\nNow we have next people on the list:\n" )
        read_from_json ( file )


      elif user_input == 'quit':
        # finishing the app
        break







#===============================================================================
# time spent: 6 min
#===============================================================================


# Copyright (c) 2017, Konstantin Chernukhin, All rights reserved.
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
