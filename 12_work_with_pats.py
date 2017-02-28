'''
Created on Feb 27, 2017
@author: kostya

TASK(s)

1. print full path of your working directory.
2. write a script that creates a directory 'test1' in your working directory. Make script to ignore if the directory exists.
3. write a script that creates a sub-directory in 'test1'. Name it 'test2'. Make script to ignore if the directory exists.
4. write a script that creates 5 files in sub-directory 'test1'. Name files test-1-[n].txt , where [n] is the number from 1 to 5.
5. write a script that prints the number of all items in 'test1' directory.
6. write a script that iterates through files only and changes their names to test-[n].txt , where [n] is the number from 1 to 5. Also print new names.
7. write a script that deletes all directories and files you've created during previous steps. Be careful when working on this task!

'''

if __name__ == '__main__':

#===============================================================================
# EXECUTION
#===============================================================================
    import os, os.path, shutil


    # sub task 1
    print ( os.getcwd() )

    # sub task 2
    my_work_dir = os.getcwd()
    dir = my_work_dir + '/test1'
    print( dir )

    os.makedirs( dir, exist_ok = True )

    # sub task 3
    dir2 = '/test2'
    dir += dir2
    print( dir )
    os.makedirs( dir, exist_ok = True )

    # sub task 4
    dir = my_work_dir + '/test1'
    for i in range( 5 ):
        with open( dir + '/test-1-' + str( i + 1 ) + '.txt', 'w' ) as file:
            pass

    # sub task 5
    print( "\nThere are {} items in the 'test1' directory.\n".format( len( os.listdir( dir ) ) ) )

    # sub task 6
    files_in_dir = os.listdir( dir )
    counter = 1
    path_part = dir + '/'
    for file in files_in_dir:
        if not file.startswith( '.' ) and os.path.isfile( dir + '/' + file ):
            new_name = 'test-' + str( counter ) + '.txt'
            os.replace( path_part + file, path_part + new_name )
            counter += 1
            print( new_name )

    # sub task 7
    print( "We'll delete this: ", dir )
    shutil.rmtree( dir )
    print( dir, "is removed sucessfully." )




#===============================================================================
# time spent: 45 min
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
