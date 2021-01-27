# [Beauty Bounty]() - Milestone Project : Full Stack with Django - Code Institute

## Table Of Content

- [**About**](#About)
  - [**Why This Project**](#Why-This-Project)
- [**UX**](#UX)
  - [**User Stories**](#User-Stories)
  - [**Research**](#Research)
  - [**Wireframes**](#Wireframes)
  - [**Design**](#Design)
- [**Features**](#Features)
  - [**Functionality**](#Functionality)
  - [**Existing Feautures**](#Existing-Features)
  - [**Features Left To Implement**](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [**Languages**](#Languages)
  - [**Tools**](#Tools)
  - [**Libraries**](#Libraries)
  - [**Frameworks**](#Frameworks)
  - [**Database**](#Database)
  - [**Hosting**](#Hosting)
- [**Testing**](#Testing)
  - [**Browsers**](#Browsers)
  - [**Devices**](#Devices)
  - [**Testing User Stories**](#Testing-User-Stories)
  - [**Manual Testing**](#Manual-Testing)
  - [**Unresolved Bugs**](#Unresolved-Bugs)
  - [**Code Validation**](#Code-Validation)
- [**Deployment**](#Deployment)
  - [**Live App Link**](#Live-App-Link)
  - [**Repository Link**](#Repository-Link)
  - [**Running Code Locally**](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [**Content**](#Content)
  - [**Acknowledgements**](#Acknowledgements)
  - [**Media**](#Media)
  - [**Disclaimer**](#Disclaimer)

## About 
My online store sells only the best beauty products of the season from makeup, skincare and even fragrances. It's the place where beauty lovers visit to get inspired and purchase the hottest products out there, to make them look and feel their best! 

## Why This Project? 
This is an e-commerce store created for my 4th Milestone Project - Full Stack with Django for [Code Institute](https://codeinstitute.net/). My app allows users to search, view and purchase beauty products.

The front-end display and functionality uses HTML, CSS, JavaScript and the back-end functionality uses Python, Django and PostgresSQL.

## UX

### User Stories
As a user, I want to be able to:
* Look at all the app's products
* Search for a specific product
* Look into different product categories
* View product information
* View my cart item(s)
* Add a product to my cart
* Increase/Decrease the quantity of the product I am interested in purchasing
* Delete a product from my cart
* View order summary and total before proceeding with the payment
* Purchase the added cart item(s) with my credit card details
* Have a shipping or billing address option
* Get a confirmation when my payment goes through
* Get a notification if my payment doesn't go through
* Create my personal account
* Login/Logout of my personal account
* Contact costumer service via email or call
* Connect with the people of Beauty Bounty through social media 

### Research
I researched tutorials on e-commerse stores with Python and Django on [YouTube](https://www.youtube.com/) and [Udemy](https://www.udemy.com/), to get a general idea of the functionality that was needed to be implemented for this project. Most of my code was taken from Udemy's E-commerce Website Project.

### Wireframes
To create this project's wireframes I used [Balsamiq](https://balsamiq.com/).

During the development process some changes were made.

*
*
*

### Design
I wanted to keep my website clean, fresh and sophisticated. I used a lavender color for the navbar and footer to add some character but kept everything else white. Navbar brand and icons were given a deep almost black-looking purple. Typography is "Great Vibes" for the navbar brand and "Quicksand" for the body html code. 


## Features

### Functionality
The app is using Python logic to allow users to register or login/logout to their account for free. Users are also able to add item(s) to the cart and use their credit card to make a payment. That was achieved by installing and setting up Stripe. 

### Existing Features
- **Navbar** -
The navbar includes 5 links(categories) such as All Products, Brands, New, Best Sellers and Fragrances. Additionally it includes a user icon which will redirect user to a Register/Login page, a search icon which gives users the ability to search a specific product and a cart icon which redirects users to the checkout page.

- **Search** -
The search bar allows the user to type any word(s) related to the product they are searching for. If there's any product(s) corresponding to their search, the product(s) will appear in a separate page. If there's is no product corresponding to their search, a message will appear stating "No Products Found".

- **All Products** -
Users can view all the app's products both in-stock and out-of-stock by clicking on "All Products" in the navbar. The products are being displayed in an alphabetical order. Each product has an image, name, price and it's clickable so that users can see further details about the product they are interested in.

- **View Product** -
The user can click on a specific product to view product details. It will take the user to a new page where by the product name, price and description will be displayed. If the product is in-stock there will be an "Add To Cart" button which if clicked, will take the user to their cart, but if the product is out-of-stock there will be no action but a heading stating "Out Of Stock".

- **Cart** -
In the cart we have two sections. Items section and Checkout section. In the items section is the order summary. The products that were added to the cart by the user are being displayed along with their name, price and quantity set to 1 by default. However, the user is able to increase or decrease the quantity by clicking on the + or - icon accordingly, or delete the product from their cart by clicking on the bin icon. If the product is no longer in-stock, the + icon will disappear leaving the user with no choice of increasing the product quantity. The total of each product is being calculated next to it(eg. 100x1 = $100 or 100x3 = $300). On the checkout section the total amount of all products are being calculated and the user can proceed with the payment by clicking on the "Pay With Card" button. Once the button is clicked a form will appear where by the user will have to fill in personal information such as shipping or billing address and credit card details. 

- **Completed Order** -
If the payment goes through successfully, the user will be taken to the "Thank You" page. The "Thank You" page includes an images stating "Thank You for your order", the order number underneath the image and a "Continue Shopping" button.

- **User Profile / Order History** -
In the user profile there is an order history table with the orders number, data, amound spent, and action. In the action column is an anchor element "View Order".

- **Register** -
Users can create their own account for free by clicking on the user icon in the search bar which will take them to a page with register or login section. In the register section the user will have to click on the "Create New Account" button which will take them to the register page where by the user will have to fill a form with their personal details (Name, Surname, Username, Email Address, Password, Repeat Password). Once the form is correctly filled and the "Submit" button is clicked, a new account will be created. If the form is filled incorrectly (wrong password match) the user cannot continue and create an account.

- **Welcome Page** -
When a new account is successfully created the user will be taken to the Welcome page. In the Welcome page there is a "Hello Beautiful" image with a heading underneath stating "Welcome to Beauty Bounty!" and a "Start Shopping!" button. 

- **Login** -
Users can login in their account by clicking on the user icon in the search bar which will take them to a page with register or login section. The login form has a username and password field which if correctly filled the will be successfully logged in and taken to the home page.

- **Logout** -
Users and logout from their account by clicking on "Logout" in the navbar. Users will then be redirected to the register/login page.

- **Footer** -
The footer includes two sections. A contact section with a clickable email address which opens up an email form in a new tab and a phone number with a paragraph that shows operating hours. Plus a connect section with social media links.

## Features Left To Implement
- **Pagination**

 In the future, I would like to add pagination in my app to break the content into seperate pages for a more user-friendly experience.

- **Carousel Slide**

In the future, I would like to add a carousel slider to display makeup looks and ideas to inspire the page visitors.

- **Tutorials**

In the future, I would like to add a page with makeup/skincare tutorials from beauty experts sharing their beauty  tips & tricks and videos on how to use a specific makeup or skincare products that's available on the app!




### Testing

## Resolved
* -icons floating
* SECRET KEY EXPOSED! x2
* POSTGRES URI Exposed, destroyed database



* created cart - deleted database - reupload products
* sqlite3
* max product quantity

### Credits

## Code
* Dropdown menu was taken from [W3 Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover).
* Checkout code taken from Stripe
* Hide + code taken from slack overflow

## Media

## Acknowledgements
* Tutor Assistance
* Mentor
* Slack Overflow
