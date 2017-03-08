'''
Created on Mar 8, 2017
@author: kostya

TASK
Write a function that creates a JSON file from a given dictionary that contains writers' names and their birthdays.
Then write another function that opens a JSON file and prints out all key/values pairs.
'''

import json

bd_dict = {
    "Anne McCaffrey": "April 1, 1926",
    "Ursula K. Le Guin": "October 21, 1929",
    "George Orwell": "June 25, 1903",
    "J. R. R. Tolkien": "January 3, 1892",
    "Jules Verne": "February 8, 1828",
    "Marion Zimmer Bradley": "June 3, 1930",
    "Terry Pratchett": "April 28, 1948",
    "Ray Bradbury": "August 22, 1920",
    "C. S. Lewis": "November 29, 1898",
    "Roger Zelazny": "May 13, 1937"
}

def save_to_json( dictionary ):
    with open( 'task_14_bd_dictionary.json', 'w' ) as json_file:
        json.dump( dictionary, json_file )

    print( 'File saved!' )


def read_from_json( file ):
    with open( file, 'r' ) as json_file:
        load_from_json = json.load( json_file )
        for k, v in load_from_json.items():
            print( k, v )




if __name__ == '__main__':


    file = "task_14_bd_dictionary.json"

    save_to_json( bd_dict )
    read_from_json ( file )



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
