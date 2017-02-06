'''
Created on Dec 19, 2016
@author: kostya

TASK
Write a HTML parser using HTMLParser and urllib.request that parses
the content from a given website and prints the content of all
headers on the page and the URLs of all <a> tags.

=========================
website parser v.1
=========================

> Enter website ULR (with http:// part):
http://razrisovki.ru/

> The headers on the page are:
> Hello World
> How to learn Python
> Contact me
>
> The URLs on the page are:
> http://google.com
> http://gmail.com
> http://yahoo.com

'''


if __name__ == '__main__':

    import urllib.request, re, sys
    from html.parser import HTMLParser


    class MyHTMLParser( HTMLParser ):

        parsed_text = ''
        headers_tags_list = ['h1', 'h2']

        def handle_starttag( self, tag, attrs ):

            if tag == 'a':
                if attrs[0][0] == 'href':
                    url_value = attrs[0][1]
                    MyHTMLParser.parsed_text += '<' + ''.join( tag ) + '>' + '##' + ''.join( url_value ) + '##'

            else:
                MyHTMLParser.parsed_text += '<' + ''.join( tag ) + '>'

            return MyHTMLParser.parsed_text

        def handle_data( self, data ):

            MyHTMLParser.parsed_text += ''.join( data )
            return MyHTMLParser.parsed_text

        def handle_endtag( self, tag ):
            MyHTMLParser.parsed_text += '</' + ''.join( tag ) + '>'
            return MyHTMLParser.parsed_text

    #===========================================================================
    # EXECUTION
    #===========================================================================


    user_url = input( 'Enter website ULR (with http:// part):\n' )
    with urllib.request.urlopen( user_url ) as html:

        text_html = ''
        for line in html.readlines():
            text_html += ''.join( line.decode( 'utf-8' ) )

        parser = MyHTMLParser()
        parser.feed( text_html )

        # print ( parser.parsed_text )

        p_headers = re.compile( r'<h\d>(\w+)</h\d>' )
        headers_text = p_headers.findall( parser.parsed_text )

        p_urls = re.compile( r'#{2}(.*)#{2}' )
        url_text = p_urls.findall( parser.parsed_text )


        if headers_text:
            print ( '\nThe headers on the page are:' )

            for header_text in headers_text:
                print( header_text )

        else:
            print( 'There are no headers on the page.\n' )


        if url_text:
            print ( '\nThe URLs on the page are:' )

            for url in url_text:
                print( url )
        else:
            print( '\nThere are no URLs on the page.\n' )


    print( "That's it folks" )
    sys.exit()



#===============================================================================
# time spent: 80 min
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
