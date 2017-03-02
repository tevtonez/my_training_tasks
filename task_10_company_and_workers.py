'''
Created on Feb 08, 2017
@author: kostya

TASK
Create a class 'Company' that contains objects of 2 classes of workers
that derived from parent class 'Worker': 'Manager' and 'Engineer'.
Workers should have fields: 'name', 'job_title' 'office_number', 'project'.
'Company' class should have methods: 'ShowManagers', 'ShowEngineers',
'ShowAll'. These methods should print the lists of related objects.

'''
from abc import ABCMeta, abstractmethod

if __name__ == '__main__':


    class Worker( metaclass = ABCMeta ):
        """represents any worker in the company"""

        def __init__( self, name, office_number, project ):
            self.name = name
            self.office_number = office_number
            self.project = project

        @abstractmethod
        def show_info( self ):
            """shows info about object"""

            print( "Name: {},\tOffice: {},\tProject: {};".format( self.name, \
                    str( self.office_number ), self.project ), end = "\t" )



    class Manager( Worker ):

        def __init__( self, name, office_number, project, job_title = "Manager" ):
            Worker.__init__( self, name, office_number, project )
            self.job_title = job_title

        def show_info( self ):
            """shows info about Manager"""
            Worker.show_info( self )
            print( "Job title: {}".format( self.job_title ) )



    class Engineer( Worker ):

        def __init__( self, name, office_number, project, job_title = "Engineer" ):
            Worker.__init__( self, name, office_number, project )
            self.job_title = job_title

        def show_info( self ):
            """shows info about Engineer"""
            Worker.show_info( self )
            print( "Job title: {}".format( self.job_title ) )


    class Company():

        list_of_workers = []

        def __init__( self ):
            """
            Populates Company object list with workers objects
            """
            worker1 = Manager( 'John', 33, 'IRC_3' )
            worker2 = Engineer( 'Vika', 23, 'IRC_3' )
            worker3 = Engineer( 'Dave', 33, 'IRC_3' )
            worker4 = Engineer( 'Ted', 23, 'Bubblez' )
            worker5 = Manager( 'Tom', 21, 'Bubblez' )
            worker6 = Engineer( 'Ella', 21, 'Bubblez' )

            self.list_of_workers.extend( [worker1, worker2, worker3, worker4, worker5, worker6 ] )

        def ShowAll( self ):
            """
            Displays all workers in the Company
            """
            print( "Showing all workers:\n" )
            for worker in self.list_of_workers:
                worker.show_info()


        def ShowManagers( self ):
            """
            Displays all Managers in the Company
            """
            print( "Showing all Managers:\n" )
            for worker in self.list_of_workers:
                if worker.job_title == "Manager":
                    worker.show_info()


        def ShowEngineers( self ):
            """
            Displays all Engineers in the Company
            """
            print( "Showing all Engineers:\n" )
            for worker in self.list_of_workers:
                if worker.job_title == "Engineer":
                    worker.show_info()


    #===========================================================================
    # EXECUTION
    #===========================================================================

    company = Company()  # Creating a company with workers
    company.ShowAll()  # Showing all workers
    print( "\n\n" )
    company.ShowManagers()  # Showing all Managers
    print( "\n\n" )
    company.ShowEngineers()  # Showing all Engineers

#===============================================================================
# time spent: 40 min
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
