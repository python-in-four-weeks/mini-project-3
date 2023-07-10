from flask import Blueprint, request, jsonify, abort
from datetime import date, timedelta
from ..config.sqlalchemy import db
from ..models.book import Book
from ..models.customer import Customer
from ..models.loan import Loan

loan_endpoints = Blueprint("loan_endpoints", __name__, url_prefix="/loans")
