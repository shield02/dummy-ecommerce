This project was created with Django

## About the project
This project goal is to create a web application that is similar to amazon; it is an E-Commerce website for vendors to sell their products with one click and get customer traction easily. It helps customers deliver the item to their doorstep at a minimal price and within a short time. This website is specified for some products; How to 'Add To Cart' and a 'Payment Integration' utility is implemented.

## Aspects of the project

### Admin panel
Admin can add the retailer to change his status, approve or reject. He can see how many retailers are there, how many are approved and how many are pending with status. An admin can monitor total deliveries, pending payout, retailer’s personal information, bank details, and subscription that the retailer has selected. In certain conditions, the admin can remove the retailer as well. Admin has the authority to do everything; he has permission to see all deliveries with small things like payments, history, customer information, and retailer information. He can download all the data in a CSV file. The main functionality is adding items in the Item table, generating a promo code for retailers, and adding the sub-category for retailers. Similarly, he can update or delete the functionality.  

### Customer panel
Customers can access all of the products added by the admin. He can create his own account. He does not require any permission from the admin or retailer to sign up. He can add the product to the cart and buy the products. There is functionality for online payment which we did through third-party API. At one time, customers can only buy products from the same retailer and not from others. In case the customer declines the previous cart or successfully buys products then only he is allowed to buy from other retailers. 

### Retailer panel
The retailer has the choice of selling products. The retailer can add their business hours for customers when the product is available. They can update their bank account and see the payment history of items sold. The data can be downloaded in CSV format. They can manage the delivery of items requested by customers, see all the information on orders, take action on it, and see the total revenue generated through delivery. On the dashboard page, they can see customer count and repeated customers and have a filter to check monthly details. 