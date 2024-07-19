from flask import Flask
app=Flask(__name__)
@app.route("/")
def Favourite_Person():
    return "<div><center><h1 style='background:red'>Nature</h1></center><p><strong>Nature's </strong>beauty is a profound source of inspiration and solace, offering an endless array of landscapes and ecosystems that captivate our senses and nurture our spirits. From the tranquil serenity of lush forests and the vibrant colors of blooming wildflowers to the majestic grandeur of towering mountains and the rhythmic ebb and flow of ocean tides, nature's wonders are both vast and varied. These natural marvels not only provide breathtaking aesthetics but also play a crucial role in sustaining life on Earth, regulating the climate, and supporting a diverse array of flora and fauna. As we immerse ourselves in nature's splendor, we are reminded of our intrinsic connection to the environment and the imperative to protect and preserve these precious ecosystems for future generations.</p></div>"
if __name__=="__main__":
    app.run(debug=True)