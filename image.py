import mcbundle
# Modify this to make any art you want. Here I made Zalk's beautiful face.
images = {}
images["zelkam"] = [
	"OOOOOOOO",
	"O0OOOO0O",
	"OOOOOOOO",
	"OW0OO0WO",
	"OW0OO0WO",
	"WWW00WWW",
	"gWWWWWWg",
	"ggWWWWgg",
]

images["badboyhalo"] = [
	"00000000",
	"000RR000",
	"00R00R00",
	"0RW00WR0",
	"R000000R",
	"R000000R",
	"R000000R",
	"0R0000R0",
]

image_array = images["zelkam"]
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
