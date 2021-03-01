# Pizza-API

<!-- <p> -->

###### Stored Data regarding Pizza in the following fashion:-

1. Pizza type (Cannot be changed): Regular or Square
2. Pizza size (Changable): (Default sizes) Small, Medium, Large,
3. Pizza Toppings(Changable): Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno

###### API response requirements

1. API endpoint to create regular pizza and a square pizza
2. API endpoint which lists the information about all the stored pizza
3. filtering the list based on Size & Type of Pizza
4. API endpoint that allows the user to edit or delete any pizza from the database

#### Configurations

DB-NAME: PizzaAppDatabase
Collection-NAME: PizzaAppCollection

#### Steps for running the project

1. Create & run a virtualenv

```
virtualenv env
source env/Scripts/activate ---> bash on windows
source env/bin/activate     ---> Linux
```

2. Install the requirements
   `pip install requirements.txt`
3. Install and MongoDB atlas on your local
4. move into the app-directory
   `cd pizza_site/`
5. run the server

```python manage.py runserver

```

# API guide

1.  api/pizza
    ==> you will get a list of pizza and also can create
2.  api/pizza/<pk:id>
    ==> detail page where you can do RUD(Read, update, delete)
3.  api/size
    ==> perform create
    <strong>Although it was mentioned that only Small/Medium/Large size are present but if you want to create another size, the api can utilize that.</strong>
4.  api/topping
    ==> you will get a list of toppings and also can create
5.  api/topping/<pk:id>
    ==> update the name of the topping

 <!-- ```
{
    "name":"Jalapeno popers",
    "pizza_shape": "SQUARE",
    "pizza_size": "LARGE",
    "pizza_topping": ["Tomato", "Corn", "Jalapeno"]
}
{
    "name":"Jalapeno popers",
    "pizza_shape": "SQUARE",
    "pizza_size": 3,
    "pizza_topping": [2, 3, 6]
}
Pizza.objects.create(
   name="Jalapeno popers",
    pizza_shape="SQUARE",
    pizza_size= Size.objects.get(id=3),
    pizza_topping=[2, 3, 6]
)
``` -->
