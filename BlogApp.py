from flask import Flask, render_template, redirect, request
from butter_cms import ButterCMS
 
blogs = Flask(__name__)
 
client = ButterCMS('c3c37caed6eaa3141e464fc82cab8f83cae7925f')
 
@blogs.route("/") #For default route
def main():
 
   
    blog = client.posts.all()
    data = blog['data']
 
    return render_template("BlogList.html",  homepage = data)
#defining viewblog route
@blogs.route("/viewblog", methods = ['GET', 'POST'])
def viewBlog():
   #using Flask’s args property to get ‘slug’ parameter from BlogList.html
    slug = request.args.get('slug')
    fullblog = client.posts.get(slug)
    Fulldata = fullblog['data']
    print(Fulldata)
    
 
    return render_template("Fullblog.html", blogpage = Fulldata)
   
if(__name__ == "__main__"):
    blogs.run()