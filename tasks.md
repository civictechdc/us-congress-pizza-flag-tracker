## Next task

- Tasks to do between sessions
    - [] Auth (FLASK SESSIONS?) Start over chat
    - [] Componentizing the front end to not repeat ourselves (DRY)
    - [x] Finish the tests
    - [] Entering the states.js into offices table automatically.
    - [] Pull states & offices from server
    - [] Flag statuses mockup with static data?
    - [] Flag statusses from backend (requires some more elaboration)
    - [] Figure out why getting CORS errors instead of 500 errors
    - [x] Disabling button if errors
    - Improve state / office UI 

- Discuss MVP

  - Update orders and see the status of the order
  - when you scan the qr code
    - see the order (today)
    - update the status
    - it gives you a prompt to update?
  - report and queries that we haven't thought about
  - do we need any additional attributes of orders?
  - security (people adding/updating/deleting the orders, but also ppl updating the status)

- report out from flag reform meeting on thoughts from Ananda and co.
- PyCharm IDE
- Fix populating data when click on edit - create new route for get_by_uuid

## Everyday TDD

- refactor options
  - check code coverage
  - comment out any untested code
  - look at naming
  - use named parameters instead of positional

## Every time

- Onboard new person
  - env setup: install AnyDesk
  - project review
- Send name and github email in form: Co-authored-by: Ethan Strominger <ethanstrominger2@gmail.com> in Slack
- Review Ensemble (aka Mob) and TDD
  - [ ] Roles: Driver (Smart Keyboardist), Navigator (Conductor / Facilitator), and Team mates
  - [ ] Navigator sets direction, can ask for advice and team mates can indicate they have a suggestion
  - [ ] Rotate every 5-7 minutes
  - [ ] Quick retro to see if anything should be adjusted after every round
  - [ ] Leave 10 minutes at end for committing
- Identify who will be AnyDesk host and set up env

- Review what was done last session and if there is work remaining to do

## To Dos

- [ ] Investigation
- [ ] Look at what to install
- [ ] Technical debt / refactoring -
  - [x] Python: Change way we do importing, explicitly import, import from config.py
  - [ ] - [ ] Check Daniel's code to maybe do more https://github.com/codeforboston/flagging
  - [ ] - [ ] Flask/Python: Be in production mode, app.py - [ ] Create an src folder with **init** - [ ] Annotate routes - if we can get it to work easily - [ ] Environment:
  - [ ] - [ ] Use git module, either make backend master repo
  - [ ] - [ ] Deployment
  - [ ] - [ ] Identify where we are not modular - [ ] Blueprints?
      - [ ] Figure out code coverage - [ ] Comment out untested code - [ ] Use named parameters instead of positional! - [ ] Set up guide in readme: how to deploy locally and in cloud - [ ] Add black, pytest, pytest-cov, pytest-watch to requirements.txt - [ ] Create test for route controller
  - [ ] Add tests for order num endpoint
  - [ ] Add comments for code thats currently commented out and dead code(And get it to work!!) (db.relationships in particular)
  - [ ] Console.log
  - [ ] Search by title -> search by order number
  - [ ] remove unneccessary import of dropbox
  - [ ] Combobox https://reach.tech/combobox/
- [x] rename state to status in figma documentation
- [x] review create test and code
- [ ] adding an order:
  - [x] test the create action
    - [x] When create an order with required attributes, auto generates a UUID.
  - [x] (just write the) controller & router : confirm a route calls the correct controller - started, needs to take more input.
  - [x] Manually build React UI for creating an order
    - [x] decide on mono-repo/server, multi-repo/server, or mono-repo/multi-server
          DECISION: multi-repo/server
      - Pros
        - mono-repo/server: easier to keep synchronized, easier to deploy at least locally, don't need to worry about CORS
        - multi-repo/server: more flexible for changing UI or db later, frontend / backend distinction more obvious, can be deployed separately on different servers, may be easier to set up in Heroku
        - mono-repo/multi-server: easier to keep synchronized while allowing for future flexibility
    - [x] implement screen for creating orders using https://bezkoder.com/react-hooks-crud-axios-api/ (substitute tutorials for orders)
- [x] Change SQLAlchemy to JSON
- [ ] QR code:
  - [x] Review pull request for test for `get_QRCode('any_string')` returns PNG for the qr code for `'any_string'`
    - [x] Tests and implements route for qr_code that includes a parameter for the string
  - Resource: https://stackoverflow.com/questions/26363613/how-to-test-send-file-flask
  - [x] Ask ethan about "data = request.args.get("value", uuid)" from controllers.py
  - [ ] create an environment variable for <frontendBaseURL> in backend
  - [ ] Modify above test that the QR code returns `<frontendBaseURL>/status/<uuid>` where root_url is read from an env variable
  - [x] Create a button in the UI that calls route for generating qr code with UUID as a parameter
  - [x] QR code return http://localhost:3000/orders/uuid
  - [x] Display the order when above is entered
  - [x] Review pull request for test for `get_QRCode('any_string')` returns PNG for the qr code for `'any_string'`
    - [ ] Run and fix the tests
- [ ] Explore deploying the app frontend/backend for QR code demo
  - [x] Set up https://codefordc-flag.herokuapp.com/
  - START HERE
  - [ ] Get Postgres working with the app deployed on Heroku
  - [x] Un-hard code and reference environment variable <frontendBaseURL> of the frontend inside QR code.
- [ ] Screen for changing status
  - [ ] React: Create React route for `(https://localhost:3000/)show?id=<uuid>` that fetches details for the specified order
  - [ ] Add a hard coded drop down list (temporary)
  - [ ] Add a Submit button that calls backend route for updating status (see update status below)
- [x] getting list of orders
  - [x] create test for OrderTransactions.getAll()
  - [x] create controller and router
  - [x] create UI to list orders, all attributes except QR code
  - [x] Make it look user friendly
  - [x] When an order is clicked, the order details are shown
  - [x] when click on an order, see the QR code
  - [x] Create tests for updated orders
  - [x] Create update functions
  - [ ] When an order is edited, the order details are shown (resolve the 404 on /orders/uuid)
  - [ ] When an order is edited and published, changes persist (update/put request)
- [ ] Screen for changing status
  - [ ] React: Create React route for `(https://localhost:3000/)show?id=<uuid>` that fetches details for the specified order
  - [ ] Add a hard coded drop down list (temporary)
  - [ ] Add a Submit button that calls backend route for updating status (see update status below)
- [ ] create status codes and descriptions + getAllStatusCodes()
  - model actions (create, read, update, delete)
    - test when create several statuses (StatusCodeActions.create), then StatusCodeActions.getAll() returns those statuses
    - test when create several statuses, then StatusCodes.getDescription(statusCode) returns the description
  - controller and router for creating and getting statuses
  - UI for listing and creating statuses
- update status
  - create test for OrderTransactions.updateStatus(order_number, status)
  - create controller and router
- query database on multiple criteria

### Later / authorization tests
- table for us_states/congressional offices for those states, and on front-end change free text to dropdown for all options (AJAX).
- tests for admin authorization
- tests for update status authorization
- tests and UI for creating and getting all attributes for an order
- tests and UI for creating with invalid attributes
- tests and UI for updating order
- tests filtering order by multiple parameters
- tests create order with invalid US state

### Low Priority Tasks
