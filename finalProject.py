from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}



#/restaurants page 
@app.route('/', methods=['GET', 'POST'])
@app.route('/restaurants/', methods=['GET', 'POST'])
def showRestaurants():
	return render_template('restaurants.html', restaurants=restaurants)


#/restaurants/new page 
@app.route('/restaurants/new/', methods=['GET', 'POST'])
def newRestaurant():

	if request.method == 'POST':
		restaurant['name'] = request.form['name']
		restaurant['id'] = str(int(restaurants[len(restaurants)-1]['id']) + 1)
		restaurants.append(restaurant)
		for i in range(len(restaurants)):
			print (str(restaurants[i]))
		return redirect(url_for('showRestaurants'))
	else: 
		return render_template('newrestaurant.html')

#/restaurants/restaurant_id/edit 
@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['POST','GET'])
def editRestaurant(restaurant_id):
	currentRestaurant = ""
	for i in range(len(restaurants)):
		if restaurants[i]['id'] == str(restaurant_id):
			currentRestaurant = restaurants[i]
	if request.method == 'POST':
		for i in range(len(restaurants)):
		 	if restaurants[i]['id'] == str(restaurant_id):
				restaurants[i]['name'] = request.form['name']		
				return redirect(url_for('showRestaurants'))
	else:
		return render_template('editrestaurant.html', restaurant_id=restaurant_id, currentRestaurant=currentRestaurant)


#/restaurants/restaurant_id/delete
@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
	if request.method == 'POST':
		radioButtonAnswer = request.form.getlist('deleteSelection')
		print radioButtonAnswer
		print type(radioButtonAnswer[0])
		if radioButtonAnswer[0] == u'no':
			print "radioButtonAnswer = no"
			return redirect(url_for('showRestaurants'))
		else:
			print "radioButtonAnswer = yes"
			for i in range(len(restaurants)):
				if restaurants[i]['id'] == str(restaurant_id):
					restaurants.pop(i)
					return redirect(url_for('showRestaurants'))
	else: 
		return render_template('deleteRestaurant.html', restaurant_id=restaurant_id)



#/restaurants/restaurant_id
#/restaurants/restaurant_id/menu 
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
	return "This page is the menu for restaurant %s" % restaurant_id


#/restaurants/restaurant_id/menu/new
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
	return "This page is for making a new menu item for restaurant %s" % restaurant_id

#/restaurants/restaurant_id/menu/menu_id/edit 
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
	return "This page is for editing menu item %s in restaurant %s" % menu_id, restaurant_id

#/restaurants/restaurant_id/menu/menu_id/new
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/new/')
def deleteMenuItem(restaurant_id, menu_id):
	return "This page is for deleting menu item %s in restaurant %s" % menu_id, restaurant_id



if __name__ == '__main__':
	app.debug = True 
	app.run(host='0.0.0.0', port=5000)
