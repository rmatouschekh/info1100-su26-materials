# Assignment 1: Who's That?
# due Monday 06/29 at 9:00am (EST)

# Author: 
# NetID: 

import os
import errno

bio_path = input("Author Last Name: ").lower()

if not os.path.exists(os.path.join("bios", bio_path + ".txt")):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), bio_path)

with open(os.path.join("bios", bio_path + ".txt"), "r") as f:
    bio = f.read().strip()

print(bio)

print("") # Write your non-AI code here

print("\n#################### AI Generated – Required ####################\n")

# Write your required AI-generated code here

print("\n#################### AI Generated – Free Choice ####################\n")

# Write your free choice AI-generated code here