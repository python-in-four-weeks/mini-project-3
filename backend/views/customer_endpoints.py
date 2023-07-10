from flask import Blueprint, request, jsonify, abort
from sqlalchemy.exc import IntegrityError
from email.utils import parseaddr
from ..config.sqlalchemy import db
from ..models.customer import Customer

customer_endpoints = Blueprint("customer_endpoints", __name__, url_prefix="/customers")
