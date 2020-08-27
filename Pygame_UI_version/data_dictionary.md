Variable name | Data type | Descripton
HEIGHT | Integer | The height of the screen, in pixels
WIDTH | Integer | The width of the screen, in pixels
window_surface | Record (Class) | The window itself 
background | Record (Class) | The background
manager | Record (Class) | Manages all events
end | Boolean | Starts as false, used to quit the program when the x pressed
dest | string | The 'Destination' of this loop. Which function will be called.
event | Record (Class) | A pygame Event, used to check what has been done.
clock | Record (Class) | A pygame Clock, used in the pygame_gui module to update the screen, and used in the 'Memorise.py' screen to track the time
objects | Dictionary of Records (Classes) and list | Used to store all the objects on the screen
time_delta | floating point number | Shows the time between frames
help_text | text | the entirety of the content of the help page
tot_score | Integer | the total score of a game
rnd | Integer or string | the score of a round or the 'Destination' to be sent back to 'Main.py'
disp | string | The 'Destination' sent back down to 'Main.py'
characters | string | a list of all characters that can be in this game
out | string/int | the variable to be returned
mem | string | the value returned from 'Memorise.py'
rep | string | the value returned from 'Repeat.py'
positions | list of tuples of tuples | strores the positions for the characters
timer | float | used to time the memorise stage, updated when the 'clock' variable ticks
orig | list | used when updating the onscreen timer
pos | integer | position of the character in the string/list
out_c | string | the character to be outputted
typ | string | the type of character that the referenced dropdown is set to
arrow_btn_pos | list of integers | the x positions of the arrow buttons 
drpdn_pos | list of integers | the x positions of the dropdowns
group | Dictionary of Records (Classes) | group of items (up arrow, down arrow, dropdown, character)
arp | list | variable returned form 'arrow_pressed'
drp | list | variable returned form 'dropdown_changed'
up_button | Record (Class) | an up button object
dn_button | Record (Class) | an down button object
dropdown | Record (Class) | a character type dropdown
home_btn | Record (Class) | a home button
help_btn | Record (Class) | a help button