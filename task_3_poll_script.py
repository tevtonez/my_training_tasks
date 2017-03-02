'''
Created on Nov 18, 2016
@author: kostya

TASK
Create a script that asks user a question with 3 possible answers: "Yes", "No", "Maybe".
The results should be written in a log file with the date and time of line creation.
Once log file contains 10 or more lines script should show total number of votes and
percentage for every answer.
Do not use modules math or course or similar. Write everything you need manually

OUTPUT EXAMPLE
Question: Do you think it's a good script?
YES - 30%
NO - 20%
MAYBE - 50%

You may want to create a graphic representation of percentage using some UTF symbols (eg
u25A8 and u25A2

'''

if __name__ == '__main__':

    import time, collections

    #===========================================================================
    # EXECUTION
    #===========================================================================

    # question itself
    question = "Do you think it's a good script? (Yes, No, I don't know)\n"

    # asking user for an answer
    answer = input( question ) + "::" + time.asctime( time.localtime() ) + '\n'
    # writing answer into file
    with open( "3_poll_results.txt", "a", encoding = "utf-8" ) as poll_result_file:
        poll_result_file.write( str( answer ) )


    # showing polls results:
    print( "\nPolls results:" )

    # iterating through file
    with open( "3_poll_results.txt", "r", encoding = "utf-8" ) as poll_result_file:
        poll_answers_l = [line for line in poll_result_file]

        if len( poll_answers_l ) >= 10:

            # making a list of answers:
            all_lines_l = [line.split( '::' ) for line in poll_answers_l]

            # count answers
            cnt = collections.Counter()
            for item in all_lines_l:
                cnt[item[0].lower()] += 1

            # calculating averages
            total_values = sum( cnt.values() )

            for k, v in cnt.items():
                k_percentage = v * 100 / total_values
                print ( "{} - {}%".format( k.upper(), round( k_percentage ) ) )
                print ( "{}{}".format( u'\u25A8' * int( k_percentage ), u'\u25A2' * ( 100 - int( k_percentage ) ) ) )

        else:
            print( '\nNot enough data to display.\nNeed {} answers more.\n'.format( 10 - len( poll_answers_l ) ) )




#===============================================================================
# time spent
# without graphics: 70 min
# with percentage bars 75 min
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
