########### These are code snippets that need to be added to joywifi ##########
### This file will not run ###

### Add to Line 341 (just after # Get length of input string)
##### Print something on the screen to indicate there's more text to the left
                # Check if thestring is too long for the screen  ### NEWCODE ###
                if stringlength > 11:
                    oled_line_4 = 'Reached'


### Add to Line 510 (just after # Draw the selection box)
##### Manually set the x and y coordinates

                # Check if thestring is too long for the screen / display
                if stringlength > 11:  ### NEWCODE ###
                    selection_x1 = 85 
                    selection_y1 = 28
                    selection_x2 = 95
                    selection_y2 = 42


### Add to Line 532 (just before we draw all the text lines)
##### Only print the last X characters of the string

                # Check if thestring is too long for the display ### NEWCODE ###
                if stringlength > 11:
                    characters = -13
                    #string = "This is a string"
                    oled_line_3 = (oled_line_3[characters:])
                    #output: 'This'
