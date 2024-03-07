from fastapi import FastAPI
from routes.controller import filters, dashboard, orders, overview
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# different routes to create
# /dashboard - total number of orders and total sales
# how the filter works for dashboard
# product - show the total number of orders and total sales 
# state - product on this state - show the total number of orders and total sales
# city - state, city - show the total number of orders and total sales
# from and to - state, city, fromandto - show the total number of orders and total sales

# /order - shows all the orders - will have filters
# how will filters work
# product - 
# state - show all the orders in this state
# city - show all the order in this city and state
# fromandto show all the orders between two dates and from specified city and state
# /filters - product, state, city and from and to  total number of order and sales

origins = [
    "http://localhost",  # Add your frontend's domain here
    "http://localhost:3000",  # Example for React's development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can specify headers (e.g., ["Authorization"])
)

app.include_router(filters.router)
app.include_router(dashboard.router)
app.include_router(orders.router)
app.include_router(overview.route)

@app.get("/")
async def root():
    return {"message": "Hello World"}