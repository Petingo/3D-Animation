from PIL import Image

folder_root = "nb"
frames = []
# load images in seq1:
for i in range(0, 91, 2):
    new_frame = Image.open(folder_root + '/seq1/Frame_%05d.bmp' % i)
    frames.append(new_frame)

frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)

for i in range(0, 91, 2):
    new_frame = Image.open(folder_root +'/seq2/Frame_%05d.bmp' % i)
    frames.append(new_frame)

frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)
frames.append(new_frame)

first_frame = frames[0]

# save into a GIF file that loops forever
first_frame.save(folder_root + '_1.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               optimize=True,
               duration=80, loop=0)