import mcbundle
# Modify this to make any art you want. Here I made Zalk's face.
image_array = [
	"OOOOOOOO",
	"O0OOOO0O",
	"OOOOOOOO",
	"OW0OO0WO",
	"OW0OO0WO",
	"WWW00WWW",
	"gWWWWWWg",
	"ggWWWWgg",
]
image = "".join(image_array)
myArray = []
map = {
	"L": "lime",
	"G": "green",
	"0": "black",
	"M": "magenta",
	"B": "blue",
	"b": "light_blue",
	"R": "red",
	"P": "purple",
	"O": "orange",
	"W": "white",
	"Y": "yellow",
	"7": "brown",
	"G": "gray",
	"g": "light_gray",
	"C": "cyan",
	"p": "pink"
}
for o in range(len(image)):
	myArray.append(f"""{map[image[o]]}_stained_glass_pane""")
print(mcbundle.array_to_bundle_data(myArray))
