# Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

# Setup Instructions

## Install Dependencies:

1. Clone the repository.
2. Install dependencies (`pip install -r requirements.txt`)

## Create Virtual Environment:
1. Open a terminal or command prompt.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the command:
    python -m venv your_environment_name
4. Once the virtual environment is created, you need to activate it. On Windows, run:
    your_environment_name\Scripts\activate
5. When you're done working in the virtual environment, you can deactivate it by running:
    deactivate

## Set Up a new project with a single application

1. django-admin startproject your_project_name
2. cd your_project_name directory
3. django-admin startapp your_appname

## Database Migration

1. python manage.py makemigrations
2. python manage.py migrate

## Superuser creation and Token Generation:

1. python manage.py createsuperuser
2. pip install httpie
3. http POST http://127.0.0.1:8000/api-token-auth/ username=<your_username> password=<your_password>

## Running the server:

python manage.py runserver

## Access Django Admin:

Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. this is to access the database as a admin user.

## How to run a api endpoint:

1. First we need to make sure that we migrated the models to database
2. Then we need to start the server using "python manage.py runserver" command.
3. Then we need to open another cmd prompt and open virtual environment and open the project folder and provide httpie commands.

## Testing or Using the API endpoints:

We can test API endpoints using httpie commands.

## Create a Vendor:

using httpie:
    http POST http://127.0.0.1:8000/api/vendors/ vendor_code=01 name="Vendor 1" contact_details=5689412035 address="Address 1" on_time_delivery_rate=8 quality_rating_avg=6 average_response_time= 6 fulfillment_rate=5 "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to create a vendor by providing the vendor details.

## List all vendors details:

using httpie:
    http http://127.0.0.1:8000/api/vendors/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to get the details of all vendors.

## Retrieve a specific vendor's details:

using httpie:
    http http://127.0.0.1:8000/api/vendors/vendor_code/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to get the details of vendor with vendor_code which was mentioned in the command.

## Update a vendor's details:

using httpie method:

    PUT Method:
        http PUT http://127.0.0.1:8000/api/vendors/vendor_code/ vendor_code='Update code' name="Updated name" contact_details="update contact" address="updated address" on_time_delivery_rate='update rating' quality_rating_avg='updated rating' average_response_time='updated rating' fulfillment_rate='updated rating' "Authorization: Token your_obtained_token"

    Patch Method:
        http PATCH http://127.0.0.1:8000/api/vendors/vendor_code/ name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"

    About this API endpoint:
        Here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new vendor with given details). The PATCH method is used to update the vendor's details. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.

## Delete a vendor:

using httpie:
    http DELETE http://127.0.0.1:8000/api/vendors/vendor_code/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to delete the vendor with given vendor_code.


## Create a purchase order:

using httpie:
    http POST http://127.0.0.1:8000/api/purchase_orders/ po_number=1 vendor=01 order_date="2023-01-01" delivery_date="2023-01-10" items='[{"item_name": 20 }]' quality_rating=4.5 issue_date="2023-01-01" status="Pending" acknowledgment_date="2023-01-02" "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to create a purchase_order with given details.

## List all purchase orders details:

using httpie:
    http http://127.0.0.1:8000/api/purchase_orders/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to get the details of all purchase orders.

## Retrieve a specific purchase order's details:

using httpie:
    http http://127.0.0.1:8000/api/purchase_orders/po_number/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to get the details of purchase order with given po_number.

## Update a purchase order's details:

using httpie:

    PUT method:
        http PUT http://127.0.0.1:8000/api/purchase_orders/po_number/ po_number="Updatedpo" vendor="updatedcode" order_date="2023-01-02T12:00:00" delivery_date="2023-01-15T12:00:00" items:='[{"item_name": 20 }]' quality_rating:=4.8 issue_date="2023-01-01" status="updated" acknowledgment_date="2023-01-02" "Authorization: Token your_obtained_token"

    PATCH method:
        http PATCH http://127.0.0.1:8000/api/purchase_orders/po_number/ order_date="2023-01-02T12:00:00" delivery_date="2023-01-15T12:00:00" items:='[{"item_name": "Updated Item", "quantity": 20 }]' quality_rating:=4.8 status="updated" "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new purchase_order with given details). The PATCH method is used to update the purchase_order's details. Here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.(we can provide any no of fields in PATCH mathod.)

## Delete a purchase order:

using httpie:
    http DELETE http://127.0.0.1:8000/api/purchase_orders/po_number/ "Authorization: Token your_obtained_token"

About this API endpoint:
    Here this endpoint is used to delete a purchase order with given po_number.

## Retrieve a vendor's performance metrics:

using httpie:
    http http://127.0.0.1:8000/api/vendors/vendor_code/performance/ "Authorization: Token your_obtained_token"

About this API endpoint:
    1. Here this endpoint is used to retrieve the performance metrics of a vendor with given vendor_code.This performance metrics contains on_time Delivery rate, quality rating average, average response time, fulfilment rate.
    2. On time delivery rate is calculated each time a PO status changes to "completed".Tthis is the average of no of po delivered before the delivery_date and no of total po's delivered.
    3. quality rating average is calculated after every po completion and it is the average of all ratings given to that specific vendor.
    4. average response time is calculated each time a po is acknowledged by the vendor.It is the time difference between issue_date and acknowledgment_date for each po, and then the average of these times for all po's of the vendor.
    5. fulfillment rate is calculated when po status is set to "completed".This is the average of no of successfully fulfilled pos (status = "completed" without issues) by the total no of pos issued to the vendor.

## Update acknowledgement_data and trigger the recalculation of average_response_time:

using httpie:
    http PATCH http://127.0.0.1:8000/api/purchase_orders/po_number/acknowledge/ "Authorization: Token your_obtained_token" acknowledgment_date="2023-12-20T12:00:00Z"

About this API endpoint:
    Here this endpoint is used to acknowledge the purchase_order with given po_number and trigger the recalculation of average_reponse_time.
