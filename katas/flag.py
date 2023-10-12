from swampy.World import World

# world = World()
# world.mainloop()
#
# canvas = world.ca(width=500, height=500, background='white')
# bbox = [[-150,-100], [150, 100]]
# canvas.rectangle(bbox, outline='black', width=2, fill='green4')


world = World()

# create a canvas and put a text item on it
ca = world.ca()
ca.text([0, 0], 'hello')

# wait for the user
#wait_for_user()
