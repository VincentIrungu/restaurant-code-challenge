#models.py
from sqlalchemy import create_engine, Column, Integer, String, Table,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()



class Restaurant(Base):
    __tablename__='restaurants'
    id=Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Float())
    
    review=relationship('Review', backref='restaurant')
    customers=relationship('Customer', secondary='restaurants_customers', back_populates='restaurants')

    def all_restaurants_reviews(self):
        return self.review
    
    def all_restaurant_customers(self):
        return self.customers
    
    def full_restaurant_reviews(self):
        return f"Review for {self} by {self.customers}: {self.review} stars."
    
    @classmethod
    def fanciest(cls):
         return session.query(cls).order_by(cls.price.desc()).first()
        
     
    def __repr__(self):
        return f'<Restaurant {self.name}>'


class Customer(Base):
    __tablename__='customers'
    id=Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    review=relationship('Review', backref='customer')
    restaurants=relationship('Restaurant', secondary='restaurants_customers', back_populates='customers')

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def all_customer_reviews(self):
          return self.review
    def all_customers_restaurants(self):
          return self.restaurants
    def full_name(self):
         return f"{self.first_name} {self.last_name}"
    def favorite_restaurant(self):
         max_review = max(self.review, key=lambda review: review.rating)
         return max_review.restaurant
    def add_review(self,restaurant,rating):
         new_review=Review(rating=rating,customer=self,restaurant=restaurant)
         session.add(new_review)
         self.review.append(new_review)
         session.commit()
         print(f"New review for {self.restaurants} added successfully!")

    def delete_reviews(self,restaurant):
        session.query(Review).filter_by(restaurant_id=restaurant.id).delete()
        session.commit()
        print(f'Review for {restaurant} deleted successfully')


    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'


"""class Review(Base):
    __tablename__='reviews'
    id=Column(Integer(),primary_key=True)
    rating=Column(Float())
    customer_id=Column(Integer(), ForeignKey('customers.id'))
    restaurant_id=Column(Integer(),ForeignKey('restaurants.id'))
    
    def __init__(self,rating,customer,restaurant):
        self.rating=rating
        self.customer=customer
        self.restaurant=restaurant

    def customer_review(self):
        return self.customer
    def restaurant_review(self):
        return  self.restaurant
    def full_review(self):
        return f"Review for {self.restaurant} by {self.customer}: {self.rating} stars."

    def __repr__(self):
        return f'< Review {self.rating}>'"""


  
    
"""restaurants_customers=Table(
    'restaurants_customers',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)
   
"""
   

engine=create_engine('sqlite:///restaurants.db')

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

