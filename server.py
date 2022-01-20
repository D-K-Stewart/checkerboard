from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')          
def eight():
    
    return render_template('index.html', num=8, sum=8)  

@app.route('/4')          
def four():
    
    return render_template('index.html', num=4, sum=8)

@app.route('/<int:num>/<int:sum>')          
def index(num,sum):
    
    return render_template('index.html', num=num, sum=sum)



# @app.route('/play/<sum>')                           
# def playground2(sum):
#     return render_template('index.html', num=int(sum), tempColor="lightblue")

# @app.route('/play/<sum>/<color>')
# def playground3(sum, color):
#     return render_template('index.html', num=int(sum), tempColor=color)





#KEEP THIS AT THE BOTTOM!
if __name__=="__main__":       
    app.run(debug=True)   