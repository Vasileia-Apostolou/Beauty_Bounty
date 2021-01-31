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
* View product information
* View my cart item(s)
* Add a product to my cart
* Increase/Decrease the quantity of the product I am interested in purchasing
* Delete a product from my cart
* View order summary and total before proceeding with the payment
* Purchase the added cart item(s) with my credit card details
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
I wanted to keep my website clean, fresh and sophisticated. I used a pink marble image for the navbar background to add some character and a lavender color to the footer, but kept everything else white. The same navbar background image was used for the reviews table. Navbar brand and icons were given a deep almost black-looking purple. For the free shipping banner I added a black background color to add contrast and a pink color for the text to match the color of the navbar. The buttons have the same background color and text color as the free shipping banner. Typography is "Great Vibes" for the navbar brand and "Quicksand" for the body html code. 

## Features

### Functionality
The app is using Python logic to allow users to register or login/logout to their account for free. Users are also able to add item(s) to the cart and use their credit card to make a payment. That was achieved by installing and setting up Stripe. 

### Existing Features
- **Navbar** -
The navbar includes 3 links such as Home, Products and Categories. Additionally it includes a user icon which will redirect user to a Register/Login page, a search icon which gives users the ability to search a specific product and a cart icon which redirects users to the checkout page.

- **Search** -
The search bar allows the user to type any word(s) related to the product they are searching for. If there's any product(s) corresponding to their search, the product(s) will appear in a separate page.

- **Products** -
Users can view all the app's products both in-stock and out-of-stock by clicking on "Products" in the navbar. The products are being displayed in an alphabetical order. Each product has an image, name, price and it's clickable so that users can see further details about the product they are interested in.

- **View Product** -
The user can click on a specific product to view product details. It will take the user to a new page where by the product name, price and description will be displayed. If the product is in-stock there will be an "Add To Cart" button which if clicked, will take the user to their cart, but if the product is out-of-stock there will be no action but a heading stating "Out Of Stock".

- **Review** -
The user can see reviews that other users have left. In order to post a review the user needs to have an account. If the user doesn't have an account, posting a review is not an option.

- **Cart** -
In the cart we have two sections. Items section and Checkout section. In the items section is the order summary. The products that were added to the cart by the user are being displayed along with their name, price and quantity set to 1 by default. However, the user is able to increase or decrease the quantity by clicking on the + or - icon accordingly, or delete the product from their cart by clicking on the bin icon. If the product is no longer in-stock, the + icon will disappear leaving the user with no choice of increasing the product quantity, and a "Out Of Stock" text will appear instead. The total of each product is being calculated next to it (eg. 100x1 = $100 or 100x3 = $300) depending on the quantity. On the checkout section the total amount of all products are being calculated and the user can proceed with the payment by clicking on the "Pay With Card" button. Once the button is clicked a form will appear where by the user will have to fill in personal information such as shipping or billing address and credit card details. 

- **Completed Order** -
If the payment goes through successfully, the user will be taken to the "Thank You" page. The "Thank You" page includes an images stating "Thank You for your order". Additionally, users who are registered and logged in can click on a link below where by it will redirect them to the order history page. Users who are not registered and logged in can click on a link below where by it will redirect them to the registration page.

- **User Profile / Order History** -
In the users profile there is an order history table with the orders number, data, amound spent, status and action. In the action column is an anchor element "View Order". Only users who are registered have access to their order history page. 

- **View Order**
In the "View Order" page there is a table with the order details.

- **Register** -
Users can create their own account for free by clicking on the user icon in the search bar which will take them to a page with register or login section. In the register section the user will have to click on the "Create New Account" button which will take them to the register page where by a form had to be filled in with their personal details (Name, Surname, Username, Email Address, Password, Repeat Password). Once the form is correctly filled in and the "Submit" button is clicked, a new account will be created. If the form is filled incorrectly (wrong password match) the user cannot proceed and create an account.

- **Welcome Page** -
When a new account is successfully created the user will be taken to the Welcome page. In the Welcome page there is a "Hello Beautiful" image with a heading underneath stating "Welcome to Beauty Bounty!" and a "Start Shopping!" button. 

- **Login** -
Users can login in their account by clicking on the user icon in the search bar which will take them to a page with register or login section. The login form has a username and password field which if correctly filled, the user will be successfully logged in and taken to the home page.

- **Logout** -
Users can logout from their account by clicking on "Logout" in the navbar. Users will then be redirected to the register/login page.

- **Footer** -
The footer includes two sections. A contact section with a clickable email address which opens up an email form in a new tab and a phone number with a paragraph that shows operating hours. Plus a connect section with social media links.

## Features Left To Implement
- **Pagination**

 In the future, I would like to add pagination in my app to break the content into seperate pages for a more user-friendly experience.

- **Carousel Slide**

In the future, I would like to add a carousel slider to display makeup looks and ideas to inspire the page visitors.

