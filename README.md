# Django-Spring-2021
 
## LAB 5 -- *continuation of the past lab*
* added some links
  * auth_\login\
  * auth_\signup\   
* added api views (viewsets)
  * todos/                     ---> all todo lists (GET, POST)
  * todos/<int:pk>/            ---> todo list retrieve (GET, POST, PUT, DELETE)
  * tasks/                     ---> all todo tasks (GET, POST)
  * tasks/<int:pk>/            ---> todo task retrieve (GET, POST, PUT, DELETE)
  * todos/<int:pk>/tasks/      ---> todo tasks in todo list (GET)
  * todos/<int:pk>/completed/  ---> todo completed tasks in list (GET)
  * auth_/login                ---> to get jwt token for authenticate
  * auth_/signup               ---> to create user



## LAB 4 -- *continuation of the past lab*
 
* added some links for convenient use
  * All Todos
  * Links 1
  * Links 2 
* you should write manually \completed to register, since it was not asked to add onclick event to Completed_Tasks
  * Example: todos\1\completed 
* all data replaced to database Postgresql, added modules
  * Lists
  * Tasks
* added filters, search, ordering to admin panel

![image](https://user-images.githubusercontent.com/51375666/109455847-b28eb980-7a81-11eb-93f9-37ffbdb59b59.png)

