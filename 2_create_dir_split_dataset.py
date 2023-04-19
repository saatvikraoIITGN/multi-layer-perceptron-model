# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
# create directories
dataset_home = 'dataset_rats_vs_snakes/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	labeldirs = ['rats/', 'snakes/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
# seed random number generator
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.20
# copy training dataset images into subdirectories
src_directory = 'images'
for file in listdir(src_directory):
	src = src_directory + '/' + file
	dst_dir = 'train/'
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('rat'):
		dst = dataset_home + dst_dir + 'rats/'  + file
		copyfile(src, dst)
	elif file.startswith('snake'):
		dst = dataset_home + dst_dir + 'snakes/'  + file
		copyfile(src, dst)

# import os
# cwd = os.getcwd()
# print(cwd)