with open("ex.txt","w") as f:
    f.write("Welcome\nThis is example file\nThanks for your attention")
with open("ex.txt","a") as f:
    f.write("\nUsing 'a' mode to add a text to end")