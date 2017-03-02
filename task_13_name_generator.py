'''
Created on Mar 2, 2017
@author: kostya

TASK
Write a function that asks user for desired name length and for quantity of names to be generated.
Print out the names at the end.
'''

import random, string

vowels = 'aeiouy'
consonants = 'bcdfghklmnpqrstvwxz'
any_letter = string.ascii_lowercase

def generator():
  '''Asks user for length and quantity of names to be generated'''
  name_length = input( "Enter the length of name: " )
  quantity = input( "Enter how many names you need: " )

  name_structure = ""

  for i in range( int( name_length ) ):
    letter_input = input( "Enter 'v' for vowel, 'c' for consonant, 'l' for any letter, or any other letter to use it in name: " )
    name_structure += letter_input

  for n in range( int( quantity ) ):
    name = ""
    for l in name_structure:
      if l == 'v':
        name += random.choice( vowels )

      elif l == 'c':
        name += random.choice( consonants )

      elif l == 'l':
        name += random.choice( any_letter )

      else:
        name += l

    print ( name )


if __name__ == '__main__':

  generator()


#===============================================================================
# time spent: 15 min
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