- **Categories**

In the future, I would like to add a navbar dropdown menu where by the users can see products based on their categories.

- **Best Sellers**

In the future, I would like to add a "Best Sellers" navbar item where by it will display the best selling products of Beauty Bounty.

- **New**

In the future, I would like to add a "New" navbar item where by it will display the all the new products that were added in Beauty Bounty.

- **Email Confirmation**

In the future, I would like to add a function that sends an order email confirmation to the email address that the user has provided.

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

### Browsers
This web application was tested in the following browsers to ensure the web application is compatible and responsive.
 * Chrome
 * Mozilla
 * Safari
 * Opera 
 * Internet Explorer

 ### Devices
 This web application was tested in the following devices to ensure the web application is compatible and responsive.
 * IPhone 8 Plus
 * Huawei P30 Pro 
 * Huawei Mediapad T5
 * MacBook Pro

### Testing User Stories
- **As a user, I want to be able to look at all the app's products**
1. Click on "Products" link on the navbar.

- **As a user, I want to be able to search for a specific product**
1. Type a word related to the product you are looking for.
2. Click on the "Search" button.

- **As a user, I want to be able to view product information**
1. Click on the product you would like to get more information about

- **As a user, I want to be able to view my cart item(s)**
1. Click on the cart icon in the navbar

- **As a user, I want to be able to add a product to my cart**
1. Click on the product you would like to add to your cart
2. Click on "Add To Cart" button

- **As a user, I want to be able to increase/decrease the quantity of the product I am interested in purchasing**
1. Click on the + icon if you want to increase the quantity

or

1. Click on the - icon if you want to decrease the quantity

- **As a user, I want to be able to delete a product from my cart**
1. Click on the bin icon if you want to remove the product from your cart

- **As a user, I want to be able to view order summary and total before proceeding with the payment**
1. Go to your cart

- **As a user, I want to be able to purchase the added cart item(s) with my credit card details**
1. Go to your cart
2. Click on "Pay With Card"
3. Fill in your personal information
4. Click "Pay"

- **As a user, I want to be able to create my personal account**
1. Click on the user icon in the navbar.
2. Click on "Create Account"
2. Fill in the Register Form with a username, email address and password.
3. Click on "Submit" button.

- **As a user, I want to be able to log in and out of my personal account.** 
* LOGIN 
1. Click on the user icon in the navbar.
2. Fill in the Login Form with your username and password.
3. Click on the "Login" button. 
* LOGOUT 
1. Click on the "Logout" link in the navbar.

- **As a user, I want to be able to contact costumer service via email or call.** 
1. Go to the bottom of the page
2. Contact phone number and email address are being displayed.
* Click on the email address to open a form

- **As a user, I want to be able to connect with the people of Beauty Bounty through social media.** 
1. Go to the bottom of the page
2. Social media links are being displayed and can be clicked

## Manual Testing

* I tested that the navbar brand(Beauty Bounty) redirects user to the home page.
* I tested that the navbar collapses to a hamburger menu in smaller screen devices.
* I tested that the search bar shows the user a product related to the word they typed.
* I tested the registration form by creating several fake user accounts with a username, email address, password and tested the "Submit" button.
* I logged in from several fake user accounts using the username and password and tested the "Login" button.
* I tested the log out funtion from all accounts by clicking on the "Logout" button.
* I tested that the about section is being displayed in the "Home" page.
* I tested that all "Go back" buttons takes user to the home page.
* I tested that "Products" link in the navbar takes user to the all products page.
* I tested that when a user clicks on a specific product, it takes them to the product details page.
* I tested that the "Add To Cart" button add the product into the users cart
* I tested that if the product has less than 200 in stock, a "Low In Stock" text will appear.
* I tested that if the product stock is 0, a "Out Of Stock" text will appear.
* I tested on the cart page, that if the "+" icon is clicked, the product quantity is increasing.
* I tested on the cart page, that if the "-" icon is clicked, the product quantity is decreasing.
* I tested on the cart page, that if the bin icon is clicked, the product quantity is being removed from the cart.
* I tested that the "Pay With Card" button brings up a form where the user has to fill in with personal details such as shipping/billing address and credit card details.
* I tested that when a payment goes through, a user is taken to a "Thank You For Your Order" page.
* I tested that in the "Thank You For Your Order" if the user is logged in, the user can click on "Click here to view order history" which will redirect to the "Order History" page.
* I tested that in the "Thank You For Your Order" if the user is logged out or not registered, the user can click on "To view order history click here to register" to register in order to view order history.
* I tested that in the "Order History" page the user can see the Order number, date, price, total amount spent, status and view order(action).
* I tested that in the "View Order" page the user can see order details.
* I tested that the "Print" button in the "View Order" page will give the user the option of printing/downloading the order details table.


### Resolved Bugs

- **Plus Icon**

In the cart page, when a product was reaching maximum in-stock quantity, the "+" icon was floating on top of the table. I realised that this was caused because in the else-block I haven't defined a table cell.

