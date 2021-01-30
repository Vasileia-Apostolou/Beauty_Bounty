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

* [Home](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Home%20Page.pdf)
* [All Products](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/All%20Products.pdf)
* [Product Details](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Product.pdf)
* [Cart](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Cart.pdf)
* [Completed Order](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Thank%20You.pdf)
* [Order Details](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Order%20Details.pdf)
* [Register/Login](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Register:Login.pdf)
* [Search](https://github.com/Vasileia-Apostolou/Beauty_Bounty/blob/master/store/static/wireframes/Search.pdf)

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

## Technologies Used

### Languages
1. [HTML](https://en.wikipedia.org/wiki/HTML)

HTML was used in this project to keep up with the latest industry standards. 

2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

CSS was used for styling the content.

3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

JavaScript was used to create the main functional logic of this app. 

4. [Python](https://en.wikipedia.org/wiki/Python_programming_language)

Python was used as the back-end programming language for this app.

### Tools
1. [Git](https://git-scm.com/)

Git was used in this project for version control.

2. [Gitpod](https://www.gitpod.io/)

Gitpod was used to develop this project.

3. [Balsamiq](https://balsamiq.com/)

Balsamiq was used to create the wireframes.

4. [Dev Tools](https://developers.google.com/web/tools/chrome-devtools)

Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools can help you edit pages on-the-fly and diagnose problems quickly, which ultimately helps you build better websites, faster. Google Chrome's Dev Tools was used in the building process of this project.

### Libraries 
1. Icons were obtained from [Font Awesome](https://fontawesome.com/).

2. Fonts were taken from [Google Fonts](https://fonts.google.com/).

3. [Bootstrap](https://getbootstrap.com/) classes were used to build the navigation bar and to make the website responsive.

### Frameworks 
1. [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

2. [jQuery](https://jquery.com/) is a fast, small, and feature-rich JavaScript library. It was used in this project to simplify the DOM.

### Hosting 
* [Heroku](https://www.heroku.com/) was used as the hosting platform to deploy this app.

## Testing

### Resolved
* -icons floating
* SECRET KEY EXPOSED! x2
* POSTGRES URI Exposed, destroyed database
* created cart - deleted database - reupload products
* sqlite3
* max product quantity

## Deployment

### Live App Link 
Click the link below to run my project in the live environment:

* [Beauty Bounty](https://beauty-bounty.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

* [Beauty Bounty Repository](https://github.com/Vasileia-Apostolou/Beauty_Bounty)

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `.bashrc` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and pasted all of the `.bashrc` default variables in Heroku's Config Vars section.
7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in the `.bashrc` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.
8. Went to the **S3** section of AWS and created a new S3 bucket.
9. Within the relevant bucket's permissions, changed the **CORS Configuration** to the following:

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

10. Still in the **S3** section, changed the **Bucket Policy** to the following:

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<my-bucket-name>/*"
            }
        ]
    }
    ```

11. Replaced the `<my-bucket-name>` in the `Resource` line with my S3 bucket's name instead.
12. Went to the **IAM** section of AWS, created a 'New Group' and attached my S3 bucket details to it.
13. Still in the **IAM** section, created a 'New Policy' and a 'New User' and attached these to the newly created group.
14. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    ```

15. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
16. Updated the `settings.py` file with the relevant configuration for static and media file storage.
17. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
18. Created a requirements.txt file using the following command in the terminal window:

    ```sudo pip3 freeze --local > requirements.txt```

19. Created a Procfile using the following command in the terminal window:

    ```echo web: gunicorn UnicornAttractor.wsgi:application > Procfile```

20. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.
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
