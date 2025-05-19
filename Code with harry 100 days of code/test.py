def welcome():
    print("hello this is the function of the welcome ")


print(__name__)
if __name__ == "__main__":
    welcome()

# __name__=="__main__" mean if the file run directly then this code will run
# but if the file is imported in another file then this code will not run
