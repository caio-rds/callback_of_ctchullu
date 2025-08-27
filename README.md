# The Call<span style="opacity:0.5">back</span> of C'tchullu

### What is it about?
> **Restful API** using *Python* (**FastAPI**) and *MongoDB*.

This project is a simple example of how to create a RESTful API using FastAPI and MongoDB.
You can use it as a starting point for your own projects or just to learn how an API works.

### Why this API returns URLs instead of the data itself or IDs?
> - Because it is a RESTful API, and in RESTful APIs, resources are identified by URLs.
> - This way, you can easily navigate through the API by following the URLs.
> - Also, it is a good practice to return URLs instead of IDs or data itself, as it makes the API more flexible and easier to use.
> - For example, if you want to get the details of a character, you can simply follow the URL returned in the character's data.
> - This way, if the character's data changes, you don't need to change the URL, as it will always point to the correct resource.
> - This is known as HATEOAS (Hypermedia As The Engine Of Application State), and it is a key principle of RESTful APIs.

## *Project is inspired in **[SWAPI](https://swapi.bry.com.br/).***