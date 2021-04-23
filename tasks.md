## Next task
- Continue with the UI list on frontend
- Look for the words START HERE


## Everyday TDD
- refactor options
  - check code coverage
  - comment out any untested code
  - look at naming
  - use named parameters instead of positional
## Every time
- Onboard new person
  - env seup: install AnyDesk
  - project review
- Send name and github email in form: Co-authored-by: Ethan Strominger<ethanstrominger2@gmail.com> in Slack
- Review Ensemble (aka Mob) and TDD
  - [ ] Roles: Driver (Smart Keyboardist), Navigator (Conductor / Facilitator), and Team mates
  - [ ] Navigator sets direction, can ask for advice and team mates can indicate they have a suggestion
  - [ ] Rotate every 5-7 minutes
  - [ ] Quick retro to see if anything should be adjusted after every round
  - [ ] Leave 10 minutes at end for committing
- Identify who will be AnyDesk host and set up env

- Review what was done last session and if there is work remaining to do
## To Dos
- [ ] Investigaton
      - [ ] Look at what to install
      - [ ] Try PyCharm
- [ ] Technical debt / refactoring
      - [x] Python: Change way we do importing, explicity import, import from config.py
      - [ ] Check Daniel's code to maybe do more https://github.com/codeforboston/flagging
      - [ ] Flask/Python: Be in production mode, app.py
      - [ ] Create an src folder with __init__
      - [ ] Annotate routes - if we can get it to work easily
      - [ ] Environment:
        - [ ] Use git module, either make backend master repo 
        - [ ] Deployment
      - [ ] Identify where we are not modular
      - [ ] Blueprints?      
      - [ ] Figure out code coverage
      - [ ] Comment out untested code
      - [ ] Use named parameters instead of positional!
      - [ ] Set up guide in readme: how to deploy locally and in cloud
      - [ ] Add black, pytest, pytest-cov, pytest-watch to requirements.txt
      - [ ] Create test for route controller
- [ ] rename state to status in figma documentation
- [x] review create test and code
- [ ] adding an order: 
  - [x] test the create action
    - [x] When create an order with required attributes, auto generates a UUID.
  - [x] (just write the) controller & router : confirm a route calls the correct controller - started, needs to take more input.
  - [x] Manually build React UI for creating an order
    - [x] decide on mono-repo/server, multi-repo/server, or mono-repo/multi-server
      DECISION: mutil-repo/server
      - Pros
        - mono-repo/server: easier to keep synchronized, easier to deploy at least locally, don't need to worry about CORS
        - multi-repo/server: more flexible for changing UI or db later, frontend / backend distinction more obvious, can be deployed separately on different servers, may be easier to set up in Heroku
        - mono-repo/multi-server: easier to keep synchronized while allowing for future flexiblity
    - [x] implement screen for creating orders using https://bezkoder.com/react-hooks-crud-axios-api/ (substitute tutorials for orders)
- [ ] Change SQLAlchemy to JSON
- [ ] Getting the QR code:
  - Create test that `Util.getQRCode('any_string')` returns PNG for the qr code from `?root_url:/show/any_string` route (we can build on early Feb experiment)
  - Create test for OrderTransactions: when you add a order there is a QR code attribute on the order.
  - Create a test that `OrderTransactions.getOrderByID(ordernumber).qrCode` returns the PNG of the QR code including the order's corresponding UUID.
  - Manually build and test UI for specifying an order number and displaying the qr code so that you can print it.
- [ ] getting list of orders
  - [x] create test for OrderTransactions.getAll()
  - [x] create controller and router
  - [x] create UI to list orders, all attributes except QR code
-  START HERE https://getbootstrap.com/docs/4.0/content/tables/
  - [ ] Make it look user friendly 
  - [ ] when click on an order, see the QR code
- [ ] create status codes and descriptions + getAllStatusCodes()
  - model actions (create, read, update, delete)
    - test when create several statusses (StatusCodeActions.create), then StatusCodeActions.getAll() returns those statusses
    - test when create several statusses, then StatusCodes.getDescription(statusCode) returns the description
  - controller and router for creating and getting statusses
  - UI for listing and creatng statusses
- update status
  - create test for OrderTransactions.updateStatus(order_number, status)
  - create controller and router
  - review UI for scanning and updating status
  - consider status being a drop down - only a few, scanning two codes is cumbersome
  - UI:
    - when call get ??root_url:/show/<order.id> you see a drop down for statusses and order id is displayed
    - when submit, update status
- query database on multiple criteria

### Later / authorization tests

- tests for admin authorization
- tests for update status authorization
- tests and UI for creating and getting all attributes for an order
- tests and UI for creating with invalid attributes
- tests and UI for updating order
- tests filtering order by multiple parameters
- tests create order with invalid US state

### Low Priority Tasks


