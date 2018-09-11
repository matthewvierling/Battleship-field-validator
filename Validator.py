# Battleship field validator funcion
# Currently not complete
#
# Matthew Vierling	9/10/2018
#


def validateBattlefield(field):
    
	visited = dict()

	#set all places as not being visited
	for i in range(len(field)):
		for j in range(len(field[i])):
			visited[str(i)+","+str(j)] = False

	for i in range(len(field)):

		for j in range(len(field[i])):

			#if not visited -- this is so no cells are double checked
			if visited[str(i)+","+str(j)] == False:

				#if contains ship part
				if field[i][j] == 1:

					#follow path
					#mark all in path as visited
					#if path not valid return false

					#when done with path, check if it is valid ship and marked it as used
					#if not valid ship or too many of that ship used return false
					pass

				else:
					visited[str(i)+","+str(j)] = True
				#end if
			#end if
		#end for
	#end for

	return True;

#end validateBattlefield


