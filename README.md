# E-Commerce Automation Project

## Project Overview

This project is an automation test suite for an unspecified e-commerce website. The primary goal of this project is to automate key user interactions and verify the functionality of various features on the site. The automation scripts were developed using Python and Selenium.

#### Test Cases
*Opening the E-Commerce Website with Notifications Disabled:* The site is launched with all browser notifications turned off to ensure they do not interfere with the testing process.

*Scrolling to the Footer and Selecting a Random Category:* The script scrolls to the bottom of the page and randomly selects a category from the footer section.

*Choosing the Third Product in the Selected Category:* Once a category is selected, the script navigates to that category's page and selects the third product listed.

*Navigating to Product Details and Adding to Cart:* The script goes to the selected product's detail page, gathers product information, returns to the previous page, and adds the product to the cart.

*User Login:* The script automates the login process by entering valid credentials. Note: Captcha is handled manually and must be completed within 15 seconds.

*Navigating to the Cart Screen:* After logging in and adding the product to the cart, the script proceeds to the cart screen, verifying that the product has been successfully added.