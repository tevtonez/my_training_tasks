'''
Created on Nov 21, 2016
@author: kostya

TASK
Write a function that takes three arguments:
- Number of citizens in the city
- The disease spreading speed from one person to another (in hours)
- The number of people that get infected from the one infected person

Then function should calculate in which time the whole population of the city will be infected.

For example, we have a city with 300,000 people and one infected person (which is called
"patient zero") at the beginning.
Let's say the spreading speed of this disease is 24 hours and the number of people that will be
infected by contacting the "patient zero" in 24 equals 2. Then each of the infected people will
infect 2 more people in 24 hours and so one.
The function should say in how many hours the whole city will fall if no counter measures are
taken.

OUTPUT EXAMPLE
"The city with the population of 300,000 people will be 100% infected in 96 hours if disease
spreading speed is 2 persons in 24 hours"

'''

if __name__ == '__main__':

    def Zombify( population = 30, hours = 24, spreading = 2 ):
        """
        This takes 3 arguments 'population' (int), 'hours' (int), 'spreading' (int)
        and calculates the time that is needed to infect whole 'population' if disease
        speed is 'spreading'/'hours'.

        """

        infection_time = 0
        infected = 1
        time_unit = 'hours'

        # calculating time
        while infected < population:
            infected += infected * spreading + infected
            infection_time += hours

        # transforming hours into days
        if infection_time > 72:
            time_unit = 'days'
            infection_time = infection_time / 24

        print( 'The city with the population of {} people will be 100% infected in about {} \
{} in case of disease spreading speed {} persons per {} hours'.\
        format( population, infection_time, time_unit, spreading, hours ) )


    Zombify( 30, 24, 2 )

#===============================================================================
# time spent
# without graphics: 10 min
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
