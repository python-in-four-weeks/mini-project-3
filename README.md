# Mini-Project 3: Library Administration

## Introduction

You have been tasked with completing a library admin website that some previous contractors left part-finished. The frontend is complete, as well as the book-related functionality, but the customer- and loan-related functionality is still to be completed.

## Setup

As usual, start by running `poetry install`. After you have done this, run `poetry run flask run` to start the API.

To run the frontend, install the Visual Studio Code **Live Server** extension, start the server, and navigate to the `index.html` file in the `frontend` folder in your browser.

## Endpoints to complete (10 points each)

### Customer endpoints

- `GET /`: this endpoint should allow you to view all customers from the database. It should handle an optional request query parameter, `search`, a fragment of a customer name, which you should use to restrict the search.
- `GET /<library_card_number>`: this endpoint should allow you to view a customer with a specific library card number.
- `POST /`: this endpoint should allow you to add a new customer to the database. It should handle two mandatory JSON properties, `name` and `email`. If either is not present, the endpoint should abort with a 400 error. If the email matches that of an existing account, the endpoint should abort with a 409 error. Otherwise, the endpoint should add a new customer with the given properties to the database and return the new customer.
- `PUT /<library_card_number>`: this endpoint should allow you to edit an existing customer in the database. Again, it should handle two mandatory JSON properties, `name` and `email`. If either is not present, the endpoint should abort with a 400 error. If the email matches that of an existing account (except for the existing one saved for the current customer), the endpoint should abort with a 409 error. Otherwise, the endpoint should update the customer with the given properties, save to the database and return the updated customer.
- `DELETE /<library_card_number>`: this endpoint should allow you to delete a customer from the database. It should return the deleted customer.

### Loan endpoints

- `GET /`: this endpoint should allow you to view all loans from the database. It should handle an optional request query parameter, `search`, a fragment of either a book title or a customer name, which you should use to restrict the search.
- `GET /<int:id>`: this endpoint should allow you to view a loan with a specific id.
- `POST /`: this endpoint should allow you to add a new loan to the database. It should handle two mandatory JSON properties, `book_id` and `customer_library_card_number`. If either is not present, the endpoint should abort with a 400 error. Otherwise, the endpoint should add a new loan with the given properties to the database and return the new loan.
- `PATCH /<int:id>`: this endpoint should allow you to edit an existing loan in the database. Again, it should handle one of two JSON properties, `renew` or `return`. If neither are present, the endpoint should abort with a 400 error. Otherwise, if the `renew` property is present, the loan's due date should be updated to two weeks from today, or if the `return` property is present, the loan's return date should be set to today. In either case, the endpoint should save to the database and return the updated loan.
- `DELETE /<int:id>`: this endpoint should allow you to delete a loan from the database. It should return the deleted loan.

Feel free to look at the already-completed book endpoints for inspiration.
