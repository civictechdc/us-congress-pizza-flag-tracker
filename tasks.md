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
  - [ ] Rotate every 5 minutes
  - [ ] Quick retro to see if anything should be adjusted after every round
  - [ ] Leave 10 minutes at end for committing
- Identify who will be AnyDesk host and set up env

- Review what was done last session and if there is work remaining to do
## To Dos
- [ ] Investigaton
      - [ ] Look at what to install
      - [ ] Try PyCharm
- [ ] Technical debt
      - [ ] Figure out code coverage
      - [ ] Comment out untested code
      - [ ] Use annotation for routing
      - [ ] Use named parameters instead of positional
      - [ ] Set up guide: how to installl environment
      - [ ] Add black, pytest, pytest-cov, pytest-watch to requirements.txt
      - [ ] Create test for route controller
- [ ] rename state to status in documentation
- [x] review create test and code
- [ ] adding an order: 
  - [x] test the create action
    - [x] When create an order with required attributes, auto generates a UUID.
  - [ ] (just write the) controller & router : confirm a route calls the correct controller - started, needs to take more input.
  - [ ] Manually build React UI for creating an order
    - [ ] decide on mono-repo/server, multi-repo/server, or mono-repo/multi-server
      - Pros
        - mono-repo/server: easier to keep synchronized, easier to deploy at least locally, don't need to worry about CORS
        - multi-repo/server: more flexible for changing UI or db later, frontend / backend distinction more obvious, can be deployed separately on different servers, may be easier to set up in Heroku
        - mono-repo/multi-server: easier to keep synchronized while allowing for future flexiblity
    - [ ] proposal: If going with one respository, follow https://dev.to/arnu515/build-a-fullstack-twitter-clone-using-flask-and-react-1j72 skipping authentication and use order entity rather than tweet entity
    - [ ] proposal if going with two: use https://bezkoder.com/react-crud-web-api/
- [ ] Getting the QR code:
  - Create test that `Util.getQRCode('any_string')` returns PNG for the qr code from `?root_url:/show/any_string` route (we can build on early Feb experiment)
  - Create test for OrderTransactions: when you add a order there is a QR code attribute on the order.
  - Create a test that `OrderTransactions.getOrderByID(ordernumber).qrCode` returns the PNG of the QR code including the order's corresponding UUID.
  - Manually build and test UI for specifying an order number and displaying the qr code so that you can print it.
- [ ] getting list of orders
  - create test for OrderTransactions.getAll()
  - create controller and router
  - create UI to list orders, all attributes except QR code
  - when click on an order, see the QR code
- create status codes and descriptions + getAllStatusCodes()
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

### Later / authorization tests

- tests for admin authorization
- tests for update status authorization
- tests and UI for creating and getting all attributes for an order
- tests and UI for creating with invalid attributes
- tests and UI for updating order
- tests filtering order by multiple parameters
- tests create order with invalid US state

### Tests That Are Done:

### Low Priority Tasks

- consider passing an object rather than positional for create

### Retro format

##### Sunday Mar 12
- Learned
  - UUID
  - Git Stash
- Liked
  - AnyDesk
  - Refactoring to remove stuff
  - Quickly re-creating db
  - Class method do the work rather than the database
- Proposals for doing differently next time
  - Create a shell file for each step of recreating db (e.g. wipedb.sh `rm flag.db && rm -rf migrations/`)
  - 7 minutes, if 2 or 3 people
  - 4 people, 5 minutes

  ##### Wed Mar 17
  - Learned
    - Rajinder learned routes, POST vs. GET in routes
    - Thad thought about how SQLAlchemy works and remembered Flask POST details.
    - Ethan refreshed on how POST works.
  - Liked
    - Postman
    - Getting the hang of hosting AnyDesk
    - Wednesday night
    - Not as much facilitation needed by Ethan
  - Proposal for doing differently next time
    - Thad would like to eat before hacking
    - Ethan would like to join the group