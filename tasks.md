To Do:
- test adding an order: 
  - controller
    - When create an order with required attributes, then it gets saved to the database and auto generates an id
    - Refactor: move add logic to a controller, change test to call the controller
  - route
    - when call route with required attributes the posted values get sent to create order
  - Manually build and test UI for creating an order
- test getting qr code 
  - function returns 
  - controller: verify get includes qr code and in format root_url:/update/<qr_code>
  - route
  - Manually build and test UI for viewing a specific order and seeing the qr code and scanning the qr code
- update status
  - controller - when update status of specified order, the order is updated
  - route
  - 
  

Done:
