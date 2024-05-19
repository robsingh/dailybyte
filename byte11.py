'''
You are on the command line of a computer in the root directory and given a list of commands to run. 
The commands consist of three possible operations, 
../ which brings you to the parent directory (or nowhere if you’re already in the root directory), 
./ which keeps you in the current directory, 
and directory_name/ which moves you to a new directory with the specified name (these named directories are guaranteed to always exist). 
After running all the commands, return the amount of commands required to bring you back to the root directory.
Note: The commands must be run in the order they appear in commands.

Ex: Given the following commands…

commands = ["a/", "b/"], 
return 2 (we've gone two directories deeper, so we must go backwards two directories which requires 2 commands).
Ex: Given the following commands…

commands = ["a/", "../"], return 0.



'''