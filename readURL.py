import requests

class readURL():
    def __init__(self, Url):
        if "drive.google.com" in  Url:
            Url_LHS = Url
            Url_LHS = Url_LHS.split("file")
            Url_RHS = Url_LHS.pop()
            Url_LHS = "".join(Url_LHS)
            Url_LHS = Url_LHS + "/u/0/uc?id="
        #____________________________________
            Url_RHS = Url_RHS.split("/d/")
            Url_RHS.pop(0)
            Url_RHS = "".join(Url_RHS)
            Url_RHS = Url_RHS.split("/view")
            Url_RHS.pop()
        #____________________________________

            Url_RHS = "".join(Url_RHS)
            self.complete_Url = Url_LHS + Url_RHS + "&export=download"
            print(self.complete_Url)

        elif "www.dropbox.com" in Url:
            Url_LHS = Url
            Url_LHS = Url_LHS.split("www.dropbox.com")

            Url_RHS = Url_LHS.pop()
            Url_RHS = "".join(Url_RHS)

            Url_LHS = "".join(Url_LHS)
            Url_LHS = Url_LHS + "dl.dropboxusercontent.com"

            self.complete_Url = Url_LHS + Url_RHS
        
        else:
            print("\nError, cloud storage service not supported\nCurrently supported cloud services:\n\t1-Google Drive\n\t2-Dropbox\n")


    def read_Url_file(self, Tag):
        variable_str = requests.get(complete_Url)
        f = open("{Tag}.pm","wb") #Note: Should we implement an option to choose name of file?
        f.write(variable_str.text.encode())
        f.close()

a =readURL()
a.__init__("https://www.dropbox.com/s/ym1t42y0kzj9702/gogo.txt?dl=0")
a.read_Url_file("new")
print(a)
#-----------------------------------------------------------------



#----------------------------------------------------------

# https://www.dropbox.com/s/ym1t42y0kzj9702/gogo.txt?dl=0 ///// for testing purposes

# https://drive.google.com/file/d/16ZtePsjn4F0yXYwlVbn1h-eGWEiGWxGG/view   //// for testing purposes

# https://www.RandomCloudStorage/file/d/16ZtePsjn4F0yXYwlVbn1h-eGWEiGWxGG/view  ////// for testing purposes

# cloud_storage_directLink_maker() ////// for testing purposes

# read_Url_file(Tag)    ////// for testing purposes