- **Secret Key Exposed** 

During the development proccess, I realised that I have exposed the stripe secret key, along with the database ProgresSQL URI. After I contacted tutor support, I have been advised to destroy the database and create a new one. As fas as the stripe key, I hide it in an env.py file and include it to the .gitignore file.




* POSTGRES URI Exposed, destroyed database
* created cart - deleted database - reupload products
* sqlite3
* max product quantity

### Unresolved Bugs 

- **Categories** 

In the navbar there is a "categories" element which is not functioning properly.

- **Stripe Billing Address** 

In the stripe payment form, the billing address section will not allow the user to proceed, instead it will automatically take them to the shipping address section. 



### Code Validators 
The web application's HTML and CSS code has been tested in [W3C Validator](https://validator.w3.org/). The JavaScript code has been tested in [JS Hint](https://jshint.com/). Python syntax has been tested in [Pep8 Online Tool](http://pep8online.com/) and responsiveness was tested in [Resposinator](https://www.responsinator.com/), [Am I Responsive](http://ami.responsivedesign.is/) and [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly).

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

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository](https://github.com/Vasileia-Apostolou/Beauty_Bounty)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env,py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```sudo pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

### Credits

## Code
* Dropdown menu was taken from [W3 Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover)
* Checkout code taken from [Stripe](https://stripe.com/en-dk)
* Navbar HTML code was taken from [Bootstrap](https://getbootstrap.com/)

## Media
None of the images belong to me.

* The project's products were taken from different online stores such as [Colorpop](https://colourpop.com/products/making-mauves-mauve-eyeshadow-palette), [Fenty Beauty](https://www.fentybeauty.com/), [Kylie Skin](https://kylieskin.com/), [Huda Beauty](https://hudabeauty.com/), [Valentino](https://www.valentino.com/en-no) and [Giorgio Armani](https://www.armani.com/dk/armanicom).
* Home Page image was taken from a [google search](https://www.google.com/search?q=lashes+gif&tbm=isch&ved=2ahUKEwip07iq7cTuAhXVOuwKHfS3CHMQ2-cCegQIABAA&oq=lashes+gif&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgYIABAHEB46CAgAEAcQBRAeUL-vAViKtgFg4LgBaABwAHgAgAFZiAHxApIBATaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=kfEVYOnGLdX1sAf076KYBw&bih=789&biw=834&rlz=1C5CHFA_enDK875DK875#imgrc=3cY72nhKokE9FM)
* Navbar background image was taken from a [google search](https://www.google.com/search?q=pink+and+gold+marble+background&tbm=isch&ved=2ahUKEwjLhaK27cTuAhUMs6QKHWzrCYcQ2-cCegQIABAA&oq=pink+&gs_lcp=CgNpbWcQARgAMgQIIxAnMgQIIxAnMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDOgIIAFCP6QNYyvADYO_9A2gAcAB4AIABV4gB0AKSAQE1mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=qvEVYMuIIYzmkgXs1qe4CA&bih=789&biw=834&rlz=1C5CHFA_enDK875DK875)
* "Thank you for your order" image was taken from a [google search](https://www.google.com/search?q=thank+you+for+your+order+&tbm=isch&ved=2ahUKEwiryobA8MTuAhVBtaQKHShXD5UQ2-cCegQIABAA&oq=thank+you+for+your+order+&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAUJQrWJQrYK8saABwAHgAgAE8iAE8kgEBMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=5PQVYKvIFsHqkgWorr2oCQ&bih=789&biw=834&rlz=1C5CHFA_enDK875DK875#imgrc=OT8KJGkAUvUJ7M)
* "Hello Beautiful* image was taken from a [google search](https://www.google.com/search?q=hello+beautiful+pink&tbm=isch&ved=2ahUKEwiG8bHD8MTuAhVEs6QKHQTPAS0Q2-cCegQIABAA&oq=hello+bea&gs_lcp=CgNpbWcQARgAMgQIIxAnMgQIIxAnMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEENQzcMEWJjPBGDq2wRoAHAAeACAAUiIAaYEkgEBOZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=6_QVYMbPFsTmkgWEnofoAg&bih=789&biw=834&rlz=1C5CHFA_enDK875DK875#imgrc=U-NPJr20WTz5TM)

## Acknowledgements
* Overall project and README file was inspired by [this](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/README.md#Deployment) project
* Most of this project's functionality was taken from [this Udemy course](https://www.udemy.com/course/build-ecommerce-website-to-master-django-and-python/learn/lecture/16779602?start=0#content)
* Code Institute's Tutor assistance has helped my a lot in solving and understanding the cause of the errors and issues I was facing
* Special thanks to my mentor Gerard McBride 
* [Slack Overflow](https://stackoverflow.com/) has been very helpful in solving errors

## Disclaimer
This project is for educational purposes only.
