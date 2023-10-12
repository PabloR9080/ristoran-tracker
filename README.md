# Restaurant API

This project was developed as a test for backend-developer role

> Main link: https://ristoran-api.onrender.com

This api contains a jwt factor to authenticate, there are more details in the postman collection to get the credentials.

# Routes

## API
### Restaurants
All of the routes in this representation are prefixed with the HTTP method.

<code>GET /api/v1/restaurant</code>

Retrieve a full list of the restaurants with the id, name, street, phone, email and positional details.


<code>POST /api/v1/restaurant</code>

Create a new resource, require all the fields defined by the model of <i>Restaurant</i>

<code>GET /api/v1/restaurant/{id}</code>

Retrieve a more detailed description of a Restaurant.

<code>PUT /api/v1/restaurant/{id}</code>

UPDATE one or more existent fields for a existent Restaurant.

<code>DELETE /api/v1/restaurant/{id}</code>

Delete a Restaurant with the given id.

<code>GET /api/v1/restaurant/statistics?latitude=x&longitude=y&radius=z</code>

Get a subset of the Restaurants that are within the range of the raidus z of the point x,y.
Returns the average rating of the subset, the count and the standard deviation of the ratings.

## Token
For this route you would need a super user on the application.

<code>POST /api/token/</code>

The main route to get the acces token. You would need credentials of the api.

<little> Developed with  🐍  by pablorosas </little>
