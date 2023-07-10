# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:02:01 2023

@author: James Curtis Buckler
"""
def compute_loan_repayment(PV, r, n):
    """
    Compute the loan monthly repayment amount.

    Parameters:
    PV : float - Present Value or loan principal amount
    r : float - Annual interest rate as a decimal
    n : int - Number of months

    Returns:
    Pmt : float - Loan monthly repayment amount
    """
    r = r / 100  # Convert APR to a decimal

    Pmt = r * PV / (1 - (1 + r) ** -n)
    return Pmt

PV = 12000
r = 7.45
n = 48

monthly_repayment = compute_loan_repayment(PV, r, n)
print(f"The monthly repayment amount is: {monthly_repayment}")

