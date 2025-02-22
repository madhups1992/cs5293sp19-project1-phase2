import pytest
import project1_phase2
from project1_phase2 import unredactor

def tests_():
    text = """
Story of a man who has unnatural feelings for a pig. 
Starts out with a opening scene that is a terrific example of absurd comedy.
A formal orchestra audience is turned into an insane, violent mob by the crazy chantings of it's singers. 
Unfortunately it stays absurd the WHOLE time with no general narrative eventually making it just too off putting. 
Even those from the era should be turned off. The cryptic dialogue would make Shakespeare seem easy to a third grader. 
On a technical level it's better than you might think with some good cinematography by future great Vilmos Zsigmond. 
Future stars Sally Kirkland and Frederic Forrest can be seen briefly.
"""
    
    red = unredactor.redaction(text,['and','a man','the'])
    assert len(red[1])>0
