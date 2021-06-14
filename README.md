# MSP4 Lee's Burger KItchen (LBK)

![Screenshot](static/images/)

This is the Website for [Lee's Burger Kitchen(LBK)](). Which is an online burger delivery site. 

The purpose of this site is to use everything learnt from all the modules of the Full Stack Developer Course and create a Full Stack 
Django Framework project that includes the accessing, manipulating and displaying data retrieved from a relational database. 
The Website utilises a PostGres database together with Python code to access and manipulate the data. 

HTML, CSS and Javascript were used to help assist the Django frameworks with the visualization of the data. The site utilises the UI feature called Stripe which allows online payments.

------

# User Experience (UX)

## User stories
### Common user stories (guests, new users and authenticated users)

As a User....
*  I expect to access the website from any device, so that I can use the website anytime and anywhere.
*  I expect to easily navigate the website, so that I can quickly find what I'm looking for.
*  I want to find an information about the company, to know what they do, what their main principles and ideas
*  I want to see the location of the LBK.
*  I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
*  I want to view all available products.
*  I want to view product details (e.g. image, price, description, ingredients), so that I can make an informed decision before I buy.
*  I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
*  I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
*  I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
*  I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
*  I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.


### New Users
As a new user....
* I want to create my own account, so that I can save, view and edit my profile details and view my order history.

### Returning users
As a returning user....
*  I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
*  I want to reset my password if I forgot it, so that I can get access to my profile again.
*  I want to be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.
*  I want to be able to change my email.
 
### Website Owner(admin)
As a Site owner....
*  I want to secure admin interface avalable only for website admin, so that I can add, edit and remove products.
*  I want to be able to view orders recieved  for that day and update the order status.
*  I want to be able to differentiate between active orders and completed orders for the day.
*  I want to be able to view history of all orders recieved.   

## Design

### Frameworks

- Bootstrap, front-end framework was chosen for this project for its ease of use and ability to be easily customized. 
It was used for creating features such as navbar, cards, forms, modals, as well as for the layout.
- JQuery is used for initializing some Bootstrap components.

### Colour Scheme

The main goals of UI is to focus the user's attention on the product images therefore simple greys, whites and blacks where used to create
a clean and neat background. 


### Typography 
    
The Font Barlow Condensed was used from google fonts accross the site as its a clean and simple font.

### Icons
        
Icons from fontawesome where used throughout the site as the grab the users attention. They create a more user-friendly experience for 
users as they give visual clues about the subject. Icons used across the project for social media links, forms, cart, search bar and the 
navigation are similar to what the user would see in other sites giving them a sense of familiarity.

### Imagery  

The main image has been chosen to be eye catching and gives the user a clear indication of what the website is about.
The other images have been choosen to highlight the product in an appealing light.  
    
    
## Wireframes:
The [LBK](docs/LBK.pdf) wireframes can be found here.
 
------

# Features

## Existing Features

* Home page - The homepage welcomes users to the site with a hero image, text and place order button which indicaates the purpose of the site. further down the page the user can find sections about our burgers, about us, our ingredients, and reviews section. Each section contains, imagery relavant to the section, a brief but informtive narative about the section and a button to take user to that view. 
* Our Burgers - Our Burgers gives a brief explanation about our burgers with a button to the menu page.
* About Us - The about us page gives users a little story of who we are, why we are different, delivery info and costs and contact details.
* Our Suppliers - Our suppliers page gives users breif narrative about our ingredients and providers with links to their sites.
* User Reviews - The reviews page has a brief narrative informing the users that these are customers reviews of LBK and displays the reviews in a accordian style list displaying review title and date of review the drop down reveals the review, rating, user name, and date. Users are encouraged to click and add review. 
* Add review - When users click to add a review they are asked to sign in or register if not already, the user name is displayed at the tom and they are asked to leave a title, select a rating from 1 to 5 and leave a comment.
* Footer - The footer has links to social media accounts these are defaulted to the homepage of the social media platform as no accounts exist for LBK. Opening and closing times and a link to homepage are also included.
* Logo - The LBK logo is a subtle burger and initial logo which acts a link to the homepage.
* Navbar - The Navbar allows users an easy navigation through the site for registered and non-registered users. Some navigational links have access only for authenticated users or superusers and is accessible on all pages, the Navbar links consist of Menu, Order, Admin, My Account and Checkout.

### Menu
* Menu - Menu in the Navbar takes user to the products page, which displays all products in cards format. When the card image is clicked or hovered on the card displays the product name description and more info button for all users, for superusers edit and delete buttons are visible. Included on this page is a search functionality that allows users to search for products based on name and description. Users can filter products based on category type which returns all products in that category.  
* Product Details - When user clicks on the more info the product details appear which displays name, price, category, ingredients and if sutible for vegetarians. Non authenticated users see an option to login or register to place order, authenticated users can add quantity and add to cart. Superusers also have button options to edit product details or delete product.

### Order
* Order - Order in the navbar has a dropdown option that allows users the options to place an order, view customer burgers and create a custom burger.   
* Place Order - Place order allows authenticated users to view a list of all products split by category, adjust the quantity and add to cart. 
* Build your Own - Custom burgers view allows the users to view all customer burgers created by other users and to create their own.
* Create your own - Create your own view allows users to create their own brger and add to cart. The ingredients are split by category and the user can choose what they want in their burger as well as give it a creative name.

### Checkout
* Shopping Cart - The shopping cart displays the product details that have been added to the cart the user can see product image, name, price, quantity, subtotal, cart total, delivery costs and grand total. the user can continue shopping or checkout.
* Checkout Page - The checkout page utilises Stripe to process user payments, this page has order summary, client details, delivery info and payment info. The Client details and delivery info are populated from the user profile if completed or if they have ticked the option to save delivery info on previous transactions. The payment info uses stripes standard layout of card number, expiry, cvc and also displays error notification regarding card details. Once user clicks secure checout the user is the greeted with a custom loading page followed by a order confirmation, containing order info, order details, delivery info and billing info and a email confirmation is sent to the email address provided.    

### My Account
* User Profile Page - The authenticated user profile page is accessed from My Account in the navbar, this displays the users profile name, profile picture, username, email, delivery info and order history, which the user cand click on to see the past order confirmtion details 
* Update Profile details - User can update their username, email, profile picture and delivery info. 
* User Order History - The Order history gives a brief overview of the order order number, date, status, items and total. Users can click on order number to view the confirmation order.

### Admin
* Admin - The admin section in the navbar allows store owners the ability to add products, see the orders for that day and all orders.
* Add Product - The add product allows superusers the abillity to add new products via a form to the database by completing the relevant fields.
* Todays Orders Dashboard - Todays orders shows the store owner a breakdown of total revenue and a count of how many orders have been recieved that day. Underneath this is two tables one for active orders and the other for completed orders. The tables display basic information about the order id, total, order at, name, email and status. When the row is clicked on the complete order details are displayed.  
* Order Details/Status Update - The order details display the order info and status which can be updated by store owner to order recieved (default), order cooking, out for delivery and delivered. When order is updated to delivered the order is moved from the active table in the order dashboard to completed.
* Order History - The Order history allows the store owner the ability to see all orders and has the ability to serach all orders for the name, id, email, status and ordered on that way if a custome complains the owner can search his order and pull up the order information.
* Django All Auth
* Sign Up - The sign up allows new users to register and create a profile by completing the registration form.
* Login - Allows registered users the ability to sign in. 
* Forgot Password - Allows users the ability to reset their password.
* Logout - Allows the users to logout.
* Back to Top - Features on the right hand side of the screen and allows the users the ability to return back to top of the screen.

## Future Development
* Order Delivery tracker - Allows useres the ability to track their order 
* Apple & Google Pay - Allows the users to pay using Apple pay or Google Pay
* Social Account Login feature - Allows user the ability to sign in with their social accounts such as facebook
* Voting buttons - Allows the users the ability to vote if they like the custom burger

 
## Database Structure


1. Profile
- User Profiles

2. Products 
- Categorys
- Custom_burgers
- Ingredients
- Products

3. Customers
- Reviews

4. Checkout
- Orders


# Technologies Used
 
 **Languages** 
- HTML
- CSS
- Python
- Javascript
- Jinja
 

**Libraries & Frameworks**
   
[Django](https://www.djangoproject.com/):
 Django Framework was used to creat this project. 

[Bootstrap](https://getbootstrap.com/):
 Bootstrap was used throughout the site to help design and customize and help with 
 
[Font Awesome](https://fontawesome.com/):
 Font Awesome was used to provide the Icons throughout this website.

[Google Fonts](https://fonts.google.com/):
 Google fonts was used to import the font into the style.css file

[JQuery](https://jquery.com/):
 JQuery was used to enable scripts 

[Pillow](https://pypi.org/project/Pillow/):
 Pillow was installed as imaging library for this project.
 
[Gunicorn](https://gunicorn.org/):
 Was installed and used as the webserver

[Psycopg2](https://pypi.org/project/psycopg2/):
 Psycopg2 was utilised as the PostgreSQL database adapter for the project.
 
[Stripe](https://stripe.com/gb):
 Stripe was used for the online payment processing when customer uses the checkout.
 
[Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/):
 Django Crispy Forms was used to render the behavior of the forms in this project.

[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html):
 Boto3 was used along with AWS to create, configure, and manage AWS services.

[Django Storages](https://django-storages.readthedocs.io/en/latest/):
 Django Storages was used as the backend storages for connecting with S3

**Tools**

[Git](https://git-scm.com/): 
 Git was used by utilizing the Gitpod terminal to commit to Git and push to GitHub.

[GitHub](https://github.com/):
 GitHub was used to create a repository and store the code after it was pushed from Git.

[Pip](https://pip.pypa.io/en/stable/installing/):
 Pip was used to istall python packages/modules required for the project.

[Heroku](https://www.heroku.com):
 Heroku was used to deploy my app.

[AWS S3 Bucket](https://aws.amazon.com/):
 AWS S3 was used to store the static files and the images for the project.

[Balsamiq](https://balsamiq.com/):
 Wireframes were created using Balsamiq

[Pixabay](https://pixabay.com/):
 Pixabay was used to source the background imagery for the webpage and Burger Images.

[Istock](https://www.istockphoto.com/): 
 Istock was used to source the background imagery for the webpage and Burger Images.

[Pexels](https://www.pexels.com/):
 Pexels was used to source the background imagery for the webpage and Burger Images.

[Imgur](https://imgur.com/): 
 Was used to upload my images and create a url for the database upload.


**Databases**

[SQlite3](https://sqlite.org/index.html):
 SQLite3 was used as the developmental database before deploying to Heroku.

[PostgresSQL](https://www.postgresql.org/):
 Postgres SQL was used as the relational database after to deploying to Heroku.

# Testing
### Code Validation
The Freeformatter HTML Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no errors in the project.

[CSS Validator](http://jigsaw.w3.org/css-validator/) - [Results]()

[HTML Validator](https://validator.w3.org/) - [Results](docs/) the results show a warning "lack of heading for section", the section displays 
the flash messages that displays success/error messages when user logs in, adds/removes files.

[JSHint](https://jshint.com/) - [Results](docs/)

Lighthouse was used on Google Chrome to help improve perfomance and accessability. This helped improve the contrast issue with background
and foreground colours - [Results](docs/)


### Devices
The website was tested on laptop, desktop, iphone, ipad on the following browsers:
- Google Chrome
- Microsoft Edge
- Safari
- Firefox 

### Manual Tests for functionality of features
### 1. Responsive on all devices 
- Chrome Dev Tools was used to check the sites compatiability all all devices. 
- A link to the site was tested on iphone and ipad.
### 2. Home page
- The homepage animations were tested to ensure that when the page loads and refreshed the welcome animations work, also the scroll animations were tested. 
- The button links  on the homepage for Place Order, Our burgers, About us, our suppliers and reviews were all clicked and the appropriate page was loaded.
### 3. Place Order 
- The Place order button was clicked and the relevant page was returned. For non authenticated users they are directed to the login page authenticated users are directed to the place order view.
- The close button was clicked and was returned to the homepage.
### 4. Our Burgers
- The view menu button in the our burger section was clicked and the menu page was returned.
- The close button was clicked and was returned to the homepage.
### 4. About Us
- The about us button in the about us section was clicked and the relevant page was returned.
- The create your own burger button was clicked and the custom burger page was returned.
- The close button was clicked and was returned to the homepage.
### 5. Our Suppliers
- The our suppliers button in the Fresh ingredients section was clicked and the relavant page was returned.
- The links to all suppliers was clicked and the homepage for theat company was returned in a new window. 
- The close button was clicked and was returned to the homepage.
### 6. User Reviews 
- The reviews button in the Reviews section was clicked and the relavant page was returned.
- Test reviews were added to the database and the review was displayed on the list of reviews. 
- The review title was clicked and the review comments, rating, username and date was displayed as a dropdown.
- The close button was clicked and was returned to the homepage.
- The Add Review button was clicked and the form  to add a review was returned.  
### 7. Add review
- The add review form was completed and submitted and a review was posted to the database and displayed on the reviews section.
### 8. Footer
- The social links were all clicked to ensure that the relevant link opened in a new window.
- The burger icon was clicked and the homepage was returned.
### 9. Logo
- The burger icon was clicked and the homepage was returned.
### 10. Navbar
- The Navbar links were all tested on the main navbar, the appropriate pages opened when clicked.

### 11. Menu
- The Menu link was clicked and all the products were returned.
- All cards were tested to ensure that when hovered or clicked that the product name, description, price and more info button are shown.
- The cards were tested to ensure that when logged in as a superuser the edit and delete buttons are displayed, the edit and delete buttons were tested. 
- The more info button was clicked and the product details were returned, this was tested as a non-authenticated user, as a authenticated user and a superuser. As a non-authenticated user returns the product info and a link to login or register, logged in as a authenticated user allows the user to select quantity and add to cart and as a super user edit and delete buttons are visible.

### 12. Order
- The Order link was clicked and the options for place order and build your own were available. 
- The Place Order button was clicked as a non-authenticated user the login page is returned, as a authenticated user the order page is returned.
- Items were added to the cart at different quantities to ensure they worked.
### 13. Build your own
- The Build your Own link in the navbar was clicked and the custom page was returned which displays all custom burgers that have been created by users.
- The Create your own burger button was clicked this was tested as a non-authenticated user when clicked was redirected to the login page and for authenticated users the create your own form was returned.

### 14. Create your own
- Various Custom Burgers were created using the form, multiple ingredients were selected from the same category, custom name was inputted and the create burger button was clicked and the success message appears.
- The quantity was tested and the created burger was then added to the cart. 

### 15.(a) My Account - Non-authenticated
- The register functionality was tested by creating various users, tested using the same email address or username as already created users to test that the error message works.
- The signin functionality was tested by logging in with created users and tested using incoorect username and passwords.
- The forgot password link on the login was tested to change the password of an existing user.  

### 15.(b) Account - Authenticated
- The logout link was tested to ensure that the logout page was returned.
- The My Profile link was tested to ensure that the correct profile page and user information was returned.
- The Update Profile button was clicked and the username, email address, delivery info and profile picture were changed and updated by completing the form and clicking the update button. 
- clicking the order id in the order history in the profile page returns the order confirmation along with a message confirming this is an old order. 

### 16. Checkout
- The shopping cart link was clicked with items in and out the bag, when clicked with an empty cart the user is greeted with a screen confirming the cart is empty and a still hungry? button when clicked returned the Menu page.
- When Items are added to cart a success message appears with confirmation of the product name added to the bag and a break down of items in the cart and a subtotal.
- After Adding Items to cart the cart button was clicked which returns the shopping cart which shows the product image, name, price, quantity, subtotal, cart total, delivery costs, grand total, Still Hungry? button and secure checkout.
- The quantity update and remove buttons were tested when items were increased or decreased and updated the subtotal changes to the correct ammount. When remove is clicked the item is removed from basket and the totals are updated.
- The Secure Checkout button was clicked and the checkout page was loaded.   

### 16. Checkout Page    
- The checkout page was tested using stripes test card numbers to make purchase, which was successfully processed and order appeares in the database and order history, after completing payment a confirmation email was recieved with breakdown of order. 

### 17. Admin
- The admin link in the navbar only displays when logged in as a superuser this was tested by logging in as a regular user. 
- The Add Product was tested by completing the form and adding new product to the database, this item was then searched for on the menu page and by using the filter options and the search bar.
- Todays Orders Dashboard was tested by completing multiple orders through the secure checkout the total orders and the total revenue displayed the correct amount.  
- The order update was tested by clicking on an order and changing the order status to all of the options and update them. When updated to delivered the orders were moved from active to completed.
- The Order History was tested by searching for order id, name, email, status and order at and the relevant order/orders was returned.
- Clicking on the reset returned all orders

### 18. Back to Top
- The back to top was tested on relevant pages and when clicked they page returns to the top.


## Testing User Stories

**External User Goals:**

As a User....
*  I expect to access the website from any device, so that I can use the website anytime and anywhere.
    (a)  The website has been developed to be mobile responsive and can be used accross multiple platforms.
*  I expect to easily navigate the website, so that I can quickly find what I'm looking for.
    (a)  The Navbar helps users navigate the site.
    (b)  Close buttons allows usere the ability to go back to previous page.
    ![]()
*  I want to find an information about the company, to know what they do, what their main principles and ideas
    (a)  The About us section gives the users some additional information about the company.
*  I want to see the location of the LBK.
    (a)  The Address of LBK can be found on the About us section.
*  I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
    (a)  The User can click on the email icon in the social link to send emails to LBK
    (b)  LBK telephone number can be found in the contact us section of the about us page.
    (c)  The email address can be found on the confirmation email in case there is a problem.
*  I want to view all available products.
    (a)  The Menu page allows useres to see all products and can be filtered by category type
    (b)  The Order page allows users to see a simplistic menu page of all products.
*  I want to view product details (e.g. image, price, description, ingredients), so that I can make an informed decision before I buy.
    (a)  The menu page gives the user brief information about the product.
    (b)  The more info button takes users to the product details page where more information can be found.
    (c)  The place order page gives the user simplistic but relevant information about the product.
*  I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
    (a)  The Menu page allows the users to search for keywords that are either in the name or in the description of the product.
    (b)  The User can narrow down the product based on category type in the menu section.
*  I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
    (a)  Users can update and remove items from their cart in the shopping cart screen.
    (b)  Users can continue to shop if they have missed an item by using the still hungry button.
*  I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
    (a)  The shopping cart and the checkout page clearly breakdown the cost by subtotal, order total, delivery costs and a grand total.
    (b)  Underneath the payment section in the checkout it clearly states the total the card will be charged.
    (c)  When adding items to cart the user is greeted with a success message which informs the user the cost excluding delivery.
    (d) The Cart Icon in the Navbar shows the user the subtotal of their cart at all times.
*  I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
*  I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.
    (a) on succesful completion the user recieves an order confirmation.


### New Users
As a new user....
* I want to create my own account, so that I can save, view and edit my profile details and view my order history.
    (a)  The all auth allows users the ability to create an account using the register.
    (b)  When logged in the user can view their account at all time by clicking my account and my profile.
    (c)  The user can update their info and profile picture using the update profile button in my profile page.
    (d)  The user can see all their orders on the profile page and by clicking the order id for more detail.

### Returning users
As a returning user....
*  I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
    (a)  The user can tick the remember me on the login page for easy access.
    (b)  On completion of first order the user can tick to store their information to their profile page which will autofilled on next purchase.
    (c)  The user can enter their information to their profile page which will be used as default against purchases.
*  I want to reset my password if I forgot it, so that I can get access to my profile again.
    (a)  The user can reset their password via the login section by clicking forgot password.
*  I want to be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details.
    (a)  The user can reset their password via the login section by clicking forgot password.
*  I want to be able to change my email.
    (a) The user can update email address by accessing their profile page and clicking update profile.

 
### Website Owner(admin)
As a Site owner....
*  I want to secure admin interface avalable only for website admin, so that I can add, edit and remove products.
    (a)  Superusers can access the stores admin page to access the database.
    (b)  Superusers can add products throurgh the Admin section of the Navbar.
    (c)  Superusers can edit and delete particular products through the menu page and/or the product details page.   
*  I want to be able to view orders recieved  for that day and update the order status.
    (a)  Superusers can see all orders for that day by using the Todays orders in the Admin section of the navbar.
*  I want to be able to differentiate between active orders and completed orders for the day.
    (a)  The order dashboard is split into two tables the top for active the bottom for completed.
    (b)  The order status in the dashboard confirms the status of the order.
*  I want to be able to view history of all orders recieved.
    (a)  Superusers can see the complete order history by clicking the Order History in the admin section of the navbar.
      
 

    
## Bugs
- After deploying to Heroku Menu image links were broken as the file url wasn't included in the media folder upload. These were added in the admin section.

- After deploying a Server Error 500 message appeared after confirming payment in the checkout app. Debug was turned back on to True to discover where the issue was ![error](static/images/error.png). This error was due to the order_id in the models.py having a max-length of 28 when the UUID is 32 characters. This issue was corrected and migrations where ran but the error still occured. After contacting Tutor support it was highlighted that there were existing orders in the developembntal database that was causing this error. These orders were deleted from the admin section, the postgress database was reset and the data was dumped into jason.db and reimported.

- After creating the Custom_burger cfreator an integrity Error occured on the Heroku app when clicking the create burger button. This error was resolved by adding a price field in the Custom_burger model and giving it a default value.


# Deployment 

Lees Burger Kitchen was developed using [GitPod](https://www.gitpod.io/) using Git & GitHub for version control. 
It is hosted on the [Heroku](https://heroku.com/) platform, with static files hosted in AWS S3 Basket.

### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/)    

Accounts will need to be created for the following services:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- An Email account for this project I used [Gmail](https://mail.google.com/)

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/Leeap83/Lee-s_Burger_Kitchen.git`          

More information about the cloning process can be found here: [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).   

2. Set up environment variables.     
Note, that this process will be different depending on IDE you use.   
In this it was done using the following way:      
    - Create `.env` file in the root directory.
    - Add `.env` to the `.gitignore` file in your project's root directory
    - In `.env` file set environment variables with the following syntax:     
    ```bash 
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
     ```
    
3. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`     
4. In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
5. Load the data fixtures(**categories**, **products**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`        
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`   
7. You will now be able to run the application using the following command:     
`python3 manage.py runserver`     
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
The project was deployed to [Heroku](https://dashboard.heroku.com/apps) Pages using the following steps...

To deploy the project on heroku, take the following steps:

1. If not already present, create a requirements.txt file using the command:

    pip freeze > requirements.txt

2. If not already present, create a `Procfile` with the command:

    echo web: python app.py > Procfile

3. Push the the project to GitHub.

4. Log in to your Heroku account and create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the 
"New" button in your dashboard. Give it a name and set the region to the one closest to you, then click the "Create app" button.

5.  Click on "Deploy" tab and under "Deployment method" and select GitHub. Select the correct repository and click "Connect".

6. Click on the "Settings" tab and under "Config Vars" click "Reveal Config Vars" and enter the Key and values stored in
the env.py file:
                 
| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |
  

7. In the "Manual Deployment" section of this page, make sure the master branch is selected and then click "Deploy Branch".

8. The site is now successfully deployed, click the "Open app" button to visit it.



# Credits

**Code**
* [Code Institute](https://codeinstitute.net/) The project's code was developed by following the video lessons for the Boutique Ado Django Mini-Project, but was customized, modified and enhanced to fit the project purposes. 
* Animation on the homepage was implemented following JulioCodes [Youtube](https://www.youtube.com/c/JulioCodes)
* Kevin Loughrey & Scott Kipp from tutor support for help with my "Server Error 500" error.

**Content & Media**

Burger Images and homepage images were downloaded from Pexels from the following Users:
* https://www.pexels.com/@taryn-elliott
* https://www.pexels.com/@valeriya
* https://www.pexels.com/@atomlaborblog
* https://www.pexels.com/@jonathanborba
* https://www.pexels.com/@seyed-ali-hosseini-1226419
* https://www.pexels.com/@geraud-pfeiffer

Istock Credits were purchased and images were downloaded from the following:
* https://www.istockphoto.com/portfolio/vaaseenaa?mediatype=photography
* https://www.istockphoto.com/portfolio/comicsans?mediatype=illustration
* https://www.istockphoto.com/portfolio/Fudio?mediatype=photography
* https://www.istockphoto.com/portfolio/bhofack2?mediatype=photography


**Acknowledgements**

* My Mentor Aaron Sinnott for feedback
* Code Institute for training
* Tutor Suport for assistance with code errors
* Slack for reference on coding issues
* WS3 schools for reference on coding issues
* Stackoverflow for reference on coding issues
* YouTube online tutorials used when encountered coding issues